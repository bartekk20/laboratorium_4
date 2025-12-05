stopnie = (
    "Szeregowy",
    "Kapral",
    "Sierżant",
    "Porucznik",
    "Kapitan",
    "Major",
    "Pułkownik",
)

ilość_stopnii = len(stopnie)

Major_index = stopnie.index("Major")

Pułkownik_występowanie = "Pułkownik" in stopnie

print("Liczba stopni:", ilość_stopnii)
print("Indeks stopnia Major:", Major_index)
print("Czy 'Pułkownik' znajduje się w krotce?:", Pułkownik_występowanie)
