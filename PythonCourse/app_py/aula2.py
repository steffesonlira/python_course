a = int(input('Entre com o primeiro valor:'))
b = int(input('Entre com o segundo valor:'))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('soma: {som}. '
      '\nsubtracao: {sub}.'
      ' \nMultiplicação: {mult}. '
      '\nDivisão: {div}. '
      '\nResto {rest}'.format(som=soma,
                              sub=subtracao,
                              mult=multiplicacao,
                              rest=resto,
                              div=divisao))
print(resultado)

