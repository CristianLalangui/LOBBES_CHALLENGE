from django.contrib import admin

# Importamos UserAdmin, la clase base que nos permite personalizar la interfaz de administración

from forms_management.models import FormularioRespuestaModel


@admin.register(FormularioRespuestaModel)
class formTypeAdmin(admin.ModelAdmin):
    # ----------------------------

    list_display = ("lead_id", "form_step")

    search_fields = ("form_step",)

    readonly_fields = (   "lead_id",
        "form_step",
        "interest",
        "reschedule",
        "preferred_date",
        "proposed_time",
        "prefered_time",
        "comments",
        "confirmation",          ##Django solo permite personalizar y
        "preferred_channel",     ##hacer logica con los modelos del admin,                             ##si están en readonlyFields
        "notes",)                ## Si están en readOnlyFields

    def get_fields(self, request, obj=None):
        if obj is None:
            return ["lead_id", "form_step", "dataJson"]
        if obj.form_step == "1":
            return ["lead_id", "form_step","interest","reschedule","preferred_date"]
        elif obj.form_step == "2":
            return ["lead_id", "form_step","proposedTime","preferedTime","comments"]
        else:
            return ["lead_id", "form_step","confirmation","preferred_channel","notes"]

    def interest(self, obj):
        return obj.dataJson.get("interest")

    def reschedule(self, obj):
        return obj.dataJson.get("reschedule")

    def preferred_date(self, obj):
        return obj.dataJson.get("preferred_date")

    def proposed_time(self, obj):
        return obj.dataJson.get("proposedTime")

    def prefered_time(self, obj):
        return obj.dataJson.get("preferedTime")

    def comments(self, obj):
        return obj.dataJson.get("comments")

    def confirmation(self, obj):
        return obj.dataJson.get("confirmation")

    def preferred_channel(self, obj):
        return obj.dataJson.get("preferred_channel")

    def notes(self, obj):
        return obj.dataJson.get("notes")