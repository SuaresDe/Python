#!/usr/bin/env python
# coding: utf-8

# In[13]:


import random

aluno1 = str(input("Primeiro aluno: "))
aluno2 = str(input("Segundo aluno: "))
aluno3 = str(input("Terceiro aluno: "))
aluno4 = str(input("Quarto aluno: "))

lista = [aluno1, aluno2, aluno3, aluno4]


primeiro = random.choice(lista)
print(primeiro)
lista.remove(primeiro) 

segundo = random.choice(lista)
print(segundo)
lista.remove(segundo) 

terceiro = random.choice(lista)
print(terceiro)
lista.remove(terceiro) 

quarto = lista[0]  
print(quarto)


# In[ ]:




