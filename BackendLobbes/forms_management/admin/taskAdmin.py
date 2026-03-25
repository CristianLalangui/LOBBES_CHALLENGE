
from django.contrib import admin

from forms_management.models.taskModel import TaskModel


@admin.register(TaskModel)
class taskAdmin(admin.ModelAdmin):

    list_display = ("email","taskId","formStep","formDate","status","leadId","title")
    search_fields = ("form_step",)







