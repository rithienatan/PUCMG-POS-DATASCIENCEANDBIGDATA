# Criar um workspace do Azure Synapse Analytics (Serviço de EDW)
resource "azurerm_synapse_workspace" "workspacesynapse-aulas" {
    name = var.workspacesynapse
    resource_group_name = var.gruporecursos_aula
    location = var.localizacao
    storage_data_lake_gen2_filesystem_id = "https://${var.contaarmazenamento}.dfs.core.windows.net/${var.containerdatalake}"
    sql_administrator_login = var.usuariosynapse
    sql_administrator_login_password = var.senhasynapse
    tags = var.tags
    identity {
        type = "SystemAssigned"
    }
    depends_on = [azurerm_resource_group.resourcegroup_aulas, azurerm_storage_account.storageaccount_aulas]
}

# Liberar acesso do Synapse para todos os IP's
resource "azurerm_synapse_firewall_rule" "regraacessowebsynapse-aulas" {
    name = "AllowAll"
    synapse_workspace_id = azurerm_synapse_workspace.workspacesynapse-aulas.id
    start_ip_address = "0.0.0.0"
    end_ip_address = "255.255.255.255"
    depends_on = [azurerm_resource_group.resourcegroup_aulas,
    azurerm_synapse_workspace.workspacesynapse-aulas]
}

# Regra para permitir que o serviço acesse os arquivos na conta de armazenamento
resource "azurerm_role_assignment" "permissaostorageaccountsynapse-aulas" {
    scope = azurerm_storage_account.storageaccount_aulas.id
    role_definition_name = "Storage Blob Data Contributor"
    principal_id = azurerm_synapse_workspace.workspacesynapse-aulas.identity.0.principal_id
    depends_on = [azurerm_resource_group.resourcegroup_aulas, azurerm_synapse_firewall_rule.regraacessowebsynapse-aulas, azurerm_storage_account.storageaccount_aulas]
}