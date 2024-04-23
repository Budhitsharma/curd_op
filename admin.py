from django.contrib import admin
from myapp.models import Detailmodel

# Register your models here.
class Detailadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact', 'technology', 'join_date')

admin.site.register(Detailmodel, Detailadmin)