# %%

# 04.01 - Quantos clientes tem vínculo com a Twitch?
 # 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
 # 04.03 - Quantas transações ocorreram no dia 2025-02-01?

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep=";")
clientes

# %%
clientes_twitch = (clientes["FlTwitch"] == 1).sum()
clientes_twitch

# %%
saldo_maior1000 = (clientes["QtdePontos"] > 1000).sum()
saldo_maior1000

# %%
transacoes = pd.read_csv("../data/transacoes.csv",sep=";")
transacoes

# %%
transacoes["DtCriacao"] = pd.to_datetime(transacoes["DtCriacao"].str.replace("+0000 UTC","",regex=False),format="mixed")

transacoes["DtCriacao"]
# %%
