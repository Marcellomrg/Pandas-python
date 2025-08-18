# %%
#Objetivo dessa case é juntas todas as tabelas de homicios usando os dados da pasta ipea
import pandas as pd 
import os
# %%

# %%
def read_file(file_name):

    df = (pd.read_csv(f"../data/ipea/{file_name}.csv",sep=";")
                        .set_index(["nome","período"])
                        .drop("cod",axis=1)
                        .rename(columns={"valor":file_name}))
    return df


# %%
lista_dfs = []
dfs = os.listdir("../data/ipea")
# %%
for i in dfs:
    files = i.split('.')[0]
    lista_dfs.append(read_file(files))

lista_dfs[-4]

# %%
df_geral =( pd.concat(lista_dfs,axis=1)
           .reset_index()
           .sort_values(['período','nome']))

df_geral


# %%
df_geral.to_csv("homicidios_consolidados.csv",index=False,sep=";")

# %%
