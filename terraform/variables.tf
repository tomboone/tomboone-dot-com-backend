variable "service_plan_name" {
  type = string
  description = "Name of the existing app service plan to use"
}

variable "service_plan_rg_name" {
  type = string
  description = "Resource group for the existing app service plan"
}

variable "mysql_flexible_server_name" {
  type = string
  description = "Name of the exising MySQL flexible server to use"
}

variable "mysql_flexible_server_rg_name" {
  type = string
  description = "Resource group for the existing MySQL flexible server"
}

variable "log_analytics_workspace_name" {
  type = string
  description = "Name of the existing log analytics workspace to use"
}

variable "log_analytics_workspace_rg_name" {
  type = string
  description = "Resource group for the existing log analytics workspace"
}

variable "mysql_admin_username" {
  type = string
  description = "Admin username for the existing MySQL flexible server"
}

variable "mysql_admin_password" {
  type = string
  description = "Admin password for the existing MySQL flexible server"
  sensitive = true
}

variable "api_app_tenant_id" {
  type = string
  description = "Tenant ID for the system assigned managed identity of the app service"
}

variable "api_app_client_id" {
  type = string
  description = "Client ID for the system assigned managed identity of the app service"
}

variable "front_end_url" {
  type = string
  description = "The custom domain production URL of the front end"
}

variable "azure_front_end_url" {
  type = string
  description = "The Azure-assigned production URL of the front end"
}
