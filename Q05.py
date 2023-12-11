#Contagem de Valores Pares

print("Contagem de valores pares")

# Criação da lista denominada "numeros" e da variável denominada "par"
numeros = []
par = 0

# Repete a ação 5 vezes
for i in range(5):
    # Solicita ao usuário um número
    numero = int(input(f'Digite o {i+1}° número: '))
    
    # Se o número for par vai ser  adicionado 1 
    if numero % 2 == 0:
        par += 1

# Mostra quantos números pares tem na lista
print(f"{par} valores pares")