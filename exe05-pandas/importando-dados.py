
# %%
import pandas as pd

df = pd.read_csv("../data/vendas.csv")
df
# %%
df.head(3)

# %%
df.info(memory_usage='deep')

# %%
df.describe()

# %%

df['Data'] = pd.to_datetime(df['Data'])
df

# %%
df['Data'].dtype

# %%
df['Total'] = df['Quantidade']* df['Preco']
df

# %%
df.sort_values(by= 'Data')

# %%
df.to_csv("vendas_processadas.csv",index=False)
# %%
