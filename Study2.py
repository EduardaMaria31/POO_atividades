num_lista = ((1,9,8,6,3))
print(num_lista)

# 6°questão

print(f"O tamanho da sua lista é {(len(num_lista))}")

# 7°questão

print(f"A soma dos números informados na lista é: {sum(num_lista)}")

# 8°questão

print(f"Lista em ordem crescente {sorted(num_lista)}")

# 9°questão

print(f"Lista em ordem decrescente {sorted(num_lista, reverse=True)}")

# 10°questão

l1 = [9,6,3]
l2 = [7,4,1]

lista_soma = l1 + l2
print(f"LIsta mesclada: {lista_soma}")

# 11°questão

usuario = int(input("Digite um número:"))
if usuario in num_lista:
    print(f"Este número {usuario} já na lista.")
else:
    print(f"Este número {usuario} não está na lista.")