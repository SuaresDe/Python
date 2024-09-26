import json
import csv
import os
from typing import List, Dict, Union

def leitura_json(path_json: str) -> Union[Dict, List]:
    try:
        with open(path_json, 'r') as file:
            dados_json = json.load(file)
        return dados_json
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading JSON file: {e}")
        return []

def leitura_csv(path_csv: str) -> List[Dict]:
    dados_csv = []
    try:
        with open(path_csv, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
    except FileNotFoundError as e:
        print(f"Error reading CSV file: {e}")
    return dados_csv

def leitura_dados(path: str, tipo_arquivo: str) -> Union[List[Dict], Dict]:
    if tipo_arquivo == 'csv':
        return leitura_csv(path)
    elif tipo_arquivo == 'json':
        return leitura_json(path)
    return []

def get_columns(dados: List[Dict]) -> List[str]:
    return list(dados[0].keys()) if dados else []

def rename_columns(dados: List[Dict], key_mapping: Dict[str, str]) -> List[Dict]:
    new_dados_csv = []
    
    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            new_key = key_mapping.get(old_key, old_key)  
            dict_temp[new_key] = value
        new_dados_csv.append(dict_temp)
    
    return new_dados_csv 

def size_data(dados: List[Dict]) -> int:
    return len(dados)

def join(dadosA: List[Dict], dadosB: List[Dict]) -> List[Dict]:
    combine_list = []
    combine_list.extend(dadosA)
    combine_list.extend(dadosB)
    return combine_list  

def transformando_dados_tabela(dados, nomes_colunas):
    dados_combinados_tabela = [nomes_colunas]

    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)

    return dados_combinados_tabela

def salvando_dados(dados, path):
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

path_json = 'raw_datas/dados_empresaA.json'
path_csv = 'raw_datas/dados_empresaB.csv'

# Leitura
dados_json = leitura_json(path_json)
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)
print(f"Tamanho dos dados JSON: {tamanho_dados_json}")

dados_csv = leitura_csv(path_csv)
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)
print(f"Tamanho dos dados CSV: {tamanho_dados_csv}")

# Transformação
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)

dados_fusao = join(dados_csv, dados_json)
nome_colunas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)
print("Colunas da Fusão:", nome_colunas_fusao)
print("Tamanho dos dados da Fusão:", tamanho_dados_fusao)

# Salvar
dados_fusao_tabela = transformando_dados_tabela(dados_fusao, nome_colunas_fusao)
path_dados_combinados = 'dados_processados/processed_datas/dados_combinados.csv'

salvando_dados(dados_fusao_tabela, path_dados_combinados)
print(path_dados_combinados)
