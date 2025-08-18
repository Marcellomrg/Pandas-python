# %%
import pandas as pd


# %%
#Dado o DataFrame abaixo, use apply() 
# para criar uma nova coluna 'categoria_idade' 
# que classifique as pessoas como 'jovem' (< 30),
#  'adulto' (30-60) ou 'idoso' (> 60).
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'idade': [25, 45, 70, 35],
    'salario': [3000, 5000, 8000, 4500]
})
def classificar_idade(idade:int):
    if idade < 30:
        return 'jovem'
    elif idade <= 60:
        return 'adulto'
    else:
        return 'idoso'

df['categoria_idade'] = df['idade'].apply(classificar_idade)

# %%
df

# %%
