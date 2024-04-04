print("Programa para verificar ano bissexto")
ano = int(input("Digite o ano."))
if(ano%400 == 0 or ano%4 == 0 and ano%100 != 0):
    print("{} é  ano bissexto.".format(ano))
else:
    print("{} não é ano bissexto.".format(ano))

print('Fim do programa.')