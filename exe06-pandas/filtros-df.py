# %%
import pandas as pd

df = pd.read_csv("../data/vendas.csv")
df
# %%
filtro = df['Quantidade'] > 3

df_2 = df[filtro].copy()

df_2
# %%
filtro_2 = (df['Preco']>=50) & (df['Preco']<=500)
df_3 = df[filtro_2].copy()
df_3
# %%
df
# %%
filtro_3 = df['Vendedor'] == 'Ana'
df_4 = df[filtro_3].copy()
df_4
# %%
filtro_4 = (df['Produto'] == 'Monitor') | (df['Produto'] == 'Notebook')
df_5 = df[filtro_4].copy()
df_5
# %%
df['Total'] = df['Quantidade']*df['Preco']
filtro_5 = df['Total'] > 200
df_5 = df[filtro_5].copy()
df_5
# %%
