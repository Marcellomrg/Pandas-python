# %%

#05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch
#05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
#05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.
#05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
#05.05 - Selecione a primeira transação diária de cada cliente.

import pandas as pd
import numpy as np

clientes = pd.read_csv("../data/clientes.csv",sep=";")
clientes
# %%
clientes["twitch_points"] = clientes["FlTwitch"] * clientes["QtdePontos"]


clientes
# %%
clientes["log_pontos"] = np.log(clientes["QtdePontos"])
clientes



# %%
clientes["Apenas_uma"] = (clientes["FlEmail"] + clientes["FlTwitch"] +
                           clientes["FlYouTube"]+ clientes["FlBlueSky"]
                           +clientes["FlInstagram"])

clientes

# %%

clientes["QtdePontos"].sort_values(ascending=False).head(1)


# %%

clientes["data"] = pd.to_datetime(clientes["DtCriacao"].str.replace("+0000 UTC","",regex=False),format='mixed')
clientes[["IdCliente","data"]].drop_duplicates(keep="first")
# %%


