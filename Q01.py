
# Calculadora de Impostos

print("Bem-vindo à Calculadora de Impostos")

# Solicitar o salário ao usuário
salario = float(input("Digite seu salário: "))

# Validar se o salário é válido (não negativo)
while salario < 0:
    print("\nDigite um salário válido.")
    salario = float(input("Digite seu salário: "))

# Calcular e exibir o imposto com base nas faixas salariais
if salario <= 2000:
    print('Isento de impostos')
elif 2000 < salario <= 3000:
    print(f"Imposto: R$ {salario * 0.08:.2f}")
elif 3000 < salario <= 4500:
    print(f"Imposto: R$ {salario * 0.18:.2f}")
else:
    print(f"Imposto: R$ {salario * 0.28:.2f}")
