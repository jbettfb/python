def calculoImc(peso, altura):

    imc = peso/(altura * altura)
    

    if imc < 16.9:
        return "muito abaixo do peso."
    elif imc >= 17 and imc < 18.4:
        return "abaixo do peso."
    elif imc >= 18.5 and imc <24.9:
        return "com o peso normal."
    elif imc >= 25 and imc <= 29.9:
        return "acima do peso."
    elif imc >= 30 and imc <= 34.4:
        return "com obesidadegrau 1."
    elif imc >= 35 and imc <= 40:
        return "com obesidad grau 2."
    elif imc < 40:
        return "com obesidade grau 3."