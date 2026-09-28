"""
=============================================================
  MODUL 2  ·  Sprint 2  ·  Øvelse 2
  Monoalfabetisk substitution – afkod med given nøgle
=============================================================
En substitutionskode erstatter hvert bogstav med et fast andet
bogstav bestemt af en 26-tegns nøgle.

Nøgle:    DECKFMYIQJRWTZPXGNABUSOLVH
Alfabet:  ABCDEFGHIJKLMNOPQRSTUVWXYZ

For at AFKODE:
  Find cipher-bogstavet i nøglen → positionen = klartegnets plads i alfabetet.

  Eksempel: Cipher-bogstav D
    D er på position 0 i nøglen → position 0 i alfabetet = A  →  Klartegn: A
=============================================================
"""

ALFABET       = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NOEGLE        = "DECKFMYIQJRWTZPXGNABUSOLVH"
CHIFFERTEKST  = "Fz aueabqbubqpzarpkf fnabdbbfn isfnb epyabds tfk fb dzkfb. Mwdyfb fn: AUEAB_TFABFN"


# ── Opgave 1 ──────────────────────────────────────────────
# Implementer subst_afkod(tekst, noegle)
#
# For hvert bogstav i tekst:
#   1. Find tegnets position i noegle  (noegle.upper().index(tegn.upper()))
#   2. Slå op på den position i ALFABET  →  det er klartegnet
#   3. Bevar original case (isupper / islower)
#
# Hint: str.index(tegn) returnerer positionen for tegnet i strengen

def subst_afkod(tekst, noegle):
    resultat = ""
    for tegn in tekst:
        if tegn.isalpha():
            position = 0    # TODO: find tegnets position i noegle.upper()
            klartegn = "?"  # TODO: slå op på position i ALFABET
            if tegn.islower():
                klartegn = klartegn.lower()
            resultat += klartegn
        else:
            resultat += tegn
    return resultat


# ── Opgave 2 ──────────────────────────────────────────────
# Implementer subst_enkod(tekst, noegle) – det modsatte af afkod.
#
# For hvert bogstav i tekst:
#   1. Find tegnets position i ALFABET
#   2. Slå op på den position i noegle  →  det er cipher-tegnet
#   3. Bevar original case

def subst_enkod(tekst, noegle):
    resultat = ""
    for tegn in tekst:
        if tegn.isalpha():
            position = 0    # TODO: find tegnets position i ALFABET
            kryptegn = "?"  # TODO: slå op på position i noegle
            if tegn.islower():
                kryptegn = kryptegn.lower()
            resultat += kryptegn
        else:
            resultat += tegn
    return resultat


# ── Opgave 3 ──────────────────────────────────────────────
# Tilføj en sanity-check i funktionen nedenfor.
# Logik: enkod et testord og afkod det igen – du skal få det originale ord tilbage.
#
# Hint: subst_afkod(subst_enkod(TESTORD, noegle), noegle) == TESTORD

def sanity_check(noegle):
    testord = "HEMMELIG"
    enkod   = subst_enkod(testord, noegle)
    afkod   = subst_afkod(enkod, noegle)
    # TODO: print "Sanity-check OK" hvis afkod == testord, ellers print en fejlbesked
    pass


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
