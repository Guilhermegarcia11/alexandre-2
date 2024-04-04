print("calculadora")

while True:
    try:
        v1 = float(input('entre com o primeiro numero'))
        v2 = float(input('entre com o segundo numero'))
        op = input('digite = para a somar, - para subtrair, * para multiplicar, /para dividir ou s para sair.')

        if op == '+':
            resultado = v1 + v2
        elif op == '-':
            resultado = v1 - v2
        elif op == '*':
            resultado = v1 * v2
        elif op == '/':
            resultado = v1 / v2
        elif op.upper() == 's':
            break
        else:
            print('valor invalido.')
            continue
    except:
        continue
        print('voce digitou um valor invalido.')
    print('a operaçao escolhida foi {} e o resultado foi {} '.format(op,resultado))