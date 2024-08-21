from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ServiceSystem(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    hostname = models.CharField(max_length=255)
    ip_address = models.GenericIPAddressField()
    operating_system = models.CharField(max_length=255)
    cpu_allocation = models.CharField(max_length=255)
    ram_allocation = models.CharField(max_length=255)
    disk_allocation = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class BaseModel(TimeStampedModel):
    service_system = models.ForeignKey(ServiceSystem, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class EnvironmentVariable(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self) -> str:
        return self.name


class ConfigurationFile(BaseModel):
    file_path = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        return self.file_path


class Dependency(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Dependencies"

    def __str__(self) -> str:
        return self.name


class NetworkConfiguration(BaseModel):
    dns = models.CharField(max_length=255)
    gateway = models.CharField(max_length=255)
    subnet = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.dns


class Application(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Port(BaseModel):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    port_number = models.IntegerField(
        validators=[MinValueValidator(1024), MaxValueValidator(65535)]
    )
    protocol = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.application.name}: {self.protocol}/{self.port_number}"


class LoggingConfiguration(BaseModel):
    log_file_path = models.CharField(max_length=1024)
    log_level = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.log_file_path


class MonitoringTool(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class HealthCheck(BaseModel):
    endpoint = models.CharField(max_length=1024)
    criteria = models.TextField()

    def __str__(self) -> str:
        return self.endpoint


class Containerization(BaseModel):
    container_runtime = models.CharField(max_length=255)
    orchestration_tool = models.CharField(max_length=255)
    image_info = models.TextField()

    def __str__(self) -> str:
        return self.container_runtime


class DeploymentTool(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self) -> str:
        return self.name


class ScalingConfiguration(BaseModel):
    scaling_policy = models.TextField()
    auto_scaling_trigger = models.TextField()

    def __str__(self) -> str:
        return self.scaling_policy


class BackupConfiguration(BaseModel):
    backup_schedule = models.TextField()
    backup_location = models.CharField(max_length=1024)

    def __str__(self) -> str:
        return self.backup_location


class UserPermission(BaseModel):
    user = models.CharField(max_length=255)
    permissions = models.TextField()

    def __str__(self) -> str:
        return self.user


class DisasterRecovery(BaseModel):
    recovery_plan = models.TextField()
    backup_locations = models.TextField()
    testing_schedule = models.TextField()

    class Meta:
        verbose_name_plural = "DisasterRecoveries"

    def __str__(self) -> str:
        return self.recovery_plan


class Runbook(BaseModel):
    run_command = models.TextField()
    verify_command = models.TextField()
    upgrade_command = models.TextField()
    rollback_command = models.TextField()

    def __str__(self) -> str:
        return self.run_command
