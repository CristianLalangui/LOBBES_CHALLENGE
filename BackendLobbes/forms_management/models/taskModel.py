from django.db import models



class StepFormChoices(models.TextChoices):


    STEP1 = "1", "1"
    STEP2 = "2", "2"
    STEP3 = "3", "3"

class TaskModel(models.Model):

    email = models.CharField(max_length=50,unique=False,blank=False,null=False)
    taskId = models.CharField(max_length=50,unique=False,blank=False,null=False)
    leadId = models.CharField(max_length=50,unique=False,blank=True,null=True)
    formDate = models.DateTimeField(max_length=50,unique=False,blank=False,null=False)
    status = models.CharField(max_length=100, default="Form 1 pending")
    title = models.CharField(max_length=50,unique=False,blank=False,null=False)


    class Meta:
        db_table = 'tasks'
        verbose_name = "Task"
        verbose_name_plural = "Tasks"