# -*- coding: utf-8 -*-

import pandas as pd
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
