# %%
import pandas as pd

idades = [31,32,45,76,90,45,21,48,100]


series_idade = pd.Series(idades)

print(series_idade)

media_idade = series_idade.mean()
variancia = series_idade.var()
summary_idades = series_idade.describe()

print(media_idade)
print(variancia)
print(summary_idades)

# %%
