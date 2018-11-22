# Tablcie w Py nazywa się też Listami

array = []
print(array)
array = [1, 2, 3]
print(array)

array.append(4)
array.append(5)
array.append(6)
print(array)

print(array[0])

for x in array:  # wypisze tylko elementy nieparzyste
    if x % 2 == 0:
        continue  # pozwala przeskoczyć 1 krok pętli
    print(x)

a1 = [2, 4, 6, 8]
a2 = [1, 3, 5, 7]

a12 = a1 + a2  # wsttawienie tablicy a2 zaraz za a1
print(a12)
print(3 * a1)  # tablica zawierająca elementy a1 ustawione 3 razy po sobie

# Set - zbiór, np. set = {1, 2, 3}

a12 = set(a1) | set(a2)  # | - suma zbiorów
print(a12)
a12 = set(a1) & set(a2)
print(a12)  # set() - zbiór pusty

a222 = [a2, a2, a2]  # tablica tablic
print(a222)

a3 = range(1, 11)  # liczby od 1 do 10
print(a3)

for n in a3:
    if n % 5:  # n % m jest prawdziwe dla reszt różnych od zera; równoważne n % m != 0
        print(n)

# Length
print(len(a3))
# działa też dla string'ów
s = "Kocham"
print(len(s))

a2 = [2, 4, 6, 8]  # ten sam zestaw, co w a1
print(a1 == a2)
print(a1 is a2)  # is jest True, gdy obydwie zmienne wskazują ten sam obszar pamieci komputera
a2 = a1
print(a1 == a2)
print(a1 is a2)