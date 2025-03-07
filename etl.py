import csv
from typing import List, Dict
from datetime import datetime

path_arquivo = "./data/vendas.csv"

def ler_csv(nome_do_arquivo_csv) -> List[Dict]:
    """
    Função que lê um arquivo csv e retorna uma lista de dicionários.
    """
    lista = []
    with open(nome_do_arquivo_csv, mode="r", encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista

def calcular_total_venda(venda: dict) -> float:
    """
    Função que calcula o valor total da venda, multiplicando quantidade pelo preço unitário.
    """
    quantidade = int(venda['Quantidade'])  # Certifica-se que a quantidade é um número inteiro
    preco_unitario = float(venda['Preço Unitário'])  # Certifica-se que o preço unitário é um número flutuante
    total = quantidade * preco_unitario  # Calcula o total
    return total

def calcular_total_geral(vendas: List[Dict]) -> float:
    """
    Função que calcula o valor total de todas as vendas.
    """
    total_geral = 0
    for venda in vendas:
        total_geral += calcular_total_venda(venda)
    return total_geral

# Função 1: Vendas acima de um limite
def vendas_acima_de_um_limite(vendas: List[Dict], limite: float) -> List[Dict]:
    """
    Função para filtrar todas as vendas com valor superior ao limite especificado.
    """
    vendas_filtradas = []
    for venda in vendas:
        total_venda = calcular_total_venda(venda)
        if total_venda > limite:
            vendas_filtradas.append(venda)
    return vendas_filtradas

# Função 2: Contar vendas por produto
def contar_vendas_por_produto(vendas: List[Dict]) -> Dict[str, int]:
    """
    Função para contar quantas vezes cada produto aparece nas vendas.
    """
    contagem_produtos = {}
    for venda in vendas:
        produto = venda['Produto']
        if produto in contagem_produtos:
            contagem_produtos[produto] += 1
        else:
            contagem_produtos[produto] = 1
    return contagem_produtos

# Função 3: Filtrar vendas por data
def vendas_por_data(vendas: List[Dict], data_inicial: str, data_final: str) -> List[Dict]:
    """
    Função para filtrar vendas dentro de um intervalo de datas.
    """
    vendas_filtradas = []
    data_inicial = datetime.strptime(data_inicial, "%Y-%m-%d")
    data_final = datetime.strptime(data_final, "%Y-%m-%d")

    for venda in vendas:
        data_venda = datetime.strptime(venda['Data'], "%Y-%m-%d")
        if data_inicial <= data_venda <= data_final:
            vendas_filtradas.append(venda)
    return vendas_filtradas

# Exemplo de uso das funções:

vendas_itens = ler_csv(path_arquivo)

# Calculando total de todas as vendas
total_geral = calcular_total_geral(vendas_itens)
print(f"Total de todas as vendas: R$ {total_geral:.2f}")

# Filtrando vendas acima de R$ 500
limite = 500
vendas_filtradas = vendas_acima_de_um_limite(vendas_itens, limite)
print(f"\nVendas acima de R$ {limite}:")
for venda in vendas_filtradas:
    print(venda)

# Contando vendas por produto
vendas_por_produto = contar_vendas_por_produto(vendas_itens)
print("\nContagem de vendas por produto:")
for produto, quantidade in vendas_por_produto.items():
    print(f"{produto}: {quantidade}")

# Filtrando vendas entre 2023-01-01 e 2023-12-31
vendas_filtradas_data = vendas_por_data(vendas_itens, "2023-01-01", "2023-12-31")
print("\nVendas entre 2023-01-01 e 2023-12-31:")
for venda in vendas_filtradas_data:
    print(venda)
