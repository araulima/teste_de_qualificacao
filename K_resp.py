# -*- coding: utf-8 -*-

import pandas as pd

dados = pd.read_excel('teste.xlsx')
dados['VALOR TRANSAÇÃO'] = dados['VALOR TRANSAÇÃO'].astype(float)

valores = dados["VALOR TRANSAÇÃO"]

total = sum(valores)

print('RS',round(total , 2))

