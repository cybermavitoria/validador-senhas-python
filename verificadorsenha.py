senha=input("Digite uma senha:")
if len(senha) >8:
    print("Senha fraca, muito curta")
elif senha.islower() or senha.isupper():
    print("Senha fraca, deve conter letras maiúsculas e mininúsculas")
elif senha.isalnum():
    print("Senha fraca, adicione caracteres especiais")
else:
    print("Sua senha é forte, muito bem!")