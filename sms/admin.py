from django.contrib import admin

from .models import *


@admin.register(EnvironmentVariable)
class EnvironmentVariableAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'name', 'value', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'name', 'value')

@admin.register(ConfigurationFile)
class ConfigurationFileAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'file_path', 'description', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'file_path', 'description')

@admin.register(Dependency)
class DependencyAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'name', 'version', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'name', 'version')

@admin.register(NetworkConfiguration)
class NetworkConfigurationAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'dns', 'gateway', 'subnet', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'dns', 'gateway', 'subnet')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'name', 'version','description', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'name', 'version','description')

@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'application', 'port_number', 'protocol', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'application__name', 'port_number', 'protocol')

@admin.register(LoggingConfiguration)
class LoggingConfigurationAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'log_file_path', 'log_level', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'log_file_path', 'log_level')

@admin.register(MonitoringTool)
class MonitoringToolAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'name', 'version', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'name', 'version')

@admin.register(HealthCheck)
class HealthCheckAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'endpoint', 'criteria', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'endpoint', 'criteria')

@admin.register(Containerization)
class ContainerizationAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'container_runtime', 'orchestration_tool', 'image_info', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'container_runtime', 'orchestration_tool')

@admin.register(DeploymentTool)
class DeploymentToolAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'name', 'version', 'info', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'name', 'version', 'info')

@admin.register(ScalingConfiguration)
class ScalingConfigurationAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'scaling_policy', 'auto_scaling_trigger', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'scaling_policy', 'auto_scaling_trigger')

@admin.register(BackupConfiguration)
class BackupConfigurationAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'backup_schedule', 'backup_location', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'backup_schedule', 'backup_location')

@admin.register(UserPermission)
class UserPermissionAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'user', 'permissions', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'user', 'permissions')

@admin.register(DisasterRecovery)
class DisasterRecoveryAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'recovery_plan', 'backup_locations', 'testing_schedule', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'recovery_plan', 'backup_locations', 'testing_schedule')

@admin.register(Runbook)
class RunbookAdmin(admin.ModelAdmin):
  list_display = ('service_system', 'run_command', 'verify_command', 'upgrade_command', 'rollback_command', 'created_at', 'updated_at')
  search_fields = ('service_system__name', 'run_command', 'verify_command', 'upgrade_command', 'rollback_command')



class EnvironmentVariableInline(admin.StackedInline):
  model = EnvironmentVariable
  extra = 1
  
class ConfigurationFileInline(admin.StackedInline):
  model = ConfigurationFile
  extra = 1
  
class DependencyInline(admin.StackedInline):
  model = Dependency
  extra = 1
  
class NetworjConfiguartionInline(admin.StackedInline):
  model = NetworkConfiguration
  extra = 1

class ApplicationInline(admin.StackedInline):
  model = Application
  extra = 1
  
class PortInline(admin.StackedInline):
  model = Port
  extra = 1
  
class LoggingConfigurationInline(admin.StackedInline):
  model = LoggingConfiguration
  extra = 1
  
class MonitoringToolInline(admin.StackedInline):
  model = MonitoringTool
  extra = 1
  
class HealthCheckInline(admin.StackedInline):
  model = HealthCheck
  extra = 1
  
class ContainerizationInline(admin.StackedInline):
  model = Containerization
  extra = 1

class DeploymentToolInline(admin.StackedInline):
    model = DeploymentTool
    extra = 1

class ScalingConfigurationInline(admin.StackedInline):
  model = ScalingConfiguration
  extra = 1

class BackupConfigurationInline(admin.StackedInline):
  model = BackupConfiguration
  extra = 1

class UserPermissionInline(admin.StackedInline):
  model = UserPermission
  extra = 1

class DisasterRecoveryInline(admin.StackedInline):
  model = DisasterRecovery
  extra = 1

class RunbookInline(admin.StackedInline):
  model = Runbook
  extra = 1

@admin.register(ServiceSystem)
class ServiceSystemAdmin(admin.ModelAdmin):
  list_display = ('name', 'location', 'hostname', 'ip_address', 'operating_system', 'created_at', 'updated_at')
  search_fields = ('name', 'location', 'hostname', 'ip_address', 'operating_system')
  inlines = [EnvironmentVariableInline, ConfigurationFileInline, DependencyInline, NetworjConfiguartionInline, ApplicationInline, PortInline, LoggingConfigurationInline, MonitoringToolInline, HealthCheckInline, ContainerizationInline, DeploymentToolInline, ScalingConfigurationInline, BackupConfigurationInline, UserPermissionInline, DisasterRecoveryInline, RunbookInline]