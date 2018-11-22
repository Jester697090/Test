from functools import partial

def dzielenie(da, dk, **opcje):  # przekazanie opcji za pomocą słów-kluczy
    if opcje.get("tryb") == "dziel":
        print("Dzielę %d przez %d..." % (da, dk))
        w = da / dk
    elif opcje.get("tryb") == "mod":
        print("Obliczam resztę z dzielenia %d przez %d..." % (da, dk))
        w = da % dk
    else:
        print("Wybierz obsługiwany 'tryb': 'dziel' - zwykłe dzielenie, 'mod' - reszta z dzielenia")
        return

    if opcje.get("wyswietl") == "nie":
        return w
    else:
        print("Wynik = %f" % w)

dzielenie_zwykle = partial(dzielenie, tryb = "dziel", wyswietl = "nie")

dzielna = 20
dzielnik = 5
wynik = dzielenie_zwykle(dzielna, dzielnik)

# print(wynik)