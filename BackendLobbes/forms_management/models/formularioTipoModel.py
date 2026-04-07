import secrets

from django.db import models


class StepFormChoices(models.TextChoices):


    STEP1 = "1", "1"
    STEP2 = "2", "2"
    STEP3 = "3", "3"


class FormularioRespuestaModel(models.Model):
    # Relacionado con el lead del CRM
    lead_id = models.CharField(max_length=25, unique=False, blank=True, null=True)

    form_step = models.CharField(
        max_length=3,
        choices=StepFormChoices.choices,
        default=StepFormChoices.STEP1,
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



