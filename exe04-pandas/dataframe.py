# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv",sep=';')
df.head(5)
# %%
#Mostrar colunas 

df.columns
# %%

#Mostrar dimensoes

df.shape


# %%
#Mostrar indices
df.index


# %%
# Mostrar tipo de dados

df.dtypes

# %%

# mostrar informacoes gerais

df.info(memory_usage='deep')
# %%
#Mostrar os tres ultimos registros 

df.head(3)

# %%

#Mostrar os dois ultimos 

df.tail(2)

# %%

df.sample(2)

# %%

df.iloc[0]

# %%

df.iloc[:3,:2]

# %%

dados = {
    'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Eva'],
    'Idade': [25, 30, 35, 28, 32],
    'Salario': [5000, 6000, 7500, 5500, 6800],
    'Setor': ['TI', 'RH', 'TI', 'Vendas', 'RH']
}

df_funcionarios = pd.DataFrame(dados)
df_funcionarios
# %%
df_funcionarios.iloc[-1,[0,2]]

# %%
df_funcionarios.iloc[[0,2,4]]
# %%
df_funcionarios = df_funcionarios.set_index('Nome')
df_funcionarios



# %%

df_funcionarios.loc['Alice']

# %%
df_funcionarios.loc[['Bob','Carol'],['Idade','Salario']]
# %%
