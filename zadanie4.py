# Napisz program, który wczyta od użytkownika zdanie. Wypisz z niego wszystkie litery w kolejności
# alfabetycznej, a następnie wypisze których litera alfabetu nie zawiera.


zdanie = input("Podaj zdanie: ")

zdanie_format = list(zdanie)
print(zdanie_format)

nowe_z_f = [i for i in zdanie_format if not isinstance(i, str) or not i.isdigit()]
zdanie_format.sort()
zdanie_format.remove(' ')

alfabet = list('abcdefghijklmnopqrstuvwxyz')


