variable tags {
    default = {
        Aluno = ""
        Disciplina = ""
        Matrícula = ""
        Email = ""
        Professor = ""
    }
}

variable localizacao {
    description = "Localização geográfica dos recursos Azure"
    default = "Brazil South"
}

variable gruporecursos_aula {
    description = "Grupo de recursos utilizados durante as aulas"
    default = "resourcegroup_aulas"
}

variable contaarmazenamento {
    description = "Conta de armazenamento dos dados usados durante as aulas"
    default = "storageaccountXXXXXX" # Substituir o XXXXXX
}

variable containerdatalake {
    description = "Contêiner: Armanazenamento de blobs"
    default = "datalake-aulas"
}

variable "rede" {
    description = "Nome da rede virtual que será criada para as atividades"
    default = "vnetXXXXXX" # Substituir o XXXXXX
}
variable "gruposeguranca" {
    description = "Grupo de segurança da plataforma Azure"
    default = "vnetsecuritygroupXXXXXX" # Substituir o XXXXXX
}
variable "ip_pessoal" {
    description = "Endereço IP do usuário que vai se conectar à rede Azure"
    default = "" # Utilize o site https://whatismyip.com.br/ para descobrir seu endereço IP
}

variable workspacesynapse {
    description = "Workspace de trabalho do serviço Azure Synapse Analytics"
    default = "wksynapsepucXXXXXX" # Substituir o XXXXXX
}

variable usuariosynapse {
    description = "Nome do usuário administrador do banco Azure Synapse Analytics"
    default = "" # Defina um nome de usuário para acessar o serviço (deve iniciar com uma letra, só pode ter letras e números)
}

variable senhasynapse {
    description = "Senha do usuário administrador do banco Azure Synapse Analytics"
    default = "" # Digite uma senha forte (mínimo de 8 dígitos), letras maiúsculas e minúsculas, caracteres especiais e números"
}

variable "datafactory" {
    description = "Serviço de processamento/ingestão"
    default = "datafactoryXXXXXX" # Substituir o XXXXXX
}

variable "virtualmachine_linux" {
    description = "Nome da máquina virtual LINUX"
    default = "vmlinuxXXXXXX" # Substituir o XXXXXX
}

variable "nomeusuariovm" {
    description = "Nome do usuário administrador que vai se conectar a maquina virtual"
    default = "" # Substituir por um nome de seu conhecimento
}
variable "senhausuariovm" {
    description = "Senha do usuário administrador que vai se conectar a maquina virtual"
    default = "" # Digite uma senha forte (mínimo de 12 dígitos), letras maiúsculas e minúsculas, caracteres especiais e números"
}