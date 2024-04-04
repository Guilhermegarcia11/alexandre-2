print('Programa para calcular notas trimestrais.')

tri1 = float(input('Digite o primeiro trimestre'))
tri2 = float(input('Digite o segundo trimestre'))
tri3 = float(input('Digite o terceiro trimestre'))
media = (tri1 + tri2 + tri3)/3
if media < 40:
    print('Aluno reprovado e sua média é: {}'.format(media))
elif media >= 40 and media < 60:
    print('Aluno em recuperação e sua média é: {}'.format(media))
else:
    print('Aluno aprovado e sua média é: {}'.format(media))

print('Fim do programa.')
