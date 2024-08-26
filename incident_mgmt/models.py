from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides created_at and updated_at fields.

    Attributes:
        created_at (DateTimeField): The date and time the model was created.
        updated_at (DateTimeField): The date and time the model was last updated.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta options for the model.

        Attributes:
            abstract (bool): Whether the model is abstract.
        """

        abstract = True


class IncidentDetails(TimeStampedModel):
    """
    Model for storing incident details.

    Attributes:
        name (CharField): The name of the incident.
        description (TextField): A description of the incident.
        date_time (DateTimeField): The date and time of the incident.
        type (CharField): The type of incident.
        severity_level (CharField): The severity level of the incident.
        status (CharField): The status of the incident.
        affected_systems (TextField): The systems affected by the incident.
        investigations (TextField): The investigations conducted for the incident.
        adjustments (TextField): The adjustments made as a result of the incident.
        followup_action (TextField): The follow-up actions taken for the incident.
        incident_summary (TextField): A summary of the incident.
        reported_by (CharField): The person who reported the incident.
    """

    class SeverityLevel(models.TextChoices):
        """
        Choices for the severity level of the incident.

        Attributes:
            LOW (str): Low severity.
            MEDIUM (str): Medium severity.
            HIGH (str): High severity.
            CRITICAL (str): Critical severity.
        """

        LOW = "Low"
        MEDIUM = "Medium"
        HIGH = "High"
        CRITICAL = "Critical"

    class IncidentStatus(models.TextChoices):
        """
        Choices for the status of the incident.

        Attributes:
            OPEN (str): Open status.
            INVESTIGATING (str): Investigating status.
            RESOLVED (str): Resolved status.
        """

        OPEN = "Open"
        INVESTIGATING = "Investigating"
        RESOLVED = "Resolved"

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    date_time = models.DateTimeField()
    type = models.CharField(max_length=255)
    severity_level = models.CharField(
        max_length=10, choices=SeverityLevel.choices, default=SeverityLevel.LOW
    )
    status = models.CharField(
        max_length=15, choices=IncidentStatus.choices, default=IncidentStatus.OPEN
    )
    affected_systems = models.TextField()
    investigations = models.TextField()
    adjustments = models.TextField()
    followup_action = models.TextField()
    incident_summary = models.TextField()
    reported_by = models.CharField(max_length=255)

    class Meta:
        """
        Meta options for the model.

        Attributes:
            verbose_name_plural (str): The plural name of the model.
        """

        verbose_name_plural = "Incident Details"

    def __str__(self):
        """
        Returns a string representation of the model.

        Returns:
            str: The name of the incident.
        """
        return f"{self.name}"


class IncidentTimeline(TimeStampedModel):
    """
    Model for storing incident timeline events.

    Attributes:
        incident_id (ForeignKey): The incident that the event belongs to.
        time (DateTimeField): The time of the event.
        event_description (TextField): A description of the event.
    """

    incident_id = models.ForeignKey(IncidentDetails, on_delete=models.CASCADE)
    time = models.DateTimeField()
    event_description = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the model.

        Returns:
            str: A string in the format "time - event_description".
        """
        return f"{self.time} - {self.event_description}"


class Attachment(TimeStampedModel):
    """
    Model for storing attachments.

    Attributes:
        incident_id (ForeignKey): The incident that the attachment belongs to.
        name (CharField): The name of the attachment.
        relevant_logs (TextField): Relevant logs for the attachment.
        file (FileField): The file attachment.
        additional_docs (TextField): Additional documentation for the attachment.
    """

    incident_id = models.ForeignKey(IncidentDetails, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    relevant_logs = models.TextField()
    file = models.FileField(upload_to="attachments/", blank=True, null=True)
    additional_docs = models.TextField(blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of the model.

        Returns:
            str: The name of the attachment.
        """
        return f"{self.name}"
