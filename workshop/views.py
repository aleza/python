from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from .models import Owner
from .models import Brand
from .models import Model
from .models import Repair


def index(request):
    latest_owners_list  = Owner.objects.order_by('surname')[:]
    latest_brands_list  = Brand.objects.order_by('owner')[:]
    latest_models_list  = Model.objects.order_by('brand')[:]
    latest_repairs_list = Repair.objects.order_by('model')[:]
    context = { 'latest_owners_list' : latest_owners_list,
                'latest_brands_list' : latest_brands_list,
                'latest_models_list' : latest_brands_list,
                'latest_repairs_list': latest_repairs_list
                }
    return render(request, 'workshop/index.html', context)

def brands(request, owner_id):
    owner   = get_object_or_404(Owner, pk=owner_id)   
    brand   = get_object_or_404(Brand, pk=owner_id) 
    model   = get_object_or_404(Model, pk=owner_id)
    repair  = get_object_or_404(Repair, pk=owner_id)
    latest_brands_list  = Brand.objects.order_by('owner')[:]
    latest_models_list  = Model.objects.order_by('brand')[:]
    latest_repairs_list = Repair.objects.order_by('model')[:]    
    context = { 'owner' : owner,
                'brand' : brand,
                'model' : model,
                'repair': repair,
                'latest_brands_list'  : latest_brands_list,
                'latest_models_list'  : latest_models_list,
                'latest_repairs_list' : latest_repairs_list
                }
    return render(request, 'workshop/cars.html', context)
        
def repairs(request, owner_id):
    owner   = get_object_or_404(Owner, pk=owner_id)   
    brand   = get_object_or_404(Brand, pk=owner_id) 
    model   = get_object_or_404(Model, pk=owner_id)
    repair  = get_object_or_404(Repair, pk=owner_id)
    context = { 'owner' : owner,
                'brand' : brand,
                'model' : model,
                'repair': repair
                }
    return render(request, 'workshop/repair.html', context)        

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


