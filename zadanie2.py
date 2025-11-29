lista = ["Ania", "Jan", "Władysław", "Tadeusz"]
print(lista, "\n")
lista.sort()
print(lista)

# lista.append("Krzysztof", "Prometeusz")
# print(lista)

lista.extend(["Krzysztof", "Prometeusz"])
print(lista)

print(lista.pop())

lista.insert(2, "Kazik")
print(lista)
print("\n----------------------")

nowa_lista = lista.copy()
print(nowa_lista)