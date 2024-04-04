print("Programa para calcular o fatorial.")
numero = int(input("Digite um número."))
cont = numero

while(cont > 1):
    fatorial = numero * (cont - 1)
    cont -= 1
print("O fatorial de {} é: {}".format(numero, fatorial))