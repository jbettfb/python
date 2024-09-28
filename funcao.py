import imc as util
def apresentacao(nome, idade , peso, altura):
    calculo = util.calculoImc(peso, altura)
    print(f"{nome}, seu imc esta em {calculo}")

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")
peso = float(input("Qual o seu peso? "))
altura = float(input("Qual a sua altura? "))

apresentacao(nome, idade, peso, altura)

