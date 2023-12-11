# Identificador de DDD

print("Descubra de onde é seu DDD\n")

# Solicita o número do usuário
numero_telefone = int(input("Digite seu número de telefone "))

# Separar dois primeiros numeros do telefone
ddd = int(str(numero_telefone)[:2])

# Compara os dois primeiros dígitos e identifica o ddd certo 
if ddd == 61:
    print("Brasília")
elif ddd == 71:
    print("Salvador")
elif ddd == 11:
    print("São Paulo")
elif ddd == 21:
    print("Rio de Janeiro")
elif ddd == 32:
    print("Juiz de Fora")
elif ddd == 19:
    print("Campinas")
elif ddd == 27:
    print("Vitória")
elif ddd == 31:
    print("Belo Horizonte")
else:
    print("DDD não cadastrado")