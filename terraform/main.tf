locals {
  service_name = "tomboone-dot-com-backend"
  short_name   = "tbcbackend"
  mysql_ca_cert_content = file("${path.module}/../certs/mysql-ca-bundle.pem")
}


# Existing app service plan
data "azurerm_service_plan" "existing" {
  name                = var.service_plan_name
  resource_group_name = var.service_plan_rg_name
}

# Existing MySQL flexible server
data "azurerm_mysql_flexible_server" "existing" {
  name                = var.mysql_flexible_server_name
  resource_group_name = var.mysql_flexible_server_rg_name
}

# Existing log analytics workspace
data "azurerm_log_analytics_workspace" "existing" {
  name                = var.log_analytics_workspace_name
  resource_group_name = var.log_analytics_workspace_rg_name
}

# VNet integration - reference existing VNet infrastructure
data "azurerm_virtual_network" "vnet" {
  name                = var.vnet_name
  resource_group_name = var.vnet_rg_name
}

data "azurerm_subnet" "integration" {
  name                 = "IntegrationSubnet"
  virtual_network_name = data.azurerm_virtual_network.vnet.name
  resource_group_name  = data.azurerm_virtual_network.vnet.resource_group_name
}

# Resource group
resource "azurerm_resource_group" "main" {
  name     = "${ local.service_name }-rg"
  location = data.azurerm_service_plan.existing.location
}

# MySQL database
resource "azurerm_mysql_flexible_database" "main" {
  name                = local.short_name
  resource_group_name = data.azurerm_mysql_flexible_server.existing.resource_group_name
  server_name         = data.azurerm_mysql_flexible_server.existing.name
  charset             = "utf8mb4"
  collation           = "utf8mb4_unicode_ci"
}

# MySQL password
resource "random_password" "mysql" {
  length  = 32
  special = false
}

# MySQL user
resource "mysql_user" "prod" {
  user               = "${local.short_name}_user"
  host               = "%"
  plaintext_password = random_password.mysql.result
}

# MySQL grants
resource "mysql_grant" "prod" {
  user       = mysql_user.prod.user
  host       = mysql_user.prod.host
  database   = azurerm_mysql_flexible_database.main.name
  privileges = ["ALL PRIVILEGES"]
}

# Application insights
resource "azurerm_application_insights" "main" {
  name                = "${local.service_name}-insights"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  application_type    = "web"
}

# Linux App Service
resource "azurerm_linux_web_app" "main" {
  name                = local.service_name
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  service_plan_id     = data.azurerm_service_plan.existing.id

  virtual_network_subnet_id = data.azurerm_subnet.integration.id
  https_only = true

  site_config {
    always_on = true
    app_command_line = "/home/site/wwwroot/.venv/bin/python -m alembic upgrade head && /home/site/wwwroot/.venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --port 8000"
    application_stack {
      python_version = "3.13"
    }
  }

  app_settings = {
    "SCM_DO_BUILD_DURING_DEPLOYMENT"        = "false"
    "MYSQL_SSL_CA_CONTENT"                  = local.mysql_ca_cert_content
    "DATABASE_URL"                          = "mysql+pymysql://${mysql_user.prod.user}:${random_password.mysql.result}@${data.azurerm_mysql_flexible_server.existing.fqdn}:3306/${azurerm_mysql_flexible_database.main.name}?charset=${azurerm_mysql_flexible_database.main.charset}&ssl_disabled=false&ssl_verify_cert=false&ssl_verify_identity=false"
    "APPLICATIONINSIGHTS_CONNECTION_STRING" = azurerm_application_insights.main.connection_string
  }
}
