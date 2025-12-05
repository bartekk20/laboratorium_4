zakupy = {
    "Bułka": 0.90,
    "Chleb": 6.00,
    "Jajka": 12.00,
    "Masło": 10.00,
    "Krokiety": 8.00
}

print("Lista zakupów: ")
for artykul, kwota in zakupy.items():
    print(artykul + " - " + str(kwota) + " zł")

suma = sum(zakupy.values())
print("Suma:", str(suma) + "zł")

