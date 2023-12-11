# Imprime uma mensagem para o usuário 
print("Descubra a média de valores positivos.")

# Inicializa uma lista vazia para armazenar os números positivos 
numeros = []
positivo = 0

# Loop que solicita a entrada de cinco números.
for i in range(5):
    # Solicita ao usuário para digitar um número 
    numero = float(input(f'Digite o {i + 1}° número: '))
    
    # Verifica se o número é positivo.
    if numero > 0:
        # Se for positivo, incrementa o contador e adiciona o número à lista.
        positivo += 1
        numeros.append(numero)

# Calcula a soma dos números positivos na lista.
soma = sum(numeros)

# Verifica se há números positivos para calcular a média.
if positivo > 0:
    # Calcula a média dos números positivos.
    media = soma / positivo
    
    # Imprime a quantidade de valores positivos e a média.
    print(f"{positivo} valores positivos")
    print(f"Média dos valores positivos: {media}")
else:
    # Caso não haja valores positivos, informa ao usuário.
    print("Não há valores positivos para calcular a média.")

