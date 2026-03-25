import os

from rest_framework import status, request
from rest_framework.response import Response
from rest_framework.views import APIView
from dotenv import load_dotenv
from forms_management.models import TaskModel, formularioTipoModel
from forms_management.serializers import formSerializer, taskSerializer
from email.message import EmailMessage
import ssl
import smtplib


class TaskView(APIView):

    def post(self, request):

        serializer = taskSerializer(data=request.data)

        if serializer.is_valid():

            task = serializer.save()
            load_dotenv()
            email_sender = "cristianalg740@gmail.com"
            password = os.getenv("PASSWORD")
            body = f"https://pelletlike-primely-shalanda.ngrok-free.dev/form/step1/?idLead={task.leadId}"
            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = task.email
            em["Subject"] = "Paso 1: Registro inicial"
            em.set_content(body)

            context = ssl._create_unverified_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.send_message(em)

            data = {
                "projecttask": task.taskId,
                "startdate": task.formDate,
                "email": task.email

            }

            return Response({"success": True, "data": data}, status=status.HTTP_200_OK)


        else:
            errores = []
            for error in serializer.errors.values():
                for e in error:
                    errores.append(e)

        return Response({"success": False, "errors": errores}, status=status.HTTP_400_BAD_REQUEST)


class getAllTasks(APIView):

    def get(self, request):
        tasks = list(TaskModel.objects.all().values())

        return Response({
            "success": True,
            "data": tasks
        }, status=status.HTTP_200_OK)






class TaskViewActualizarDatos(APIView):

    def post(self, request):
        queryTaskId = request.data.get('idTask')
        queryStatus = request.data.get('status')

        taskQueryObject = TaskModel.objects.filter(taskId=queryTaskId)
        taskObject = TaskModel.objects.filter(taskId=queryTaskId).first()
        load_dotenv()

        email_sender = "cristianalg740@gmail.com"
        password = os.getenv("PASSWORD")

        if queryStatus == "Form 1 completed":
            body = f"https://pelletlike-primely-shalanda.ngrok-free.dev/form/step2/?idLead={taskObject.leadId}"
            em = EmailMessage()
            email_receiver = taskObject.email
            em["From"] = email_sender
            em["To"] = email_receiver
            em["Subject"] = "Completa el formulario 2"
            em.set_content(body)
            context = ssl._create_unverified_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.send_message(em)

        if queryStatus == "Form 2 completed":
            body = f"https://pelletlike-primely-shalanda.ngrok-free.dev/form/step3/?idLead={taskObject.leadId}"
            em = EmailMessage()
            email_receiver = taskObject.email
            em["From"] = email_sender
            em["To"] = email_receiver
            em["Subject"] = "Completa el formulario 3"
            em.set_content(body)
            context = ssl._create_unverified_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, password)
                smtp.send_message(em)

        if taskQueryObject.exists() and queryStatus and queryTaskId:
            taskQueryObject.update(status=queryStatus)
            task = taskQueryObject.first()
            task.save()

            data = {
                "status": task.status,
                "taskId": task.taskId,
                "leadId": task.leadId,
                "taskDate": task.formDate,
                "message": "taskUpdatedSuccessfully"
            }
            return Response({"success": True, "data": data}, status=status.HTTP_200_OK)

        else:
            return Response({"success": False}, status=status.HTTP_400_BAD_REQUEST)
