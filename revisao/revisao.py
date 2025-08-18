# %%
import pandas as pd

idades = [23,45,67,13,25,19]

nomes = ['Marcello','Gustavo','Aldi','Fernanda','Manoel','Vicky']

series_familia = pd.Series(idades,nomes)
series_familia
# %%
series_familia['Marcello']
# %%
series_familia.loc['Marcello']

# %%
series_familia.iloc[0]

# %%
series_familia.iloc[[0]]
# %%
series_familia[series_familia>30]
# %%
