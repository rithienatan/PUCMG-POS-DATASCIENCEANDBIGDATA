{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xNb6EFqQvaaV"
      },
      "source": [
        "# INGESTÃO DE DADOS NO AZURE STORAGE ACCOUNT USANDO PYTHON"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "wtZNCNlZvdsa"
      },
      "source": [
        "## PARA REALIZAR ESTE PROCEDIMENTO, É NECESSÁRIO COLETAR A CHAVE DE CONEXÃO DA CONTA DE ARMAZENAMENTO"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xb4z2YXYv0iw"
      },
      "source": [
        "### VAMOS UTILIZAR DADOS PÚBLICOS DE CASOS DE COVID NO BRASIL\n",
        "#### LINK PARA ACESSO: https://brasil.io/dataset/covid19/files/\n",
        "IREMOS UTILIZAR OS CASOS CONFIRMADOS DE COVID\n",
        "URL: https://data.brasil.io/dataset/covid19/caso_full.csv.gz"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "29el4y7HwUt0"
      },
      "source": [
        "## CONFIGURAÇÃO DO AMBIENTE"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "qQ9h0Sg-0qxb"
      },
      "source": [
        "### INSTALAÇÃO DE BIBLIOTECAS"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7owELzAT0jfG",
        "outputId": "22e12fcd-23ae-4198-c280-bd5f939733db"
      },
      "outputs": [],
      "source": [
        "pip install azure-storage-blob"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "EWle1tjV0vs0"
      },
      "source": [
        "### IMPORTAÇÃO DE BIBLIOTECAS"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "HABEICIewW0S"
      },
      "outputs": [],
      "source": [
        "import requests\n",
        "import gzip\n",
        "import shutil\n",
        "from azure.storage.blob import BlobClient"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "pMXx1QKRwgbm"
      },
      "source": [
        "### FUNÇÃO PARA REALIZAR DOWNLOAD DE DADOS"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "3UR_TL2hwYnJ"
      },
      "outputs": [],
      "source": [
        "def download_dados(url, nome_arquivo):\n",
        "  requisicao = requests.get(url)\n",
        "  conteudo = requisicao.content\n",
        "  arquivo = open(nome_arquivo, 'wb')\n",
        "  arquivo.write(conteudo)\n",
        "  arquivo.close()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fEGkFC5jxAS8"
      },
      "source": [
        "### REALIZAR O DOWNLOAD DOS DADOS"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "bp8hAMTdxBwC"
      },
      "outputs": [],
      "source": [
        "download_dados('https://data.brasil.io/dataset/covid19/caso_full.csv.gz', 'caso_full.csv.gz')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tbJOA7s5xbZS"
      },
      "source": [
        "#### DESCOMPACTAR ARQUIVO"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "DKtbe5VXxcw9"
      },
      "outputs": [],
      "source": [
        "with gzip.open('caso_full.csv.gz', 'rb') as arquivo_compactado:\n",
        "  with open('caso_full.csv', 'wb') as arquivo_descompactado:\n",
        "    shutil.copyfileobj(arquivo_compactado,arquivo_descompactado)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5boNn3FOyy27"
      },
      "source": [
        "### CARREGAR O ARQUIVO NO DATALAKE"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "TiYxbAPP0HyZ"
      },
      "source": [
        "#### VARIÁVEL DO ENDPOINT DE CONEXÃO"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "HNZGj-L_y4cD"
      },
      "outputs": [],
      "source": [
        "endpoint = ''"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "j0ABBra81OFT"
      },
      "source": [
        "#### CRIANDO CONEXÃO COM O STORAGE DA PLATAFORMA MICROSOFT AZURE"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "lvBjv1RW1SNQ"
      },
      "outputs": [],
      "source": [
        "blob = BlobClient.from_connection_string(conn_str=endpoint, container_name=\"datalake-aulas\", blob_name=\"raw/brazil.io/caso_full.csv\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "e9F-xG212Ryk"
      },
      "source": [
        "#### CARREGAR O ARQUIVO PARA O DATALAKE"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "ZDe9OyJg2Tqu"
      },
      "outputs": [],
      "source": [
        "with open(\"caso_full.csv\", \"rb\") as data:\n",
        "    blob.upload_blob(data)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1sJnyrcUj285"
      },
      "source": [
        "Pyspark"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JVlRyYt7m6_X",
        "outputId": "4bf58bc4-24f9-4634-e556-2fd1232276c5"
      },
      "outputs": [],
      "source": [
        "!pip install pyspark \n",
        " \n",
        "from pyspark.sql import SQLContext, SparkSession, functions as F \n",
        "from pyspark import SparkFiles\n",
        "from pyspark.sql.types import * \n",
        "from pyspark.sql.functions import * \n",
        "\n",
        "spark = SparkSession.builder.getOrCreate() \n",
        "sql = SQLContext(spark)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "UKEhu6WspB-T"
      },
      "source": [
        "Leitura do Dataset"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "4b1A5BujoseS"
      },
      "outputs": [],
      "source": [
        "df_caso_full = spark.read.format('csv').options(header=True, sep = ',').load('caso_full.csv')\n",
        "df_caso_full.createOrReplaceTempView('caso_full')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "id": "Ekt2lBohosUx"
      },
      "outputs": [],
      "source": [
        "df_dim_cidade = sql.sql(''' SELECT DISTINCT city_ibge_code, city, state, place_type FROM caso_full ''')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "id": "yxd7v8jJuKER"
      },
      "outputs": [],
      "source": [
        "df_dim_cidade.coalesce(1).write.format('csv').options(header=True, sep = ',').save('dim_cidade')"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1hZfoDs0sFre"
      },
      "source": [
        "Carregando"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "id": "6hgPhNYPo8Xm"
      },
      "outputs": [],
      "source": [
        "blob = BlobClient.from_connection_string(conn_str=endpoint, container_name=\"datalake-aulas\", blob_name=\"consume/brazil.io/dim_cidade/dim_cidade.csv\")\n",
        "with open(\"/content/dim_cidade/part-00000-83195d81-56f5-4ce6-8b84-cb10b984950f-c000.csv\", \"rb\") as data:\n",
        "    blob.upload_blob(data)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "id": "-xEAArQRqIIs"
      },
      "outputs": [],
      "source": [
        "df_dim_periodo = sql.sql('''\n",
        "select  distinct date, \n",
        "        weekofyear(cast(date as timestamp)) AS week, \n",
        "        left(date, 4) AS year, \n",
        "        substring(date, 6, 2) AS month, \n",
        "        right(date, 2) AS day,\n",
        "        case \n",
        "          when cast(substring(date, 6, 2) as integer) in (1,2,3) then 1\n",
        "          when cast(substring(date, 6, 2) as integer) in (4,5,6) then 2\n",
        "          when cast(substring(date, 6, 2) as integer) in (7,8,9) then 3\n",
        "          else 4\n",
        "        end as quarter,\n",
        "        case\n",
        "          when dayofweek(cast(date as timestamp)) = 1 then 'domingo'\n",
        "          when dayofweek(cast(date as timestamp)) = 2 then 'segunda-feira'\n",
        "          when dayofweek(cast(date as timestamp)) = 3 then 'terça-feira'\n",
        "          when dayofweek(cast(date as timestamp)) = 4 then 'quarta-feira'\n",
        "          when dayofweek(cast(date as timestamp)) = 5 then 'quinta-feira'\n",
        "          when dayofweek(cast(date as timestamp)) = 6 then 'sexta-feira'\n",
        "          else 'Sábado'\n",
        "        end as name_day\n",
        "from caso_full \n",
        "''')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "id": "Z9t4BzLdqQ7t"
      },
      "outputs": [],
      "source": [
        "df_dim_periodo.coalesce(1).write.format('csv').options(header=True, sep = ',').save('dim_periodo')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "id": "2n6QpuTlvm0D"
      },
      "outputs": [],
      "source": [
        "blob = BlobClient.from_connection_string(conn_str=endpoint, container_name=\"datalake-aulas\", blob_name=\"consume/brazil.io/dim_periodo/dim_periodo.csv\")\n",
        "with open(\"/content/dim_periodo/part-00000-e606768a-7ecb-4341-8379-1b85b4ffd99e-c000.csv\", \"rb\") as data:\n",
        "    blob.upload_blob(data)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "id": "vsEWsfMWwN5n"
      },
      "outputs": [],
      "source": [
        "df_dim_fatos = sql.sql('''\n",
        "select  distinct \n",
        "        city_ibge_code,\n",
        "        date, \n",
        "        estimated_population, \n",
        "        estimated_population_2019, \n",
        "        is_last,\n",
        "        is_repeated, \n",
        "        last_available_confirmed, \n",
        "        last_available_confirmed_per_100k_inhabitants, \n",
        "        last_available_date, \n",
        "        last_available_death_rate, \n",
        "        last_available_deaths,\n",
        "        order_for_place,\n",
        "        new_confirmed, \n",
        "        new_deaths\n",
        "from caso_full \n",
        "''')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "id": "VD4eYJjPwNmR"
      },
      "outputs": [],
      "source": [
        "df_dim_fatos.coalesce(1).write.format('csv').options(header=True, sep = ',').save('dim_fatos')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "id": "Udti4_sXzM_Y"
      },
      "outputs": [],
      "source": [
        "blob = BlobClient.from_connection_string(conn_str=endpoint, container_name=\"datalake-aulas\", blob_name=\"consume/brazil.io/dim_fatos/dim_fatos.csv\")\n",
        "with open(\"/content/dim_fatos/part-00000-784b7503-9f28-471d-a252-17b2ce1c18a2-c000.csv\", \"rb\") as data:\n",
        "    blob.upload_blob(data)"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
