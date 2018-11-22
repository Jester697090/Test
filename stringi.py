s = "Some string"

print(s)
print(s.index('S'))  # indeks pierwszego wystąpienia 'S'
print(s.count('s'))  # ile 's' występuje w s
print(s[5:11])  # znaki na miejscach od 5 do 11
print(s[:4])  # znaki od początku do 4
print(s[5:])  # znaki od 5 do końca
print(s[::])  # równoważne print(s)
print(s[-1])  # indeksy ujemne liczone są od końca; ostatni to -1

print(s.upper())  # wielkie litery
print(s.lower())  # małe litery
print(s.startswith("Some"))
print(s.endswith("g"))

charArray = s.split(" ")
print(charArray)

# Metoda format (do str)

imie = "Harry"
nazwisko = "Potter"
ile = 23
print("Nazywam się {0} {1} i zarobiłem {2} mln dolarów.".format(imie, nazwisko, ile))
print("Nazywam się {} {} i zarobiłem {} mln dolarów.".format(imie, nazwisko, ile))  # numery są opcjonalne
print(f"Nazywam się {imie} {nazwisko} i zarobiłem {ile} mln dolarów.")  # można dodać 'f' i nazwać zmienne

# wypełnia podkreślnikami (_) wycentrowany tekst
# (^) do 11 szerokości '___hello___' (11 to 3 binarnie, 3 podkreślniki ???)
print('{0:_^11}'.format('hello'))  # może się przydać

# Print bez \n (znaku nowej linii)

print('a', end='')
print('b', end='')