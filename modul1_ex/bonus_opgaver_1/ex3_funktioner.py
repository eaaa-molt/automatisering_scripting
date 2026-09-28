# Modul 1 – Sprint 3: Funktioner
# -------------------------------------------------------
# Øvelse: Pak logikken fra ex2 ind i navngivne funktioner
#         med ét ansvar hver. Test dem fra __main__.

def filtrer_store(tal, graense):
    """Returnerer en liste med kun de tal der er over grænsen."""
    store = []
    for t in tal:
        if t > graense:
            store.append(t)
    return store


def beregn_sum(tal):
    """Returnerer summen af alle tal i listen."""
    total = 0
    for t in tal:
        total += t
    return total


def find_stoerste(tal):
    """Returnerer det største tal i listen uden at bruge max()."""
    if not tal:
        return None
    stoerste = tal[0]
    for t in tal:
        if t > stoerste:
            stoerste = t
    return stoerste


# Test funktionerne
tal = [4, 15, 8, 23, 1, 17, 6, 11, 3, 19]

store_tal = filtrer_store(tal, 10)
print("Tal større end 10:", store_tal)

total = beregn_sum(tal)
print("Sum af alle tal:  ", total)

stoerste = find_stoerste(tal)
print("Største tal:      ", stoerste)

# Opgave:
# 1. Skriv funktionen 'filtrer_store' selv fra bunden
# 2. Skriv en funktion 'beregn_gennemsnit(tal)' der bruger beregn_sum()
# 3. Hvad returnerer filtrer_store([]) ? Og hvad returnerer find_stoerste([]) ?
