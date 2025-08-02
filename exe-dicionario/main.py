# %%
from random import randint

jogadores = ['Marcello','Gustavo','Aldi','Manoel']

dic = {}

for i in jogadores:
    dic[i]=randint(1,6)

# %%
lista = list(dic.items())
lista.sort(key=lambda item:item[1])
print(f'O ganhador foi {lista[-1][0]}')
# %%



# %%
