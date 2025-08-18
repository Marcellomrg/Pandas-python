# %%

#03.01 - Quantas linhas há no arquivo clientes.csv ?
#03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
#03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
#03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
#03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?


import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep=";")
clientes.head(10)
# %%
linhas = clientes.shape[0]
linhas

# %%
colunas_int = (clientes.dtypes=="int").sum()
colunas_int
# %%

produtos = pd.read_csv("../data/produtos.csv",sep=";")
produtos

# %%
produtos.dtypes

# %%
colunas_object = (produtos.dtypes == "object").sum()
colunas_object
# %%
cliente_id4 = clientes.loc[4]["IdCliente"]
cliente_id4

# %%
saldo_clientes10 = clientes.loc[9]["QtdePontos"]
saldo_clientes10


# %%
