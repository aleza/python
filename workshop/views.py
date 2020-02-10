from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Owner
from .models import Brand
from .models import Model
from .models import Repair


def index(request):
    latest_owners_list = Owner.objects.order_by('surname')[:]
    context = {'latest_owners_list': latest_owners_list}
    return render(request, 'workshop/index.html', context)

def brands(request):
    latest_brands_list = Brand.objects.order_by('brandName')
    brand = {'latest_brands_list': latest_brands_list}
    return render(request, 'workshop/cars.html', brand)

"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def student(request):
    student_list = Estudiante.objects.order_by('nombre')[:]
    context = {'student_list': student_list}
    return render(request, 'student/index.html', context)    

def students_detail(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    return render(request, 'student/detail.html', {'estudiante': estudiante})    

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
"""


