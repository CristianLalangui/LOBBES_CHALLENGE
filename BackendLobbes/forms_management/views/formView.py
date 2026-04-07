import requests
from django.shortcuts import render
from rest_framework import status
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from forms_management.models import FormularioRespuestaModel,TaskModel
from forms_management.serializers import formSerializer, taskSerializer

from forms_management.models import TaskModel


class FormView1(APIView):


    def get(self, request):
        queryIdlead = request.GET.get('idLead')

        return render(request, 'form1.html', {'idLead': queryIdlead})

    def post(self, request):
        lead_id = request.POST.get('idLead')

        TaskObject = TaskModel.objects.filter(leadId=lead_id).first()

        data = {
            "form_step": "1",
            "lead_id": lead_id,
            "response": {
                "interest": request.POST.get('interest'),
                "reschedule": request.POST.get('reschedule'),
                "preferred_date": request.POST.get('date')
            }
        }

        serializer = formSerializer(data=data)


        if serializer.is_valid():
            serializer.save()

            n8n_url = f"https://n8n.mpforall.com/webhook-test/confirm-form"

            payload = {
                "form_step": "1",
                "lead_id": lead_id,
                "task_id":TaskObject.taskId,
                "response": {
                    "interest": request.POST.get('interest'),
                    "reschedule": request.POST.get('reschedule'),
                    "preferred_date": request.POST.get('date')
                }
            }

            requests.post(n8n_url, json=payload, timeout=5,verify=True)

            return Response({"success": True, "message": "Datos enviados a n8n"}, status=status.HTTP_200_OK)

        errores = []
        for error_list in serializer.errors.values():
            for e in error_list:
                errores.append(e)

        return Response({
            "success": False,

            "errors": serializer.errors,
            "data_sent": data
        }, status=status.HTTP_400_BAD_REQUEST)


class FormView2(APIView):



    def get(self, request):
        queryIdlead = request.GET.get('idLead')
        return render(request, 'form2.html', {'idLead': queryIdlead})

    def post(self, request):
        lead_id = request.POST.get('idLead')


        TaskObject = TaskModel.objects.filter(leadId=lead_id).first()
        data = {
            "form_step": "2",
            "lead_id": request.POST.get('idLead'),
            "response": {
                "proposedTime": request.POST.get('proposedTime'),
                "preferedTime": request.POST.get('preferedTime'),
                "comments": request.POST.get('comments')
            }
        }

        serializer = formSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            n8n_url = f"https://n8n.mpforall.com/webhook-test/confirm-form2"

            payload = {
                "form_step": "2",
                "lead_id": lead_id,
                "task_id": TaskObject.taskId,
                "response": {
                    "proposedTime": request.POST.get('proposedTime'),
                    "preferedTime": request.POST.get('preferedTime'),
                    "comments": request.POST.get('comments')
                }
            }


            requests.post(n8n_url, json=payload, timeout=5, verify=True)

            return Response({"success": True}, status=status.HTTP_200_OK)

        else:
            errores = []
            for error in serializer.errors.values():
                for e in error:
                    errores.append(e)

        return Response({"success": False, "errors": errores}, status=status.HTTP_400_BAD_REQUEST)


class FormView3(APIView):

    def get(self, request):
        queryIdlead = request.GET.get('idLead')
        return render(request, 'form3.html', {'idLead': queryIdlead})

    def post(self, request):
        lead_id = request.POST.get('idLead')

        TaskObject = TaskModel.objects.filter(leadId=lead_id).first()
        data = {

            "form_step": "3",
            "lead_id": request.POST.get('idLead'),
            "response": {
                "confirmation": request.POST.get('confirmation'),
                "preferredChannel": request.POST.get('preferredChannel'),
                "notes": request.POST.get('notes')
            }
        }

        serializer = formSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            n8n_url = f"https://n8n.mpforall.com/webhook-test/confirm-form3"

            payload = {
                "form_step": "3 ",
                "lead_id": lead_id,
                "task_id": TaskObject.taskId,
                "response": {
                    "confirmation": request.POST.get('confirmation'),
                    "preferredChannel": request.POST.get('preferredChannel'),
                    "notes": request.POST.get('notes')
                }
            }


            requests.post(n8n_url, json=payload, timeout=5, verify=True)

            return Response({"success": True}, status=status.HTTP_200_OK)

        else:
            errores = []
            for error in serializer.errors.values():
                for e in error:
                    errores.append(e)

        return Response({"success": False, "errors": errores}, status=status.HTTP_400_BAD_REQUEST)
