import pandas as pd
import plotly.graph_objs as go

def graficoA():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Conversão dos valores Data Venda em tipo date
    dados['Data Venda'] = dados['Data Venda'].astype('datetime64')

    #Groupby para realizar a busca
    by_ano = dados.groupby(dados['Data Venda'].map(lambda x: x.year))['ValorVenda'].sum()

    #Plot do gráfico
    fig = go.Figure([go.Bar(x = by_ano.index, y = by_ano.values)])
    fig.update_layout(title = 'Total de Vendas por Ano', xaxis_title = 'Ano', yaxis_title = 'Total de Vendas')

    return fig

def graficoB():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Groupby para realizar a busca
    by_categoria = dados.groupby(dados['Categoria'])['ValorVenda'].sum()

    #Plot do gráfico
    fig = go.Figure([go.Bar(x = by_categoria.index, y = by_categoria.values)])
    fig.update_layout(title = 'Total de Vendas por Categoria', xaxis_title = 'Categoria', yaxis_title = 'Total de Vendas')
    return fig

def graficoC():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Conversão dos valores Data Venda em tipo date
    dados['Data Venda'] = dados['Data Venda'].astype('datetime64')
    
    #Transformação da DataFrame em multi index para o groupby
    dados.set_index(['Categoria', 'Data Venda'], inplace=True)
    dados.sort_index(inplace=True)

    #Groupby para realizar a busca
    busca = dados.groupby(['Categoria', dados.index.get_level_values('Data Venda').year])['ValorVenda'].sum()
    dic = busca.to_dict()
    df = pd.DataFrame({
        "Categoria": [i[0] for i in dic],
        "Ano": [i[1] for i in dic],
        "ValorVenda": [dic[i] for i in dic],
    })
    
    fig = go.Figure()
    for ano, group in df.groupby("Ano"):
        fig.add_trace(go.Bar(x=group["Categoria"], y=group["ValorVenda"], name=ano,
        hovertemplate="Ano=%s<br>Categoria=%%{x}<br>ValorVenda=%%{y}<extra></extra>"% ano))
    fig.update_layout(title = 'Total de Vendas de Categoria por Ano', xaxis_title = 'Categoria', yaxis_title = 'Total de Vendas', legend_title_text = "Ano")

    return fig

def graficoD():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Conversão dos valores Data Venda em tipo date
    dados['Data Venda'] = dados['Data Venda'].astype('datetime64')

    #Transformação da DataFrame em multi index para o groupby
    dados.set_index(['Categoria', 'Data Venda'], inplace=True)
    dados.sort_index(inplace=True)

    #Groupby para realizar a busca
    busca = dados.groupby(['Categoria', dados.index.get_level_values('Data Venda').year])['ValorVenda'].sum()
    dic = busca.to_dict()
    df = pd.DataFrame({
        "Categoria": [i[0] for i in dic],
        "Ano": [i[1] for i in dic],
        "ValorVenda": [dic[i] for i in dic],
    })
    
    fig = go.Figure()
    for categoria, group in df.groupby("Categoria"):
        fig.add_trace(go.Bar(x=group["Ano"], y=group["ValorVenda"], name=categoria,
        hovertemplate="Categoria=%s<br>Ano=%%{x}<br>ValorVenda=%%{y}<extra></extra>"% categoria))
    fig.update_layout(title = 'Total de Vendas de Ano por Categoria', xaxis_title = 'Ano por Categoria', yaxis_title = 'Total de Vendas', legend_title_text = "Categoria")

    return fig

def graficoE():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Conversão dos valores Data Venda em tipo date
    dados['Data Venda'] = dados['Data Venda'].astype('datetime64')

    #Criação de um grupo por anos para criar-se uma lista de anos
    by_ano = dados.groupby(dados['Data Venda'].map(lambda x: x.year)).sum()

    #Lista de anos
    listaAnos = by_ano.index.get_level_values(0).to_list()

    #Transformação da DataFrame em multi index para o groupby
    dados.set_index(['Categoria', 'Data Venda'], inplace=True)
    dados.sort_index(inplace=True)

    #Groupby para realizar a busca
    busca = dados.groupby(['Categoria', dados.index.get_level_values('Data Venda').year, dados.index.get_level_values('Data Venda').month])['ValorVenda'].sum()
    dic = busca.to_dict()

    dfAnos = []

    for k in range(len(listaAnos)):
        listCat = []
        listAno = []
        listMes = []
        listValorVenda = []
        for i in dic:
            if(i[1] == listaAnos[k]):
                listCat.append(i[0])
                listAno.append(i[1])
                listMes.append(i[2])
                listValorVenda.append(dic[i])

        df = pd.DataFrame({
            "Categoria": listCat,
            "Ano": listAno,
            "Mes": listMes,
            "ValorVenda": listValorVenda,
        })
        dfAnos.append(df)

    graficos = []
    for k in range(len(listaAnos)):
        fig = go.Figure()
        for categoria, group in dfAnos[k].groupby(["Categoria"]):
            fig.add_trace(go.Bar(x=group["Mes"], y=group["ValorVenda"], name=categoria))
        fig.update_layout(title = 'Total de Vendas de '+str(listaAnos[k])+' por Categoria pelos meses', xaxis_title = 'Meses', yaxis_title = 'Total de Vendas', legend_title_text = "Categoria")
        graficos.append(fig)

    return graficos

def graficoF():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Transformação da DataFrame em multi index para o groupby
    dados.set_index(['Fabricante', 'Produto'], inplace=True)
    dados.sort_index(inplace=True)

    #Groupby para realizar a busca
    busca = dados.groupby(['Fabricante', 'Produto'])['Cidade'].count()

    listaFabricantes = sorted(list(set(busca.index.get_level_values(0).to_list())))

    dic = busca.to_dict()

    listaPorFabri = []

    for k in range(len(listaFabricantes)):
        listProd = []
        listNumeroVendas = []
        for i in dic:
            if(i[0] == listaFabricantes[k]):
                listProd.append(i[1])
                listNumeroVendas.append(dic[i])

        listaPorFabri.append([listaFabricantes[k], [x for y, x in sorted(zip(listNumeroVendas, listProd))], [y for y, x in sorted(zip(listNumeroVendas, listProd))]])
    
    graficos = []
    for k in range(len(listaFabricantes)):
        fig = go.Figure([go.Bar(x = listaPorFabri[k][1], y = listaPorFabri[k][2])])
        fig.update_layout(title = 'Número de Vendas da fabricante '+str(listaPorFabri[k][0])+' por Produto', xaxis_title = 'Produto', yaxis_title = 'Número de Vendas')
        graficos.append(fig)

    return graficos

def graficoG():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Transformação da DataFrame em multi index para o groupby
    dados.set_index(['Loja', 'Categoria'], inplace=True)
    dados.sort_index(inplace=True)

    #Groupby para realizar a busca
    busca = dados.groupby(['Loja', 'Categoria'])['ValorVenda'].sum()

    dic = busca.to_dict()
    df = pd.DataFrame({
        "Loja": [i[0] for i in dic],
        "Categoria": [i[1] for i in dic],
        "ValorVenda": [dic[i] for i in dic],
    })
    
    fig = go.Figure()
    for categoria, group in df.groupby("Categoria"):
        fig.add_trace(go.Bar(x=group["Loja"], y=group["ValorVenda"], name=categoria,
        hovertemplate="Categoria=%s<br>Loja=%%{x}<br>ValorVenda=%%{y}<extra></extra>"% categoria))
    fig.update_layout(title = 'Total de Vendas das Lojas por Categoria', xaxis_title = 'Loja', yaxis_title = 'Total de Vendas', legend_title_text = "Categoria")

    return fig

def graficoHIGeral(ordem):
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Groupby para realizar a busca
    by_produto = dados.groupby(dados['Produto'])['ValorVenda'].sum().sort_values(ascending=ordem)

    #Plot do gráfico
    fig = go.Figure([go.Bar(x = by_produto.values, y = by_produto.index, orientation ='h')])
    if(ordem):
        fig.update_layout(title = 'Ranking dos produtos com maiores vendas no geral', xaxis_title = 'Total de Vendas', yaxis_title = 'Produtos')
    else:
        fig.update_layout(title = 'Ranking dos produtos com menores vendas no geral', xaxis_title = 'Total de Vendas', yaxis_title = 'Produtos')

    return fig

def graficoHI(ordem):
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Transformação da DataFrame em multi index para o groupby
    dados.set_index(['Loja', 'Produto'], inplace=True)
    dados.sort_index(inplace=True)

    #Groupby para realizar a busca
    busca = dados.groupby(['Loja', 'Produto'])['ValorVenda'].sum()
    busca = busca.sort_values()

    listaLojas = sorted(list(set(busca.index.get_level_values(0).to_list())))

    dic = busca.to_dict()

    listaPorLoja = []

    for k in range(len(listaLojas)):
        listProd = []
        listValorVenda = []
        for i in dic:
            if(i[0] == listaLojas[k]):
                listProd.append(i[1])
                listValorVenda.append(dic[i])

        listaPorLoja.append([listaLojas[k], [x for y, x in sorted(zip(listValorVenda, listProd), reverse=ordem)], [y for y, x in sorted(zip(listValorVenda, listProd), reverse=ordem)]])
    

    graficos = []
    for k in range(len(listaLojas)):
        fig = go.Figure([go.Bar(x = listaPorLoja[k][2], y = listaPorLoja[k][1], orientation = 'h')])
        fig.update_layout(title = 'Ranking de Vendas dos Produtos da Loja '+str(listaPorLoja[k][0]), xaxis_title ='Total de Vendas', yaxis_title = 'Produto')
        graficos.append(fig)

    return graficos

def graficoJGeral():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Criação de uma nova coluna Lucro para a DataFrame dados
    lucro = []
    valorVenda = dados['ValorVenda'].tolist()
    precoCusto = dados['preço Custo'].tolist()
    for k in range(dados['Loja'].count()):
        lucro.append(valorVenda[k]-precoCusto[k])
    dados['Lucro'] = lucro

    #Groupby para realizar a busca
    busca = dados.groupby(['Produto'])['Lucro'].sum().sort_values(ascending=True)

    #Plot do gráfico
    fig = go.Figure([go.Bar(x = busca.values, y = busca.index, orientation ='h')])
    fig.update_layout(title = 'Ranking dos produtos mais rentáveis no geral', xaxis_title = 'Lucro Total', yaxis_title = 'Produtos')

    return fig

def graficoJ():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')
    #Criação de uma nova coluna Lucro para a DataFrame dados

    lucro = []
    valorVenda = dados['ValorVenda'].tolist()
    precoCusto = dados['preço Custo'].tolist()
    for k in range(dados['Loja'].count()):
        lucro.append(valorVenda[k]-precoCusto[k])
    dados['Lucro'] = lucro

    #Groupby para realizar a busca
    busca = dados.groupby(['Loja', 'Produto'])['Lucro'].sum()

    #Lista das lojas sem valores duplicados
    lojas_set = sorted(list(set(busca.index.get_level_values(0).tolist())))

    graficos = []

    for k in range(0, len(lojas_set)):
        #Separação em uma series dos dados de produtos e lucro por loja
        grupo = busca.loc[lojas_set[k]].sort_values()
        valores_grupo = grupo.values
        produtos_grupo = grupo.index.get_level_values(0).tolist()

        #Plot do gráfico
        fig = go.Figure([go.Bar(x = valores_grupo, y = produtos_grupo, orientation = 'h')])
        fig.update_layout(title = 'Ranking dos produtos mais rentáveis da Loja '+str(lojas_set[k]), xaxis_title = 'Lucro total', yaxis_title = 'Produtos')
        graficos.append(fig)
    return graficos

def graficoK():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Groupby para realizar a busca
    busca = dados.groupby(['Loja'])['ValorVenda'].sum().sort_values()

    #Plot do gráfico
    fig = go.Figure([go.Bar(x = busca.index, y = busca.values)])
    fig.update_layout(title = 'Ranking de Vendas por Loja', xaxis_title = 'Loja', yaxis_title = 'Total de Vendas')

    return fig

def graficoL():
    #Leitura dos dados do arquivo Vendas.csv
    dados = pd.read_csv('data/Vendas.csv', encoding = 'ISO-8859-1', sep=';', decimal=',')

    #Conversão dos valores Data Venda em tipo date
    dados['Data Venda'] = dados['Data Venda'].astype('datetime64')

    #Transformação da DataFrame em multi index para o groupby
    dados.set_index(['Loja', 'Data Venda', 'Vendedor'], inplace=True)
    dados.sort_index(inplace=True)

    #Lista de cores hexadecimal para variação nos gráficos
    cores = ['#33FFCC', '#33CC99', '#339966', '#336666', '#333399', '#3300FF', '#bf00ff']

    #Groupby para realizar a busca
    busca = dados.groupby(['Loja',  dados.index.get_level_values('Data Venda').year, 'Vendedor'])['ValorVenda'].sum()
    busca = busca.sort_values()

    #Lista das lojas sem valores duplicados
    lojas_set = sorted(list(set(busca.index.get_level_values(0).tolist())))

    graficos = []

    for k in range(0, len(lojas_set)):
        #Dados separados daquela loja
        grupo = busca.loc[lojas_set[k]]
        #Lista de anos da loja da iteração
        grupoAnos = sorted(list(set(busca.loc[lojas_set[k]].index.get_level_values(0).tolist())))
        for i in range(0, len(grupoAnos)):
            grupo[grupoAnos[i]].plot.bar(rot=0)
            valores_grupo = grupo[grupoAnos[i]].values
            vendedores = grupo[grupoAnos[i]].index.get_level_values(0).tolist()
            #Plot do gráfico
            fig = go.Figure([go.Bar(x = vendedores, y = valores_grupo, marker_color = cores[k])])
            fig.update_layout(title = 'Ranking de {} dos Vendedores com maior Valor de Vendas da Loja {}'.format(grupoAnos[i], lojas_set[k]), xaxis_title = 'Total de Vendas', yaxis_title = 'Vendedores')
            graficos.append(fig)

    return graficos
