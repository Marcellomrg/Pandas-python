# %%
# Objetivo é separar o valor total da fatura do mês de cada cliente
import pandas as pd
# %%
df = pd.read_csv("vendas.csv",sep=";")
df['dtTransacao'] = pd.to_datetime(df['dtTransacao'])
df
# %%
df['vlParcela'] = df['vlVenda'] / df['qtParcelas']
df
# %%
df['OrdemParcela'] = df.apply(lambda row : [i for i in range(row['qtParcelas'])],axis=1 )
df_explode = df.explode('OrdemParcela')
# %%
def calcDtParcela(row):
    dt = row['dtTransacao'] + pd.DateOffset(month=row['OrdemParcela'])
    dt = f'{dt.year}-{dt.month}'
    return dt

df_explode['dtParcela'] = df_explode.apply(calcDtParcela,axis=1)
df_explode

# %%
(df_explode.groupby(by=["idCliente","dtParcela"])
 ['vlParcela'].sum()
                .reset_index())

# %%
