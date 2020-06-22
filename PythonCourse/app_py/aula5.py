lista = [3, 19, 2, 17]
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

lista_animais[0] = 'macaco'
print(lista_animais)

tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animais))
tupla_animal = tuple(lista_animais)
print(type(tupla_animal))
print(tupla_animal)
lista_numetica = list(tupla)
print(type(lista_numetica))
lista_numetica[0] = 100
print(lista_numetica)

# print(lista_animais[1])
#
# nova_lista = lista_animais * 3
# print(nova_lista)

# lista.sort()
# lista_animais.sort()
# print(lista)
# print(lista_animais)
# lista_animais.reverse()
# print(lista_animais)

# if 'lobo' in lista_animais:
#     print('Existe um gato na lista')
# else:
#     print('Não existe um gato na lista. Será incluído.')
#     lista_animais.append('lobo')
#     print(lista_animais)


# lista_animais.pop(1)
# print(lista_animais)

# lista_animais.remove('elefante')
# print(lista_animais)
