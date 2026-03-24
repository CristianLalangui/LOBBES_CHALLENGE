from django.urls import path
from forms_management.views import *


urlpatterns = [

    path("form/step1/", FormView1.as_view()),
    path("form/step2/", FormView2.as_view()),
    path("form/step3/", FormView3.as_view()),
    path("form/step1/submit/", FormView1.as_view()),
    path("form/step2/submit/", FormView2.as_view()),
    path("form/step3/submit/", FormView3.as_view()),
    path("form/addTasks/", TaskView.as_view()),
    path("form/updateTasks/", TaskViewActualizarDatos.as_view()),




]