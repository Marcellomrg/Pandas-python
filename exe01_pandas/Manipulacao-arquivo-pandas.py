# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")

df.to_csv("clientes.csv",index=False)

df.to_parquet("clientes.parquet",index=False)

df_2 = pd.read_parquet("clientes.parquet")

df.to_excel("clientes.xlsx",index=False)


# %%
