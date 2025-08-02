# %%
import pandas as pd

notas = [8.5,7.0,9.2,6.8,8.9]

nomes = ['Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo']

series_alunos = pd.Series(notas,index=nomes)

series_alunos

# %%
# NOta de bruno

series_alunos[["Bruno"]]
# %%
# As tres maiores notas 
maiores_notas = series_alunos.nlargest(3)
maiores_notas
# %%

#Alunos com nota maior que 8

acima_de_8 = series_alunos[series_alunos>=8]
print(acima_de_8)
# %%
# media dos alunos

media = series_alunos.mean()
media



# %%
