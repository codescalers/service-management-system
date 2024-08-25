from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class IncidentDetails(TimeStampedModel):
    class SeverityLevel(models.TextChoices):
        LOW = 'Low'
        MEDIUM = 'Medium'
        HIGH = 'High'
        CRITICAL = 'Critical'

    class IncidentStatus(models.TextChoices):
        OPEN = 'Open'
        INVESTIGATING = 'Investigating'
        RESOLVED = 'Resolved'

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    date_time = models.DateTimeField()
    type = models.CharField(max_length=255)
    severity_level = models.CharField(max_length=10, choices=SeverityLevel.choices, default=SeverityLevel.LOW)
    status = models.CharField(max_length=15, choices=IncidentStatus.choices, default=IncidentStatus.OPEN)
    affected_systems = models.TextField()
    investigations = models.TextField()
    adjustments = models.TextField()
    followup_action = models.TextField()
    incident_summary = models.TextField()
    reported_by = models.CharField(max_length=255)
    
    class Meta:
        verbose_name_plural = "Incident Details"

    def __str__(self):
        return self.name

class IncidentTimeline(TimeStampedModel):
    incident_id = models.ForeignKey(IncidentDetails, on_delete=models.CASCADE)
    time = models.DateTimeField()
    event_description = models.TextField()
    
    def __str__(self):
        return f"{self.time} - {self.event_description}"

class Attachment(TimeStampedModel):
    incident_id = models.ForeignKey(IncidentDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    relevant_logs = models.TextField()
    file = models.FileField(upload_to='attachments/', blank=True, null=True)
    additional_docs = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
