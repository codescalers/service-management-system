from django.contrib import admin
from .models import *
from django.apps import apps

class BaseAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'updated_at',)
    readonly_fields = ('created_at', 'updated_at',)

class EnvironmentVariableAdmin(BaseAdmin):
    list_display = ('name', 'value')

class ConfigurationFileAdmin(BaseAdmin):
    list_display = ('file_path', 'description')

class DependencyAdmin(BaseAdmin):
    list_display = ('name', 'version')

class NetworkConfigurationAdmin(BaseAdmin):
    list_display = ('dns', 'gateway', 'subnet')

class ApplicationAdmin(BaseAdmin):
    list_display = ('name', 'version', 'description')

class PortAdmin(BaseAdmin):
    list_display = ('application', 'port_number', 'protocol')

class LoggingConfigurationAdmin(BaseAdmin):
    list_display = ('log_file_path', 'log_level')

class MonitoringToolAdmin(BaseAdmin):
    list_display = ('name', 'version')

class HealthCheckAdmin(BaseAdmin):
    list_display = ('endpoint', 'criteria')

class ContainerizationAdmin(BaseAdmin):
    list_display = ('container_runtime', 'orchestration_tool', 'image_info')

class DeploymentToolAdmin(BaseAdmin):
    list_display = ('name', 'version', 'info')

class ScalingConfigurationAdmin(BaseAdmin):
    list_display = ('scaling_policy', 'auto_scaling_trigger')

class BackupConfigurationAdmin(BaseAdmin):
    list_display = ('backup_schedule', 'backup_location')

class UserPermissionAdmin(BaseAdmin):
    list_display = ('user', 'permissions')

class DisasterRecoveryAdmin(BaseAdmin):
    list_display = ('recovery_plan', 'backup_locations', 'testing_schedule')

class RunbookAdmin(BaseAdmin):
    list_display = ('run_command', 'verify_command', 'upgrade_command', 'rollback_command')

class BaseInline(admin.StackedInline):
    extra = 1

class EnvironmentVariableInline(BaseInline):
    model = EnvironmentVariable

class ConfigurationFileInline(BaseInline):
    model = ConfigurationFile

class DependencyInline(BaseInline):
    model = Dependency

class NetworkConfigurationInline(BaseInline):
    model = NetworkConfiguration

class ApplicationInline(BaseInline):
    model = Application

class PortInline(BaseInline):
    model = Port

class LoggingConfigurationInline(BaseInline):
    model = LoggingConfiguration

class MonitoringToolInline(BaseInline):
    model = MonitoringTool

class HealthCheckInline(BaseInline):
    model = HealthCheck

class ContainerizationInline(BaseInline):
    model = Containerization

class DeploymentToolInline(BaseInline):
    model = DeploymentTool

class ScalingConfigurationInline(BaseInline):
    model = ScalingConfiguration

class BackupConfigurationInline(BaseInline):
    model = BackupConfiguration

class UserPermissionInline(BaseInline):
    model = UserPermission

class DisasterRecoveryInline(BaseInline):
    model = DisasterRecovery

class RunbookInline(BaseInline):
    model = Runbook

models = apps.get_app_config('sms').get_models()
# register all models except for ServiceSystem
for model in models:
    if model.__name__ != "ServiceSystem":
        admin.site.register(model)

class ServiceSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'hostname', 'ip_address', 'operating_system', 'created_at', 'updated_at')
    search_fields = ('name', 'location', 'hostname', 'ip_address', 'operating_system')
    inlines = [EnvironmentVariableInline, ConfigurationFileInline, DependencyInline, NetworkConfigurationInline, ApplicationInline, PortInline, LoggingConfigurationInline, MonitoringToolInline, HealthCheckInline, ContainerizationInline, DeploymentToolInline, ScalingConfigurationInline, BackupConfigurationInline, UserPermissionInline, DisasterRecoveryInline, RunbookInline]

admin.site.register(ServiceSystem, ServiceSystemAdmin)