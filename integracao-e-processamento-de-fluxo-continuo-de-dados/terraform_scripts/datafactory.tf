# Criar um serviço do Data Factory (Serviço de ETL)
resource "azurerm_data_factory" "datafactory-aulas" {
    name = var.datafactory
    resource_group_name = var.gruporecursos_aula
    location = var.localizacao
    tags = var.tags
    depends_on = [azurerm_resource_group.resourcegroup_aulas]
}