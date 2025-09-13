output "app_service_name" {
  value = azurerm_linux_web_app.main.name
}

output "app_service_resource_group_name" {
  value = azurerm_linux_web_app.main.resource_group_name
}
