import streamlit as st
import analiseVendas as av

def main():

    st.markdown('## Universidade Federal do Agreste de Pernambuco')
    st.markdown('### Fundamentos em Ciência de Dados')
    st.markdown('** Análise de Vendas da redeX **')
    st.markdown('Relatórios gerencias para apoio a tomada de decisão')


    pagina = st.sidebar.selectbox("Escolha um relatório", ["Total de Vendas por Ano",
    "Total de Vendas por Categoria", "Total de Vendas de Categoria por Ano", "Total de Vendas de Ano por Categoria",
    "Total de Vendas dos Anos por Categoria pelos meses", "Produtos mais vendidos por cada Fabricante",
    "Total de Vendas das Lojas por Categoria", "Ranking dos produtos com maiores vendas no geral e por Loja",
    "Ranking dos produtos com menores vendas no geral e por Loja", "Ranking dos produtos mais rentáveis no geral e por Loja",
    "Ranking de Vendas por Loja", "Ranking dos Vendedores com maior valor de vendas por Loja e Ano"])

    if pagina == "Total de Vendas por Ano":
        data = av.graficoA()
        st.plotly_chart(data)
    elif pagina == "Total de Vendas por Categoria":
        data = av.graficoB()
        st.plotly_chart(data)
    elif pagina == "Total de Vendas de Categoria por Ano":
        data = av.graficoC()
        st.plotly_chart(data)
    elif pagina == "Total de Vendas de Ano por Categoria":
        data = av.graficoD()
        st.plotly_chart(data)
    elif pagina == "Total de Vendas dos Anos por Categoria pelos meses":
        data = av.graficoE()
        for fig in data:
            st.plotly_chart(fig)
    elif pagina == "Produtos mais vendidos por cada Fabricante":
        data = av.graficoF()
        for fig in data:
            st.plotly_chart(fig)
    elif pagina == "Total de Vendas das Lojas por Categoria":
        data = av.graficoG()
        st.plotly_chart(data)
    elif pagina == "Ranking dos produtos com maiores vendas no geral e por Loja":
        data = av.graficoHIGeral(True)
        st.plotly_chart(data)
        data2 = av.graficoHI(False)
        for fig in data2:
            st.plotly_chart(fig)
    elif pagina == "Ranking dos produtos com menores vendas no geral e por Loja":
        data = av.graficoHIGeral(False)
        st.plotly_chart(data)
        data2 = av.graficoHI(True)
        for fig in data2:
            st.plotly_chart(fig)
    elif pagina == "Ranking dos produtos mais rentáveis no geral e por Loja":
        data = av.graficoJGeral()
        st.plotly_chart(data)
        data2 = av.graficoJ()
        for fig in data2:
            st.plotly_chart(fig)
    elif pagina == "Ranking de Vendas por Loja":
        data = av.graficoK()
        st.plotly_chart(data)
    elif pagina == "Ranking dos Vendedores com maior valor de vendas por Loja e Ano":
        data = av.graficoL()
        for fig in data:
            st.plotly_chart(fig)

    st.markdown('** Kelwin Jonas Silva Santos **')

if __name__ == "__main__":
    main()