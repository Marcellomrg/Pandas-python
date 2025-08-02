
# %%
import pandas as pd

df = pd.read_csv("../data/vendas.csv")
df
# %%

# Vendas da 'Ana' com quantidade > 1

filtro = (df['Vendedor'] == 'Ana') & (df['Quantidade']>1)

df_2 = df[filtro].copy()
df_2
# %%
# Produtos caros (preço > 100) vendidos pelo 'Bruno'

filtro_3 = (df['Vendedor']=='Bruno') & (df['Preco']>100)

df_3 = df[filtro_3].copy()

df_3
# %%
# Vendas de Janeiro com total > 100
df['Total'] = df['Quantidade'] * df['Preco']
df['Data'] = pd.to_datetime(df['Data'])
filtro_4 = (df['Data'].dt.month == 1) & (df['Total']>100)
df_4 = df[filtro_4].copy()
df_4
# %%
# Vendas que NÃO são de Mouse nem Webcam

filtro_6 = (df['Produto'] != 'Mouse') & (df['Produto'] != 'Webcam')
df_5 = df[filtro_6].copy()

df_5

# %%
