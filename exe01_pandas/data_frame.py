# %%
import pandas as pd

idades = [31,40,34,67,89,24,56]

nomes = ["Marcello","Gustavo","irineu"
         ,"Aldi","Alves","Joana","Fernanda"]

series_idade = pd.Series(idades)

series_nomes = pd.Series(nomes)


df = pd.DataFrame()

df["Nomes"] = series_nomes
df["Idades"] = series_idade

df.iloc[0]["Nomes"]






# %%
