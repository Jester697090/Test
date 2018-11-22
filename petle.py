# Range - zamiast tradycyjnych iteratorów

for n in range(5):  # od 0 do 4 (bez 5)
    print(n)

for n in range(0, -5, -1):  # od 0 do -4 (bez -5)
    print(n)

for n in range(0, 101, 10):  # od 0 do 100 ze skokiem co 10
    print(n)

# Break i continue

n = 0
while True:
    n += 1

    if n >= 5:
        print(n)
        break  # zatrzyma pętlę

for n in range(5):
    if n % 2 != 1:
        continue  # przejdzie od razu do następnego kroku pętli
    print(n)
