# Napisz program, który wczyta od użytkownika zdanie. Wypisz z niego wszystkie litery w kolejności
# alfabetycznej, a następnie wypisze których litera alfabetu nie zawiera.

alfabet = list('abcdefghijklmnopqrstuvwxyz')
zdanie = input("Podaj zdanie: ")
zdanie_format = list(zdanie)

nowe_z_f = [i for i in zdanie_format if not isinstance(i, str) or not i.isdigit()]
if ' ' in nowe_z_f:
    nowe_z_f.remove(' ')

nowe_z_f.sort()
print(nowe_z_f, "\n")

pobierz_litery = {z for z in zdanie if z.isalpha()}
brakujace = [a for a in alfabet if a not in pobierz_litery]

print(brakujace)





