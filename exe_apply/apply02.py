# %%
import pandas as pd
# %%
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carlos', 'Diana'],
    'idade': [25, 45, 70, 35],
    'salario': [3000, 5000, 8000, 4500]
})
df
# No mesmo DataFrame, use apply() com axis=1 para calcular 
# um "score" para cada pessoa baseado 
# na fórmula: score = salario/1000 + idade/10. 
# Crie uma função personalizada para isso.
# %%
def calcular_score(serie:pd.Series):
    score = serie['salario']/1000 + serie['idade']/10
    return score

df['score']= df[['salario','idade']].apply(calcular_score,axis=1)
# %%
df
# %%
