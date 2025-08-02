# %%
import pandas as pd

Vendas = [150, 230, 180, 290, 220]

Produtos = ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam']

Precos = [2500.0, 45.0, 120.0, 800.0, 150.0]
# %%
#Serie vendas series_produtos = pd.Series(Vendas)series_produtos

# %%
#Serie produtos
series_produtos = pd.Series(Produtos)
series_produtos

# %%
#serie precos
series_precos= pd.Series(Precos)
series_precos
# %%
#------VENDAS----------
#Mostrar o tipo de dados
tipo =series_produtos.dtype
tipo
# %%
#Mostrar o tamanho
tamanho = len(series_produtos)
tamanho
# %%
# Mostrar o 3 elemento
elemnto_3 =series_produtos.iloc[2]
elemnto_3

# %%

#------PRODUTOS----------
#Mostrar o tipo de dados
tipo =series_produtos.dtype
tipo
# %%
#Mostrar o tamanho
tamanho = len(series_produtos)
tamanho
# %%
# Mostrar o 3 elemento
elemnto_3 =series_produtos.iloc[2]
elemnto_3
# %%
#------PRECOS----------
#Mostrar o tipo de dados
tipo = series_precos.dtype
tipo
# %%
#Mostrar o tamanho
tamanho = len(series_precos)
tamanho
# %%
# Mostrar o 3 elemento
elemnto_3 = series_precos.iloc[2]
elemnto_3