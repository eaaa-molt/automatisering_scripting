"""
=============================================================
  MODUL 2  ·  Sprint 2  ·  Øvelse 2  — LØSNING
  Monoalfabetisk substitution – afkod med given nøgle
=============================================================
"""

ALFABET       = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NOEGLE        = "DECKFMYIQJRWTZPXGNABUSOLVH"
CHIFFERTEKST  = "P shifypualu hm oqlyaly ly kla prrl klu obyapnzal clq, tlu klu kly møslz zvt oqlt, kly møyly kpn aps klu lulzal. Mvy uåy zaqlyulyul ocpzrly kpa uhcu, clk kb, ha éu zqæs ohy sfaala olsl apklu. Shk tpn ahnl tlk kpn wå kpu ylqzl mvy kb ly MPYL{Tpu-Lulzal-Lul}"


# ── Opgave 1 ──────────────────────────────────────────────
def subst_afkod(tekst, noegle):
    resultat = ""
    for tegn in tekst:
        if tegn.isalpha():
            position = noegle.upper().index(tegn.upper())
            klartegn = ALFABET[position]
            if tegn.islower():
                klartegn = klartegn.lower()
            resultat += klartegn
        else:
            resultat += tegn
    return resultat


# ── Opgave 2 ──────────────────────────────────────────────
def subst_enkod(tekst, noegle):
    resultat = ""
    for tegn in tekst:
        if tegn.isalpha():
            position = ALFABET.index(tegn.upper())
            kryptegn = noegle[position]
            if tegn.islower():
                kryptegn = kryptegn.lower()
            resultat += kryptegn
        else:
            resultat += tegn
    return resultat


# ── Opgave 3 ──────────────────────────────────────────────
def sanity_check(noegle):
    testord = "HEMMELIG"
    enkod   = subst_enkod(testord, noegle)
    afkod   = subst_afkod(enkod, noegle)
    if afkod == testord:
        print("Sanity-check OK")
    else:
        print(f"FEJL – forventede {testord!r}, fik {afkod!r}")


# ─────────────────────────────────────────────────────────
def main():
    print("Nøgle:       ", NOEGLE)
    print("Chiffertekst:", CHIFFERTEKST)
    print()

    klartekst = subst_afkod(CHIFFERTEKST, NOEGLE)
    print("Afkodet tekst:")
    print(klartekst)
    print()

    sanity_check(NOEGLE)


main()
