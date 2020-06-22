a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Segundo Bimestre: '))
media = (a + b + c + d) / 4
print('media: {}' .format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <=10:
#     print('media: {}'.format(media))
# else:
#     print('Foi infomrada uma nota errada')

# a = int(input('Entre com o primeiro Valor: '))
# b = int(input('Entre com o segundo Valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or  not resto_b > 0:
#     print('foi digitado um numero par')
# else:
#     print('Nenhum número par foi digitado')


# a = int(input('Primeiro Valor: '))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro Valor: '))
# if a > b and a > c:
#     print('O maior numero é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('o maior número é {}' .format(c))
# print('Final do programa')
