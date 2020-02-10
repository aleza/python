from django.contrib import admin


from .models import Owner
from .models import Brand
from .models import Model
from .models import Repair


admin.site.register(Owner)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Repair)
