"""
"form_step": 1,
"lead_id": "123",
"response": {
"interested": true,
"reschedule": true,
"preferred_date": "2026-05-10"
"""

from rest_framework import serializers

from forms_management.models import  FormularioRespuestaModel
from forms_management.models.formularioTipoModel import StepFormChoices


class formSerializer(serializers.ModelSerializer):
    form_step = serializers.ChoiceField(choices=StepFormChoices.choices)
    lead_id = serializers.CharField(required=True)
    response = serializers.JSONField(source='dataJson')

    def validate_form_step(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("El tipo de formulario tiene que tener un valor numérico")

        if int(value) < 1 or int(value) > 3:
            raise serializers.ValidationError("El tipo de formulario debe tener solo los valores (1,2,3)")

        return  value
    class Meta:

        model = FormularioRespuestaModel

        fields = (
            "form_step", "lead_id", "response"
        )

    def create(self, validated_data):

        form = FormularioRespuestaModel.objects.create(

            lead_id = validated_data["lead_id"],
            form_step = validated_data["form_step"],
            dataJson = validated_data["dataJson"]

        )

        return form
