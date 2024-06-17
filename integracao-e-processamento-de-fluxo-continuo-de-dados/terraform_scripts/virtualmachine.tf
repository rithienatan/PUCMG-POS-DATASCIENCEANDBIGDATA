# Configurando uma interface de rede
resource "azurerm_network_interface" "interfaceredevm-aulas" {
    name = "cardinterface-aulas"
    location = var.localizacao
    resource_group_name = var.gruporecursos_aula
    
    ip_configuration {
        name = "internal"
        subnet_id = azurerm_subnet.subrede-aulas.id
        private_ip_address_allocation = "Dynamic"
        public_ip_address_id = azurerm_public_ip.ippublico-aulas.id
    }

    depends_on = [azurerm_resource_group.resourcegroup_aulas,
    azurerm_subnet.subrede-aulas]
}

resource "azurerm_virtual_machine" "vm-linux" {
    name = var.virtualmachine_linux
    location = var.localizacao
    resource_group_name = var.gruporecursos_aula
    network_interface_ids = [azurerm_network_interface.interfaceredevm-aulas.id]
    vm_size = "Standard_B2ms"
    delete_os_disk_on_termination = true
    delete_data_disks_on_termination = true

    storage_image_reference {
        publisher = "Canonical"
        offer = "0001-com-ubuntu-server-jammy"
        sku = "22_04-lts-gen2"
        version = "latest"
    }

    storage_os_disk {
        name = "discosistema"
        caching = "ReadWrite"
        create_option = "FromImage"
        managed_disk_type = "Standard_LRS"
    }

    os_profile {
        computer_name = "ubuntu-aulas"
        admin_username = somethingcommingfromvar
        admin_password = somethingcommingfromvar
    }

    os_profile_linux_config {
        disable_password_authentication = false
    }
    
    tags = var.tags
    depends_on = [azurerm_resource_group.resourcegroup_aulas,
    azurerm_network_interface.interfaceredevm-aulas]
}