# %%
import pandas as pd

df = pd.read_csv("../data/vendas.csv")


df['Total'] = df['Quantidade'] * df['Preco']

df
# %%
# Total de vendas por vendedor (.groupby())
total_por_vendedor = df.groupby('Vendedor')['Total'].sum()
print(total_por_vendedor)

# %%
#Quantidade média vendida por produto

qnt_media_produto = df.groupby('Produto')['Quantidade'].mean()
qnt_media_produto

# %%
# Produto mais vendido (maior quantidade total)

qnt_max_vendida_produto = df.groupby('Produto')['Quantidade'].sum()
produto_mais_vendido = qnt_max_vendida_produto.idxmax()
produto_mais_vendido
# %%
#Vendedor com maior faturamento

max_fat_vendedor = df.groupby('Vendedor')['Total'].sum()
vendedor_maior_fat = max_fat_vendedor.idxmax()
vendedor_maior_fat

# %%