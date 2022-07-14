from django.contrib import admin

from .models import Band, Shirt, Award

# Register your models here.
admin.site.register(Band)
admin.site.register(Shirt)
admin.site.register(Award)
