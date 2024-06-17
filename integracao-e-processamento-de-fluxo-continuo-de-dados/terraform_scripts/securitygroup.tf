# Criando um grupo de segurança
resource "azurerm_network_security_group" "securitygroup-aulas" {
    name = var.gruposeguranca
    location = var.localizacao
    resource_group_name = var.gruporecursos_aula
    depends_on = [azurerm_resource_group.resourcegroup_aulas,
    azurerm_virtual_network.network-aulas]
    tags = var.tags
}

# Criando regra de segurança para conexão na porta SSH (22)
resource "azurerm_network_security_rule" "inboundrole-ssh-aulas" {
    name = "regraportassh"
    priority = 100
    direction = "Inbound"
    access = "Allow"
    protocol = "Tcp"
    source_port_range = "*"
    destination_port_range = "22"
    source_address_prefixes = [var.ip_pessoal]
    destination_address_prefix = "*"
    resource_group_name = var.gruporecursos_aula
    network_security_group_name = azurerm_network_security_group.securitygroup-aulas.name
    depends_on = [azurerm_resource_group.resourcegroup_aulas,
    azurerm_virtual_network.network-aulas,
    azurerm_network_security_group.securitygroup-aulas]
}

# Criando regra de segurança para conexão na porta HTTP (80)
resource "azurerm_network_security_rule" "inboundrole-http-aulas" {
    name = "regraportahttp"
    priority = 101
    direction = "Inbound"
    access = "Allow"
    protocol = "Tcp"
    source_port_range = "*"
    destination_port_range = "80"
    source_address_prefixes = [var.ip_pessoal]
    destination_address_prefix = "*"
    resource_group_name = var.gruporecursos_aula
    network_security_group_name = azurerm_network_security_group.securitygroup-aulas.name
    depends_on = [azurerm_resource_group.resourcegroup_aulas,
    azurerm_virtual_network.network-aulas,
    azurerm_network_security_group.securitygroup-aulas]
}