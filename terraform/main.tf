# DigiCert Global Root G2 certificate
data "http" "digicert_global_root_g2" {
  url = "https://cacerts.digicert.com/DigiCertGlobalRootG2.crt.pem"
}

locals {
  service_name = "tomboone-dot-com-backend"
  short_name   = "tbcbackend"
  microsoft_rsa_root_2017_pem = <<-EOT
-----BEGIN CERTIFICATE-----
MIIFqDCCA5CgAwIBAgIQHtOXCX95q3YKHD0uKsEafjANBgkqhkiG9w0BAQwFADBl
MQswCQYDVQQGEwJVUzEeMBwGA1UEChMVTWljcm9zb2Z0IENvcnBvcmF0aW9uMTYw
NAYDVQQDEy1NaWNyb3NvZnQgUlNBIFJvb3QgQ2VydGlmaWNhdGUgQXV0aG9yaXR5
IDIwMTcwHhcNMTkxMjE4MjI1MTIyWhcNNDIwNzE4MjMwMDIzWjBlMQswCQYDVQQG
EwJVUzEeMBwGA1UEChMVTWljcm9zb2Z0IENvcnBvcmF0aW9uMTYwNAYDVQQDEy1N
aWNyb3NvZnQgUlNBIFJvb3QgQ2VydGlmaWNhdGUgQXV0aG9yaXR5IDIwMTcwggIi
MA0GCSqGSIb3DQEBAQUAA4ICDwAwggIKAoICAQDKW765Q4wpqZEWCpW9R2LBiftJ
Nt9GkMml7XhqkyfERLTEaLgfJYNGCpqFvuA+UDJ2gcQgVC8BAl11nEhAglMQvL/H
O2iQtqQi5fZAWbAzbMjSXZ+7rCJqQs1WdMRZE4+ZdOPIBqo54WmD9GdO2GdxOQNH
9DCHgIBaoBNWxZDRnK7rJ2bwlwpVmlA8J4iCwgMeqLdqCFOZIXRUIVjJWB4rJJ8l
CnkJmxNdIJGRhOsj6XaGkYu4Qb0pFjzP+5oIWUxBm5VRWUXqL0WPUzE5gj3LJjjY
1u9xt4r5nU5I9D4J4DqZpyX9nPYcBOhUdEsA4QXcb5bhQ7sHV3NJvQXqLrU6mGPJ
qMqPHGYlPGFJcggAy0G5VYhJpQdSJCQ0HHOY2EEsX2yTRjfhWNj5mVYqYFJlhMX9
8bKDIKEhDlrGVGZNhMPWkJDG3rJqbfCEaAhsFAOLYaZuJNIUZ6eX8zXJ1jfUEHGH
5lh6CzlYE1OhCmF0zGBzKLKdEhF4LqAgtJOmvhYIe6cKRnWKqJRpF9NKgc7p5M9G
r4KWBcP1C1q1HmvAzXzlJhUFfWGQZPnr1q2h0V7VW+LNTaE6XPbDJ6mRCCCKJHIc
r4rCi8OsU5l+pPZhzLGP9LhaBXLnGNhIh5YaCZJCwXxPjUJJ0GNfDK6kBPSLsEEv
M7gK+G3JTmtDRVl4wIDAQABo1QwUjAOBgNVHQ8BAf8EBAMCAYYwDwYDVR0TAQH/
BAUwAwEB/zAdBgNVHQ4EFgQUCcxZb4aycI8aw5D4pv+7TbIjMBAwCgYJKoBILxUB
BAMCATANBgkqhkiG9w0BAQwFAAOCAgEAjKsecR5hKI6jcP+5fxU7PjHRKqalCOe4
8H2Zb4Zm71ue3peTNrQ+W3e3lXMGm/CJ5e5JTsBDzDBvXSNjHl91EZCqPmvGCjQ2
3Rnr/Nq/wTN7WJTgC3kO+UYsGF1oZDy+LJJ5gmdFXQaD3lGbwOKZLUg1gWdMDbF0
1T7Lz7KEu3kJgZFWAmEQ2LT7Qmp0xFIYDtGZdYHbH3MdW5Vy7fGZ9rT7LfR6hZFC
Oy0gB9/fT+q/9NeEK6TlG9MgOzQhkwEZPG5w/QJQ5FQD8FBL5SU5UYYBuPb7Q9k1
kH0f1fEfJ3d4mT0m4vUnfKJcT9OJN1A+WLH5Lzn/5k5GZ5YmLiU1kWdJnYVlCJTz
g4G8BmG/k+d7QOJFbPFKOmTKJYd1mB4JmXNMfk8XlKU1b5TJC4wSPq8aKNbNPIYS
IOJ2r4FwJDOZNqYCDw0QKTtcwYIzD7g8Y5JDjNqVNfUqQPDa9g9UWgdFwg3qD1f1
2P5W4hb5g9LW8aNmDBUhY4AcJdFmQoD8B5PZ2y0DH4m6DLB+/bP10eQMnFLFO5F2
MpTNO7HAgS3XYJGGdGZeQV/4JHhJXqT1kJnJgR3eU6f3OfyeHqzHKQPNiJHjG9kn
RGGM5KkxENKe8kM6THEWx/T1JZkgxTDMXb1y8zlHe1rZzFPfJnRCJ7aTNOZJFKj1
g1M4J3JyJsQ=
-----END CERTIFICATE-----
EOT

  # Combine both PEM certificates
  mysql_ca_cert_content = "${data.http.digicert_global_root_g2.response_body}${local.microsoft_rsa_root_2017_pem}"
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

  identity {
    type = "SystemAssigned"
  }

  site_config {
    always_on = true
    app_command_line = "python -m alembic upgrade head && python -m uvicorn app.main:app --host 0.0.0.0 --port 8000"
    cors {
      allowed_origins = [
        var.front_end_url,
        var.azure_front_end_url
      ]
    }
    http2_enabled = true
    minimum_tls_version = "1.2"
    application_stack {
      python_version = "3.12"
    }
  }

  app_settings = {
    "AZURE_TENANT_ID"                       = var.api_app_tenant_id
    "AZURE_CLIENT_ID"                       = var.api_app_client_id
    "OPENAPI_CLIENT_ID"                     = var.openapi_client_id
    "MYSQL_SSL_CA_CONTENT"                  = local.mysql_ca_cert_content
    "DATABASE_URL"                          = "mysql+pymysql://${mysql_user.prod.user}:${mysql_user.prod.plaintext_password}@${data.azurerm_mysql_flexible_server.existing.fqdn}:3306/${azurerm_mysql_flexible_database.main.name}?charset=${azurerm_mysql_flexible_database.main.charset}&ssl_disabled=false&ssl_verify_cert=false&ssl_verify_identity=false"
    "APPLICATIONINSIGHTS_CONNECTION_STRING" = azurerm_application_insights.main.connection_string
    "SCM_DO_BUILD_DURING_DEPLOYMENT"        = "false"
  }
}
