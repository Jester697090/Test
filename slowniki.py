pacjenci = {}

pacjenci["Kowalski"] = 22
pacjenci["Nowak"] = 25
pacjenci["Gomółka"] = 18

print(pacjenci)

for nazwisko in pacjenci:
    print("Pacjent %s ma %d lat." % (nazwisko, pacjenci[nazwisko]))  # przeszukiwanie słowników

pacjenci["Gozarski"] = 23  # dodaj
del pacjenci["Kowalski"]  # usuń

print(pacjenci)

pacjenci.pop("Gomółka")  # usuń

print(pacjenci)
