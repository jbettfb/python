# def Informacoes(nome, sobrenome):
#    return f"{nome} {sobrenome}"

# def PegarIdade(idade):
#     return f"{idade}"

# anoNascimento = int(input("qual é o seu ano de nascimento?"))
# print(f"{anoNascimento}")

# anoAtual = int(input("em que ano estamos?"))

# idade = anoAtual - anoNascimento
# print(idade)

saldo = 0
historico = ""
while True: 
    num = int(input("Para fazer um deposito pressione 1, Para fazer uma retirada pressione 2, Para ver o historico pressione 3, para sair pressione 4: "))
    if num == 1:
        deposito = int(input("Qual valor voce deseja depositar?"))
        saldo += deposito 
        historico += f"voce depositou R${deposito}\n"

    elif num == 2:
        retirada = int(input("Insira o valor da retirada: "))
        if saldo > retirada:
            saldo -= retirada
            historico += f"voce retirou R${retirada}\n"
        else:
            print("voce nao possui saldo sufiente para sacar\n")

    elif num == 3:
        print(historico)
    elif num == 4:
        print("voce decidiu sair")
        break












    


   







    

    