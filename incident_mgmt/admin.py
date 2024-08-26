from django.contrib import admin
from .models import *


class BaseAdmin(admin.ModelAdmin):
    """
    Base admin class that provides a common interface for all admin classes.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    def get_list_display(self, _):
        """
        Returns the list of fields to display in the admin interface.

        Args:
            _ (object): An unused object.

        Returns:
            list: The list of fields to display.
        """
        return self.list_display + ("created_at", "updated_at")


@admin.register(IncidentTimeline)
class IncidentTimelineAdmin(BaseAdmin):
    """
    Admin class for IncidentTimeline model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("time", "event_description")


@admin.register(Attachment)
class AttachmentAdmin(BaseAdmin):
    """
    Admin class for Attachment model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("name", "relevant_logs", "file", "additional_docs")


class IncidentTimelineInline(admin.StackedInline):
    """
    Admin inline class for IncidentTimeline model.

    Attributes:
        extra (int): The number of extra inlines to display.
        model (IncidentTimeline): The model to display.
    """

    extra = 1
    model = IncidentTimeline


class IncidentAttachmentsInline(admin.StackedInline):
    """
    Admin inline class for Attachment model.

    Attributes:
        extra (int): The number of extra inlines to display.
        model (Attachment): The model to display.
    """

    extra = 1
    model = Attachment


@admin.register(IncidentDetails)
class IncidentDetailsAdmin(BaseAdmin):
    """
    Admin class for IncidentDetails model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
        inlines (list): A list of admin inline classes to display.
    """

    list_display = (
        "name",
        "description",
        "date_time",
        "type",
        "severity_level",
        "status",
        "affected_systems",
        "investigations",
        "adjustments",
        "followup_action",
        "incident_summary",
        "reported_by",
    )
    inlines = [IncidentTimelineInline, IncidentAttachmentsInline]
