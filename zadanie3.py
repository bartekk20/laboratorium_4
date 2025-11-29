# zad 3
# Napisz program, który:
# a. Wczyta (zmienną) imię oraz wyświetli tekst „Witaj” oraz wczytane imię.
# b. Wczyta (zmienną) wiek oraz wyświetli tekst „Twój wiek to:” oraz wczytany wiek.
# c. Wczyta (zmienne) imię i nazwisko i wyświetli inicjały.
# d. Wczyta łańcuch i wyświetli go pięć razy.
# e. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta połączone te dwa łańcuchy.
# f. Wczyta dwa łańcuchy, a w trzecim łańcuchu zapamięta pierwszą połowę pierwszego i drugą połowę
# drugiego.




# imię = input("Podaj swoje imie: ")
# print("Witaj " + imię)

# wiek = (input("Podaj swój wiek: "))
# print("Twój wiek to:" + wiek)

# imie1 = input("Podaj swoje imie: ")
# nazwisko1 = input("Podaj swoje nazwisko: ")

# print("Twoje inicjały to: " + imie1[0].capitalize() + nazwisko1[0].capitalize())

lancuch1 = [1,2,3,4,5,6,7,8,9,10]
lancuch2 = [11,12,13,14,15,16,17,18,19,20]
lancuch3 = lancuch1 + lancuch2
print(lancuch1 * 5)
print("\n")
print(lancuch3)

dlugosc_lanuch_1 = len(lancuch1) // 2
lanuch4 = lancuch1[:dlugosc_lanuch_1] + lancuch2[dlugosc_lanuch_1:]
print(lanuch4)


