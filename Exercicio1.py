# imc = peso /altura*altura
nome = input("Digite seu nome: ")
print("Olá, " + nome + "!")

peso = float(input("Digite seu peso: "))
print(f"Seu peso é: {peso} kg")

altura = float(input("DIgite sua altura em metros: "))
print(f"Sua altura é: {altura:.2f} metros")

calculoImc = float(peso/(altura*altura))
resultado = f'{nome} seu IMC é {calculoImc:.2f}'
print(resultado)