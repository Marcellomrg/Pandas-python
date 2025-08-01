# %%
import pandas as pd

url = "https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil"

df = pd.read_html(url)

dfs = df[1]
dfs

dfs.to_csv("ufs.csv",sep=";")

# %%
