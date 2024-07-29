def obter_numero():#função para obter um numero para verificar se é par
    while True:
        try:
            numero = int(input("Digite um número para verificar se é par ou ímpar: "))
            return numero
        except ValueError:
            print("Por favor digite um número inteiro.")

def obter_numero2():#função para obter um numero para verificar o fatorial
    while True:
        try:
            numero2 = int(input("Digite um número para descobrirmos o fatorial: "))
            return numero2
        except ValueError:
            print("Por favor digite um número inteiro.")

def verifica_par(numero):#função para verificar se o número inserido é par
    if numero % 2 == 0:
        print(numero, "é par")
    else:
        print(numero, "é ímpar")

def fatorial(numero2):#função para verificar o fatorial do número inserido 
    if numero2 <=1:
        return 1
    else:
        return numero2 *fatorial(numero2-1)


numero = obter_numero()
numero2 = obter_numero2()
verifica_par(numero)


resultado_fatorial = fatorial(numero2)
print(f"O fatorial de {numero2} é {resultado_fatorial}")
