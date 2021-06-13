from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


from .models import Menu

# Register your models here.

class MenuResource(resources.ModelResource):
    class Meta:
        model = Menu

@admin.register(Menu)
class MenuAdmin(ImportExportModelAdmin):
    ordering=['id']
    list_display = ('id','nameid','name','price','calorie','picture','link','judge')

    resource_class = MenuResource