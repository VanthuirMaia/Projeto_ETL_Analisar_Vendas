import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar o CSV
def carregar_csv(uploaded_file):
    return pd.read_csv(uploaded_file)

# Função para calcular o total de vendas
def calcular_total_venda(df):
    df['Total Venda'] = df['Quantidade'] * df['Preço Unitário']
    return df['Total Venda'].sum()

# Função para calcular total de vendas por produto
def total_vendas_por_produto(df):
    return df.groupby('Produto')['Total Venda'].sum()

# Função para filtrar vendas acima de um valor
def filtrar_vendas_acima_de_um_limite(df, limite):
    return df[df['Total Venda'] > limite]

# Função para exibir gráficos
def grafico_vendas_por_produto(df):
    vendas_produto = total_vendas_por_produto(df)
    plt.figure(figsize=(10, 6))
    vendas_produto.plot(kind='bar')
    plt.title('Total de Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Total de Vendas')
    st.pyplot(plt)

# Função principal para o Streamlit
def main():
    # Título do Dashboard
    st.title("Dashboard de Análise de Vendas")

    # Upload do arquivo CSV
    uploaded_file = st.file_uploader("Escolha um arquivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        # Carregar o CSV
        df = carregar_csv(uploaded_file)
        
        # Exibir as primeiras linhas do dataframe
        st.subheader("Primeiras linhas do arquivo CSV")
        st.write(df.head())

        # Calcular total de vendas
        total_geral = calcular_total_venda(df)
        st.subheader(f"Total de Vendas: R${total_geral:,.2f}")
        
        # Gráfico de vendas por produto
        grafico_vendas_por_produto(df)

        # Filtrar vendas acima de um valor
        limite = st.number_input("Filtrar vendas acima de:", min_value=0, value=0, step=1)
        vendas_filtradas = filtrar_vendas_acima_de_um_limite(df, limite)
        st.subheader(f"Vendas Acima de R${limite}:")
        st.write(vendas_filtradas)
        
        # Total de vendas por produto
        st.subheader("Total de Vendas por Produto")
        st.write(total_vendas_por_produto(df))

if __name__ == "__main__":
    main()
