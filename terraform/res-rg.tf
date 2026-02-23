resource "azurerm_resource_group" "rg" {
  name     = "rg-casopractico2"
  location = var.location

  tags = {
    environment = "CP2"
  }
  
}