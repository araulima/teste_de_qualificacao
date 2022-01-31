# teste_de_qualificacao
Respostas teste de qualificação

A. Quando um dinheiro injustificável passa por um processo em que se cria a origem desse dinheiro. O dinheiro recebido por meios ilícitos, que não tem como ser justificado nem taxado pela união, são “transformados” para que possa legitimar o recebimento de um montante.

B. É um cartão cedido pelo governo para o pagamento de despesas que se enquadram como Suprimentos de Fundos

C. Servidores públicos ou ocupantes de cargo em comissão em efetivo exercício no órgão.

D. http://www.transparencia.gov.br/download-de-dados/cpgf

E. https://www.portaltransparencia.gov.br/cartoes/cpgf?paginacaoSimples=true&tamanhoPagina=&offset=&direcaoOrdenacao=asc&colunasSelecionadas=mesExtrato%2CorgaoSuperior%2CorgaoVinculado%2CunidadeGestora%2CcpfPortador%2CnomePortador%2CcodigoFavorecido%2CnomeFavorecido%2CtipoTransacao%2CdataTransacao%2Cvalor&ordenarPor=mesExtrato&direcao=desc

F. Há transações em que os dados do portador são descritos como "SEM INFORMAÇÃO", não sendo fornecido.

G. Sim, é possível.

H. Ministério da Ciência, Tecnologia, Inovações e Comunicações.

I. Na maioria das vezes, sim é fornecido, nas vezes que não é fornecido é descrito como "SEM INFORMAÇÃO".

J. Nas transações classificadas como "Sigiloso", não é fornecido a data de ocorrência da transação, mas os valores são fornecidos.

K. import pandas as pd

dados = pd.read_excel('teste.xlsx')
dados['VALOR TRANSAÇÃO'] = dados['VALOR TRANSAÇÃO'].astype(float)

valores = dados["VALOR TRANSAÇÃO"]

total = sum(valores)

print('RS',round(total , 2))

L. import pandas as pd

dados = pd.read_excel('teste.xlsx')
portadores = dados['NOME PORTADOR']

x = 0
for portador in portadores:
    if (portador == 'Sigiloso'):
     x = x + 1

print(x)

M. import pandas as pd
dados = pd.read_excel('teste.xlsx')
dados['NOME ÓRGÃO SUPERIOR'] = dados['NOME ÓRGÃO SUPERIOR'].astype(object)

trans_sig = dados.loc[(dados["NOME PORTADOR"] == "Sigiloso")]
orgao = trans_sig['CÓDIGO ÓRGÃO SUPERIOR']

x = []
for i in orgao:
 if i not in x:
  x.append(i)

z= []
y=0
for k in range(0, len(x)):
 trans_sig_orgao_econ = dados.loc[(dados["NOME PORTADOR"] == "Sigiloso") & (dados["CÓDIGO ÓRGÃO SUPERIOR"] == x[k])]
 if(len(trans_sig_orgao_econ) > y):
  y = len(trans_sig_orgao_econ)
  z = trans_sig_orgao_econ

total_gasto = trans_sig_orgao_econ['VALOR TRANSAÇÃO']

a = []
for b in z['NOME ÓRGÃO SUPERIOR']:
 if b not in a:
  a.append(b)

print('Foi o órgão ', a)
print('Um total de RS ', round(sum(total_gasto), 2))

N. import pandas as pd 
dados = pd.read_excel('teste.xlsx')
saques = dados.loc[(dados["TRANSAÇÃO"] == 'SAQUE CASH/ATM BB')]

nomes = saques['NOME PORTADOR']

x = []
for i in nomes:
 if i not in x:
  x.append(i)

z = []
y = 0
for k in range(0, len(x)):
 aux_saques = dados.loc[(dados["TRANSAÇÃO"] == 'SAQUE CASH/ATM BB') & (dados["NOME PORTADOR"] == x[k])]
 if(len(aux_saques) > y):
  y = len(aux_saques)
  z = x[k]

aux = dados.loc[(dados['NOME PORTADOR'] == z)]
saq_total = aux['VALOR TRANSAÇÃO']
org = aux['NOME ÓRGÃO SUPERIOR']

a =[]
for b in org:
 if b not in a:
  a.append(b)

print('O portador: ', z)
print('Pertencente ao órgão: ', a)
print('Gastou um total de RS',round(sum(saq_total), 2))

O. import pandas as pd
dados = pd.read_excel('teste.xlsx')
nome_fav = dados['NOME FAVORECIDO']

x = []
for i in nome_fav:
 if i not in x:
  x.append(i)

z = []
y = 0
for k in range(0, len(x)):
 aux_nome = dados.loc[(dados['NOME FAVORECIDO'] == x[k])]
 if((len(aux_nome) > y) & (x[k] != 'NAO SE APLICA') & (x[k] != 'SEM INFORMACAO') & (x[k] != 'Sigiloso')):
  y = len(aux_nome)
  z = x[k]

print(z)

P. Para o desenvolvimento dos códigos, primeiramente separei as etapas que cada exercício deveria seguir. Depois passei a desenvolver cada etapa do código e testando para poder seguir para a próxima parte. Utilizei a metodologia cascata pois não tinha muito conhecimento da linguagem python, então caso algo não funcionasse como o esperado passava a pesquisar maneiras diferentes de realizar uma mesma coisa.
