def normaliser(tekst):
    tekst = tekst.lower()
    for fra, til in [("æ","ae"),("ø","oe"),("å","aa")]:
        tekst = tekst.replace(fra, til)
    return tekst

def brugernavn(fornavn, efternavn):
    f = normaliser(fornavn)
    e = normaliser(efternavn)
    return f"{f}.{e}"

print(normaliser("Møltorp"))