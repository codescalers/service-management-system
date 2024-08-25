from django.contrib import admin
from .models import *

class BaseAdmin(admin.ModelAdmin):
    def get_list_display(self, _):
      return self.list_display + ("created_at", "updated_at")

@admin.register(IncidentTimeline)
class IncidentTimelineAdmin(BaseAdmin):
    list_display = ("time", "event_description")
  
@admin.register(Attachment)
class AttachmentAdmin(BaseAdmin):
    list_display = ("name", "relevant_logs", "file", "additional_docs")
  
class IncidentTimelineInline(admin.StackedInline):
    extra = 1
    model = IncidentTimeline
    
    
class IncidentAttachmentsInline(admin.StackedInline):
    extra = 1
    model = Attachment


@admin.register(IncidentDetails)
class IncidentDetailsAdmin(BaseAdmin):
    list_display = ("name", "description", "date_time", "type", "severity_level", "status", "affected_systems", "investigations", "adjustments", "followup_action", "incident_summary", "reported_by")
    inlines = [IncidentTimelineInline, IncidentAttachmentsInline]

    
