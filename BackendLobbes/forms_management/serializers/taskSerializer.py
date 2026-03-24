from rest_framework import serializers

from forms_management.models import TaskModel
from forms_management.models.taskModel import StepFormChoices, TaskModel


class taskSerializer(serializers.ModelSerializer):

    formStep = serializers.ChoiceField(choices=StepFormChoices)
    email = serializers.CharField(required=True)
    taskId = serializers.CharField(required=True)
    formDate = serializers.CharField(required=True)
    leadId = serializers.CharField(required=False)

    def validate_form_step(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("El tipo de formulario tiene que tener un valor numérico")

        if int(value) < 1 or int(value) > 3:
            raise serializers.ValidationError("El tipo de formulario debe tener solo los valores (1,2,3)")

        return value


    class Meta:
        model = TaskModel

        fields = (
            "formStep", "email", "taskId", "formDate","leadId"
        )


    def create(self, validated_data):
        return TaskModel.objects.create(**validated_data)