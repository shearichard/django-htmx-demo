from django.contrib import admin

from .models import CountLocation 
from .models import CountPoint 

admin.site.register(CountLocation)
admin.site.register(CountPoint)
