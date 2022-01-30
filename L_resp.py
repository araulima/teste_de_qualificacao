# -*- coding: utf-8 -*-

import pandas as pd

dados = pd.read_excel('teste.xlsx')
portadores = dados['NOME PORTADOR']

x = 0
for portador in portadores:
    if (portador == 'Sigiloso'):
     x = x + 1

print(x)