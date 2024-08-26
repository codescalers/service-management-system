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
        return self.list_display + ("service_system", "created_at", "updated_at")


@admin.register(EnvironmentVariable)
class EnvironmentVariableAdmin(BaseAdmin):
    """
    Admin class for EnvironmentVariable model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("name", "value")


@admin.register(ConfigurationFile)
class ConfigurationFileAdmin(BaseAdmin):
    """
    Admin class for ConfigurationFile model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("file_path", "description")


@admin.register(Dependency)
class DependencyAdmin(BaseAdmin):
    """
    Admin class for Dependency model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("name", "version")


@admin.register(NetworkConfiguration)
class NetworkConfigurationAdmin(BaseAdmin):
    """
    Admin class for NetworkConfiguration model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("dns", "gateway", "subnet")


@admin.register(Application)
class ApplicationAdmin(BaseAdmin):
    """
    Admin class for Application model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("name", "version", "description")


@admin.register(Port)
class PortAdmin(BaseAdmin):
    """
    Admin class for Port model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("application", "port_number", "protocol")


@admin.register(LoggingConfiguration)
class LoggingConfigurationAdmin(BaseAdmin):
    """
    Admin class for LoggingConfiguration model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("log_file_path", "log_level")


@admin.register(MonitoringTool)
class MonitoringToolAdmin(BaseAdmin):
    """
    Admin class for MonitoringTool model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("name", "version")


@admin.register(HealthCheck)
class HealthCheckAdmin(BaseAdmin):
    """
    Admin class for HealthCheck model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("endpoint", "criteria")


@admin.register(Containerization)
class ContainerizationAdmin(BaseAdmin):
    """
    Admin class for Containerization model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("container_runtime", "orchestration_tool", "image_info")


@admin.register(DeploymentTool)
class DeploymentToolAdmin(BaseAdmin):
    """
    Admin class for DeploymentTool model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("name", "version", "info")


@admin.register(ScalingConfiguration)
class ScalingConfigurationAdmin(BaseAdmin):
    """
    Admin class for ScalingConfiguration model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("scaling_policy", "auto_scaling_trigger")


@admin.register(BackupConfiguration)
class BackupConfigurationAdmin(BaseAdmin):
    """
    Admin class for BackupConfiguration model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("backup_schedule", "backup_location")


@admin.register(UserPermission)
class UserPermissionAdmin(BaseAdmin):
    """
    Admin class for UserPermission model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("user", "permissions")


@admin.register(DisasterRecovery)
class DisasterRecoveryAdmin(BaseAdmin):
    """
    Admin class for DisasterRecovery model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = ("recovery_plan", "backup_locations", "testing_schedule")


@admin.register(Runbook)
class RunbookAdmin(BaseAdmin):
    """
    Admin class for Runbook model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
    """

    list_display = (
        "run_command",
        "verify_command",
        "upgrade_command",
        "rollback_command",
    )


class BaseAdminInline(admin.StackedInline):
    """
    Base admin inline class that provides a common interface for all admin inline classes.

    Attributes:
        extra (int): The number of extra inlines to display.
    """

    extra = 1


class EnvironmentVariableInline(BaseAdminInline):
    """
    Admin inline class for EnvironmentVariable model.

    Attributes:
        model (EnvironmentVariable): The model to display.
    """

    model = EnvironmentVariable


class ConfigurationFileInline(BaseAdminInline):
    """
    Admin inline class for ConfigurationFile model.

    Attributes:
        model (ConfigurationFile): The model to display.
    """

    model = ConfigurationFile


class DependencyInline(BaseAdminInline):
    """
    Admin inline class for Dependency model.

    Attributes:
        model (Dependency): The model to display.
    """

    model = Dependency


class NetworjConfiguartionInline(BaseAdminInline):
    """
    Admin inline class for NetworkConfiguration model.

    Attributes:
        model (NetworkConfiguration): The model to display.
    """

    model = NetworkConfiguration


class ApplicationInline(BaseAdminInline):
    """
    Admin inline class for Application model.

    Attributes:
        model (Application): The model to display.
    """

    model = Application


class PortInline(BaseAdminInline):
    """
    Admin inline class for Port model.

    Attributes:
        model (Port): The model to display.
    """

    model = Port


class LoggingConfigurationInline(BaseAdminInline):
    """
    Admin inline class for LoggingConfiguration model.

    Attributes:
        model (LoggingConfiguration): The model to display.
    """

    model = LoggingConfiguration


class MonitoringToolInline(BaseAdminInline):
    """
    Admin inline class for MonitoringTool model.

    Attributes:
        model (MonitoringTool): The model to display.
    """

    model = MonitoringTool


class HealthCheckInline(BaseAdminInline):
    """
    Admin inline class for HealthCheck model.

    Attributes:
        model (HealthCheck): The model to display.
    """

    model = HealthCheck


class ContainerizationInline(BaseAdminInline):
    """
    Admin inline class for Containerization model.

    Attributes:
        model (Containerization): The model to display.
    """

    model = Containerization


class DeploymentToolInline(BaseAdminInline):
    """
    Admin inline class for DeploymentTool model.

    Attributes:
        model (DeploymentTool): The model to display.
    """

    model = DeploymentTool


class ScalingConfigurationInline(BaseAdminInline):
    """
    Admin inline class for ScalingConfiguration model.

    Attributes:
        model (ScalingConfiguration): The model to display.
    """

    model = ScalingConfiguration


class BackupConfigurationInline(BaseAdminInline):
    """
    Admin inline class for BackupConfiguration model.

    Attributes:
        model (BackupConfiguration): The model to display.
    """

    model = BackupConfiguration


class UserPermissionInline(BaseAdminInline):
    """
    Admin inline class for UserPermission model.

    Attributes:
        model (UserPermission): The model to display.
    """

    model = UserPermission


class DisasterRecoveryInline(BaseAdminInline):
    """
    Admin inline class for DisasterRecovery model.

    Attributes:
        model (DisasterRecovery): The model to display.
    """

    model = DisasterRecovery


class RunbookInline(BaseAdminInline):
    """
    Admin inline class for Runbook model.

    Attributes:
        model (Runbook): The model to display.
    """

    model = Runbook


@admin.register(ServiceSystem)
class ServiceSystemAdmin(admin.ModelAdmin):
    """
    Admin class for ServiceSystem model.

    Attributes:
        list_display (list): A list of fields to display in the admin interface.
        search_fields (list): A list of fields to search in the admin interface.
        inlines (list): A list of admin inline classes to display.
    """

    list_display = (
        "name",
        "location",
        "hostname",
        "ip_address",
        "operating_system",
        "created_at",
        "updated_at",
    )
    search_fields = ("name", "location", "hostname", "ip_address", "operating_system")
    inlines = [
        EnvironmentVariableInline,
        ConfigurationFileInline,
        DependencyInline,
        NetworjConfiguartionInline,
        ApplicationInline,
        PortInline,
        LoggingConfigurationInline,
        MonitoringToolInline,
        HealthCheckInline,
        ContainerizationInline,
        DeploymentToolInline,
        ScalingConfigurationInline,
        BackupConfigurationInline,
        UserPermissionInline,
        DisasterRecoveryInline,
        RunbookInline,
    ]
