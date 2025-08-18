# %%
import pandas as pd

q1 = pd.DataFrame({
    'produto': ['A', 'B', 'C'],
    'vendas': [100, 150, 200],
    'trimestre': ['Q1', 'Q1', 'Q1']
})
q1
# %%

q2 = pd.DataFrame({
    'produto': ['A', 'B', 'C'],
    'vendas': [120, 180, 160],
    'trimestre': ['Q2', 'Q2', 'Q2']
})
q2
# %%
q3 = pd.DataFrame({
    'produto': ['A', 'B', 'D'],  # Note: produto D só no Q3
    'vendas': [90, 200, 300],
    'trimestre': ['Q3', 'Q3', 'Q3']
})
q3

# %%
# Você tem três DataFrames de vendas de trimestres diferentes. 
# Use concat() para combiná-los em um único DataFrame.

q1_q2_q3 = pd.concat([q1,q2,q3],ignore_index= True)
q1_q2_q3

# %%
# Use concat() para combinar 
# os DataFrames horizontalmente (axis=1),
#  mas primeiro você precisa 
# resolver o problema de índices diferentes. 
# Como você faria?

q1_novo = q1.set_index('produto')
q2_novo = q2.set_index('produto')
q3_novo = q3.set_index('produto')

q1_q2_q3 = pd.concat([q1_novo,q2_novo,q3_novo],axis=1)
q1_q2_q3
# %%
#Combine os DataFrames usando concat() 
# com keys para criar um índice hierárquico 
# que identifique a origem de cada linha.

df_combinando = pd.concat([q1,q2,q3],keys=['q1','q2','q3'],)
df_combinando.loc['q1']

# %%
