import requests

url  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
url += 'CotacaoDolarPeriodo(dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
url += '@dataInicial=%2701-01-2021%27&@dataFinalCotacao=%2712-31-2021%27&$format=json'
ano = input('digite o ano: ')
dados = requests.get(url).json()
dados = dict(dados)

listacompra = list()
dicionario =dict()
maxauxiliar = 0
auxiliar = 0
contmedia = 0
for mes in range(1,13):
    mes = f'{mes:0>2}'
    for unidade in dados['value']:
        if dict(unidade)['dataHoraCotacao'][5:7] == mes:
            contmedia += 1
            auxiliar += float(dict(unidade)['cotacaoCompra'])
            if maxauxiliar < float(dict(unidade)['cotacaoCompra']):
                maxauxiliar = float(dict(unidade)['cotacaoCompra'])
                
    dicionario[mes+' mês']={'media':f'{auxiliar/contmedia:.4f}','maiorcontac':maxauxiliar}
    
    contmedia = 0
    auxiliar = 0 
    listacompra = list()

print('apliquei um for no dicionario para ficar melhor a visualização')
input('prescine Enter para continuar')
for mes in dicionario:
	print(mes,dicionario[mes])
input('Bye:)??')
            
