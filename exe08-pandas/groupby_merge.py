# %%
import pandas as pd

# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?
usuarios = pd.read_csv("../data/clientes.csv",sep =";")
usuarios.head(5)
# %%
redes = [           
                    "FlEmail"	
                   ,"FlTwitch"	
                   ,"FlYouTube"  
                   ,"FlBlueSky"	
                   ,"FlInstagram"]


# %%
quantidade_media = usuarios.groupby("IdCliente")[redes].sum().agg(["mean","var","max"])
quantidade_media
# %%
#06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.

transacoes = pd.read_csv("../data/transacoes.csv",sep = ';')
transacoes.head()
# %% 
transacoes.groupby(by="IdCliente")[["IdTransacao"]].count().sort_values(by="IdTransacao",ascending=False).head(10)
# %%
# 06.03 - Qual usuário teve maior quantidade de pontos debitados?

transacoes.groupby(by='IdCliente')[['QtdePontos']].sum().sort_values(by='QtdePontos',ascending=False).head(1)

# %%
# 06.04 - Quem teve mais transações de Streak?
produtos = pd.read_csv("../data/produtos.csv",sep=';')
produtos.head(5)
# %%
transacoes_produto = pd.read_csv("../data/transacao_produto.csv",sep=';')
transacoes_produto.head(5)

# %%
filtro = produtos['DescProduto'] == 'Presença Streak'
produtos_streak = produtos[filtro]
produtos_streak
# %%
transacoes.merge(right=transacoes_produto,how="left",on='IdTransacao').merge(right=produtos_streak,how="inner",on='IdProduto').groupby(by='IdCliente')[['QtdeProduto']].sum().sort_values('QtdeProduto',ascending=False).head(1)

# %%
#06.05 - Qual a média de transações / dia?
temp = transacoes["DtCriacao"].str.replace(" +0000 UTC", "", regex=False)
transacoes["Data"] = pd.to_datetime(temp,format="mixed")
transacoes
# %%
media_tran_dia= transacoes.groupby(by='Data')[['IdTransacao']].count()
media_real = media_tran_dia['IdTransacao'].mean()
media_tran_dia["Media"] = media_real
media_tran_dia
# %%
#06.06 - Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?
transacoes.groupby(by='IdCliente')['QtdePontos'].describe()
# %%
