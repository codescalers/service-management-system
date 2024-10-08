from django.contrib import admin

from .models import *


class BaseAdmin(admin.ModelAdmin):
    def get_list_display(self, _):
        return self.list_display + ("service_system", "created_at", "updated_at")


@admin.register(EnvironmentVariable)
class EnvironmentVariableAdmin(BaseAdmin):
    list_display = ("name", "value")


@admin.register(ConfigurationFile)
class ConfigurationFileAdmin(BaseAdmin):
    list_display = ("file_path", "description")


@admin.register(Dependency)
class DependencyAdmin(BaseAdmin):
    list_display = ("name", "version")


@admin.register(NetworkConfiguration)
class NetworkConfigurationAdmin(BaseAdmin):
    list_display = ("dns", "gateway", "subnet")


@admin.register(Application)
class ApplicationAdmin(BaseAdmin):
    list_display = ("name", "version", "description")


@admin.register(Port)
class PortAdmin(BaseAdmin):
    list_display = ("application", "port_number", "protocol")


@admin.register(LoggingConfiguration)
class LoggingConfigurationAdmin(BaseAdmin):
    list_display = ("log_file_path", "log_level")


@admin.register(MonitoringTool)
class MonitoringToolAdmin(BaseAdmin):
    list_display = ("name", "version")


@admin.register(HealthCheck)
class HealthCheckAdmin(BaseAdmin):
    list_display = ("endpoint", "criteria")


@admin.register(Containerization)
class ContainerizationAdmin(BaseAdmin):
    list_display = ("container_runtime", "orchestration_tool", "image_info")


@admin.register(DeploymentTool)
class DeploymentToolAdmin(BaseAdmin):
    list_display = ("name", "version", "info")


@admin.register(ScalingConfiguration)
class ScalingConfigurationAdmin(BaseAdmin):
    list_display = ("scaling_policy", "auto_scaling_trigger")


@admin.register(BackupConfiguration)
class BackupConfigurationAdmin(BaseAdmin):
    list_display = ("backup_schedule", "backup_location")


@admin.register(UserPermission)
class UserPermissionAdmin(BaseAdmin):
    list_display = ("user", "permissions")


@admin.register(DisasterRecovery)
class DisasterRecoveryAdmin(BaseAdmin):
    list_display = ("recovery_plan", "backup_locations", "testing_schedule")


@admin.register(Runbook)
class RunbookAdmin(BaseAdmin):
    list_display = (
        "run_command",
        "verify_command",
        "upgrade_command",
        "rollback_command",
    )


class BaseAdminInline(admin.StackedInline):
    extra = 1


class EnvironmentVariableInline(BaseAdminInline):
    model = EnvironmentVariable


class ConfigurationFileInline(BaseAdminInline):
    model = ConfigurationFile


class DependencyInline(BaseAdminInline):
    model = Dependency


class NetworjConfiguartionInline(BaseAdminInline):
    model = NetworkConfiguration


class ApplicationInline(BaseAdminInline):
    model = Application


class PortInline(BaseAdminInline):
    model = Port


class LoggingConfigurationInline(BaseAdminInline):
    model = LoggingConfiguration


class MonitoringToolInline(BaseAdminInline):
    model = MonitoringTool


class HealthCheckInline(BaseAdminInline):
    model = HealthCheck


class ContainerizationInline(BaseAdminInline):
    model = Containerization


class DeploymentToolInline(BaseAdminInline):
    model = DeploymentTool


class ScalingConfigurationInline(BaseAdminInline):
    model = ScalingConfiguration


class BackupConfigurationInline(BaseAdminInline):
    model = BackupConfiguration


class UserPermissionInline(BaseAdminInline):
    model = UserPermission


class DisasterRecoveryInline(BaseAdminInline):
    model = DisasterRecovery


class RunbookInline(BaseAdminInline):
    model = Runbook


@admin.register(ServiceSystem)
class ServiceSystemAdmin(admin.ModelAdmin):
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
