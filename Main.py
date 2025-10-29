# Atividade Prática

# 1 Questão

lista_notas = []

while True:
    valores = float(input("Digite uma nota: (Digite -1 para encerrar:)"))
    if valores != (-1):
        lista_notas.append(valores)
    else:
        break

print(lista_notas)

# Letra A

print(f"Esta lista tem {len(lista_notas)} notas.")

# Letra B

print(lista_notas)

# Letra C

for nota in reversed (lista_notas):
    print(nota)

# Letra D

print(sum(lista_notas))

# Letra E

print(sum(lista_notas) / len(lista_notas))

# Letra F
quantidade = 0
for nota in lista_notas:
    if nota > (sum(lista_notas) / len(lista_notas)):
        quantidade += 1
print(f"A quantidade de notas acima da média: {quantidade}")

# Letra G

quantidade = 0
for nota in lista_notas:
    if nota < 7:
        quantidade += 1
print(f"A quantidade de notas abaixo de 7: {quantidade}")

# Letra H

print("Gosto muito da sua aula.")





