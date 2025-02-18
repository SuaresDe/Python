#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = 10


contador = 0
soma = 0
numero_impar_atual = 1

while contador < n:
    soma += numero_impar_atual
    numero_impar_atual += 2
    contador += 1

print("A soma dos primeiros", n, "números ímpares é:", soma)
#(1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19) é igual a 100.

