import secrets

from django.db import models


class StepFormChoices(models.TextChoices):
    # Cada opción tiene:
    # PRIMER valor → lo que se guarda en la base de datos
    # SEGUNDO valor → lo que se muestra al usuario

    STEP1 = "1", "1"
    STEP2 = "2", "2"
    STEP3 = "3", "3"


class FormularioRespuestaModel(models.Model):
    # Relacionado con el lead del CRM
    lead_id = models.CharField(max_length=25, unique=False, blank=True, null=True)

    form_step = models.CharField(
        max_length=3,  # Longitud máxima del código del país
        choices=StepFormChoices.choices,  # Opciones definidas en TextChoices
        default=StepFormChoices.STEP1,  # Valor por defecto
        verbose_name="Step",
        help_text="(Cumpolsory)",
        null=True,
        blank=True
    )

    dataJson = models.JSONField()

    class Meta:

        db_table = 'forms'
        verbose_name = "Form_response"
        verbose_name_plural = "Forms_responses"



