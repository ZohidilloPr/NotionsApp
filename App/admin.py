from django.contrib import admin
from .models import NotionModel

# Register your models here.



class AdminNotionModel(admin.ModelAdmin):
    list_display = ('aim','about','impt')
    fields = ['aim','about', 'impt',]

admin.site.register(NotionModel, AdminNotionModel)
