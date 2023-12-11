# Sistema de Cofre

print("Cofre")

# Definir uma senha
senha_correta = 2002

# Solicitar a senha do usuário
tentativa_senha = int(input("Digite a senha: "))

# Verifica se a senha fornecida é correta; caso contrário, solicita novamente
while tentativa_senha != senha_correta:
    print("Senha Inválida")
    tentativa_senha = int(input("Digite a senha: "))

# Se a senha fornecida for correta, permite o acesso
print("Acesso permitido")
