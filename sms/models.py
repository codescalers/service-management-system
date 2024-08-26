from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class TimeStampedModel(models.Model):
    """
    Abstract base model that provides created_at and updated_at fields.

    Attributes:
        created_at (datetime): The date and time the model was created.
        updated_at (datetime): The date and time the model was last updated.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ServiceSystem(TimeStampedModel):
    """
    Model representing a service system.

    Attributes:
        name (str): The name of the service system.
        description (str): A description of the service system.
        location (str): The location of the service system.
        hostname (str): The hostname of the service system.
        ip_address (str): The IP address of the service system.
        operating_system (str): The operating system of the service system.
        cpu_allocation (str): The CPU allocation of the service system.
        ram_allocation (str): The RAM allocation of the service system.
        disk_allocation (str): The disk allocation of the service system.
    """

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
        """
        Returns a string representation of the service system.

        Returns:
            str: The name of the service system.
        """
        return str(self.name)


class BaseModel(TimeStampedModel):
    """
    Abstract base model that provides a foreign key to a ServiceSystem.

    Attributes:
        service_system (ServiceSystem): The service system associated with this model.
    """

    service_system = models.ForeignKey(ServiceSystem, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class EnvironmentVariable(BaseModel):
    """
    Model representing an environment variable.

    Attributes:
        name (str): The name of the environment variable.
        value (str): The value of the environment variable.
    """

    name = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the environment variable.

        Returns:
            str: The name of the environment variable.
        """
        return str(self.name)


class ConfigurationFile(BaseModel):
    """
    Model representing a configuration file.

    Attributes:
        file_path (str): The path to the configuration file.
        description (str): A description of the configuration file.
    """

    file_path = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the configuration file.

        Returns:
            str: The path to the configuration file.
        """
        return str(self.file_path)


class Dependency(BaseModel):
    """
    Model representing a dependency.

    Attributes:
        name (str): The name of the dependency.
        version (str): The version of the dependency.
    """

    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Dependencies"

    def __str__(self) -> str:
        """
        Returns a string representation of the dependency.

        Returns:
            str: The name of the dependency.
        """
        return str(self.name)


class NetworkConfiguration(BaseModel):
    """
    Model representing a network configuration.

    Attributes:
        dns (str): The DNS server.
        gateway (str): The gateway IP address.
        subnet (str): The subnet mask.
    """

    dns = models.CharField(max_length=255)
    gateway = models.CharField(max_length=255)
    subnet = models.CharField(max_length=255)

    def __str__(self) -> str:
        """
        Returns a string representation of the network configuration.

        Returns:
            str: The DNS server.
        """
        return str(self.dns)


class Application(BaseModel):
    """
    Model representing an application.

    Attributes:
        name (str): The name of the application.
        version (str): The version of the application.
        description (str): A description of the application.
    """

    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the application.

        Returns:
            str: The name of the application.
        """
        return str(self.name)


class Port(BaseModel):
    """
    Model representing a port.

    Attributes:
        application (Application): The application associated with this port.
        port_number (int): The port number.
        protocol (str): The protocol used by this port.
    """

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    port_number = models.IntegerField(
        validators=[MinValueValidator(1024), MaxValueValidator(65535)]
    )
    protocol = models.CharField(max_length=50)

    def __str__(self) -> str:
        """
        Returns a string representation of the port.

        Returns:
            str: A string in the format "application: protocol/port_number".
        """
        return f"{self.application.name}: {self.protocol}/{self.port_number}"


class LoggingConfiguration(BaseModel):
    """
    Model representing a logging configuration.

    Attributes:
        log_file_path (str): The path to the log file.
        log_level (str): The log level.
    """

    log_file_path = models.CharField(max_length=1024)
    log_level = models.CharField(max_length=50)

    def __str__(self) -> str:
        """
        Returns a string representation of the logging configuration.

        Returns:
            str: The path to the log file.
        """
        return str(self.log_file_path)


class MonitoringTool(BaseModel):
    """
    Model representing a monitoring tool.

    Attributes:
        name (str): The name of the monitoring tool.
        version (str): The version of the monitoring tool.
    """

    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=50)

    def __str__(self) -> str:
        """
        Returns a string representation of the monitoring tool.

        Returns:
            str: The name of the monitoring tool.
        """
        return str(self.name)


class HealthCheck(BaseModel):
    """
    Model representing a health check.

    Attributes:
        endpoint (str): The endpoint to check.
        criteria (str): The criteria to check.
    """

    endpoint = models.CharField(max_length=1024)
    criteria = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the health check.

        Returns:
            str: The endpoint to check.
        """
        return str(self.endpoint)


class Containerization(BaseModel):
    """
    Model representing a containerization configuration.

    Attributes:
        container_runtime (str): The container runtime.
        orchestration_tool (str): The orchestration tool.
        image_info (str): Information about the image.
    """

    container_runtime = models.CharField(max_length=255)
    orchestration_tool = models.CharField(max_length=255)
    image_info = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the containerization configuration.

        Returns:
            str: The container runtime.
        """
        return str(self.container_runtime)


class DeploymentTool(BaseModel):
    """
    Model representing a deployment tool.

    Attributes:
        name (str): The name of the deployment tool.
        version (str): The version of the deployment tool.
        info (str): Information about the deployment tool.
    """

    name = models.CharField(max_length=255, unique=True)
    version = models.CharField(max_length=50)
    info = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the deployment tool.

        Returns:
            str: The name of the deployment tool.
        """
        return str(self.name)


class ScalingConfiguration(BaseModel):
    """
    Model representing a scaling configuration.

    Attributes:
        scaling_policy (str): The scaling policy.
        auto_scaling_trigger (str): The auto scaling trigger.
    """

    scaling_policy = models.TextField()
    auto_scaling_trigger = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the scaling configuration.

        Returns:
            str: The scaling policy.
        """
        return str(self.scaling_policy)


class BackupConfiguration(BaseModel):
    """
    Model representing a backup configuration.

    Attributes:
        backup_schedule (str): The backup schedule.
        backup_location (str): The backup location.
    """

    backup_schedule = models.TextField()
    backup_location = models.CharField(max_length=1024)

    def __str__(self) -> str:
        """
        Returns a string representation of the backup configuration.

        Returns:
            str: The backup location.
        """
        return str(self.backup_location)


class UserPermission(BaseModel):
    """
    Model representing a user permission.

    Attributes:
        user (str): The user.
        permissions (str): The permissions.
    """

    user = models.CharField(max_length=255)
    permissions = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the user permission.

        Returns:
            str: The user.
        """
        return str(self.user)


class DisasterRecovery(BaseModel):
    """
    Model representing a disaster recovery plan.

    Attributes:
        recovery_plan (str): The recovery plan.
        backup_locations (str): The backup locations.
        testing_schedule (str): The testing schedule.
    """

    recovery_plan = models.TextField()
    backup_locations = models.TextField()
    testing_schedule = models.TextField()

    class Meta:
        """
        Meta class for DisasterRecovery model.

        Attributes:
            verbose_name_plural (str): The plural name of the model.
        """

        verbose_name_plural = "DisasterRecoveries"

    def __str__(self) -> str:
        """
        Returns a string representation of the disaster recovery plan.

        Returns:
            str: The recovery plan.
        """
        return str(self.recovery_plan)


class Runbook(BaseModel):
    """
    Model representing a runbook.

    Attributes:
        run_command (str): The run command.
        verify_command (str): The verify command.
        upgrade_command (str): The upgrade command.
        rollback_command (str): The rollback command.
    """

    run_command = models.TextField()
    verify_command = models.TextField()
    upgrade_command = models.TextField()
    rollback_command = models.TextField()

    def __str__(self) -> str:
        """
        Returns a string representation of the runbook.

        Returns:
            str: The run command.
        """
        return str(self.run_command)
