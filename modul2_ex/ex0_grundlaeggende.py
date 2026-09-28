"""
=============================================================
  MODUL 2  ·  Sprint 0  ·  Øvelse 0
  Grundlæggende: aritmetik, modulo og alfabetets indekstal
=============================================================
Før vi koder og afkoder hemmelige beskeder, skal vi forstå
de byggesten der bruges:

  1. Aritmetiske operatorer – inkl. heltalsdivision og modulo
  2. Modulo og "gå rundt" i alfabetet
  3. ord() og chr() – bogstaver som tal
  4. Afkod en besked skrevet med indekstal
=============================================================
"""

ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# ── Opgave 1 ──────────────────────────────────────────────
# Formål: bliv fortrolig med Pythons aritmetiske operatorer,
# særligt heltalsdivision (//) og modulo (%).
#
# Python har disse operatorer:
#   +   addition          5 + 3   = 8
#   -   subtraktion       5 - 3   = 2
#   *   multiplikation    5 * 3   = 15
#   /   division          5 / 2   = 2.5   (decimaltal)
#   //  heltalsdivision   5 // 2  = 2     (afrunder ned til helt tal)
#   %   modulo            5 % 2   = 1     (resten efter heltalsdivision)
#   **  eksponent         5 ** 2  = 25
#
# Erstat 0 med selve udtrykket – lad Python beregne resultatet.
# Eksempel: i stedet for  x = 8  skal du skrive  x = 5 + 3

def opgave1():
    # TODO: skriv udtrykket for 17 + 9
    a = 0

    # TODO: skriv udtrykket for 30 - 4
    b = 0

    # TODO: skriv udtrykket for 7 * 4
    c = 0

    # TODO: skriv udtrykket for 29 heltalsdivideret med 26  (//)
    # Hint: heltalsdivision giver kun den hele del – decimaler droppes
    d = 0

    # TODO: skriv udtrykket for resten af 29 divideret med 26  (%)
    # Hint: modulo giver det der bliver til overs efter heltalsdivision
    e = 0

    # TODO: skriv udtrykket for resten af 52 divideret med 26
    f = 0

    # TODO: skriv udtrykket for resten af 53 divideret med 26
    g = 0

    print("=== Opgave 1: Aritmetik ===")
    print(f"  17 + 9       = {a}")
    print(f"  30 - 4       = {b}")
    print(f"  7 * 4        = {c}")
    print(f"  29 // 26     = {d}   (hvor mange hele 26'ere går der i 29?)")
    print(f"  29 % 26      = {e}   (hvad er resten?)")
    print(f"  52 % 26      = {f}")
    print(f"  53 % 26      = {g}")


# ── Opgave 2 ──────────────────────────────────────────────
# Formål: forstå hvordan modulo holder os inden for alfabetets
# grænser (0–25) når vi skifter bogstaver frem eller tilbage.
#
# Alfabetet har 26 bogstaver med indeks 0–25:
#   A=0, B=1, C=2, ... Z=25
#
# Problem: vi er på Y (indeks 24) og vil 3 pladser frem.
#   24 + 3 = 27  ← ugyldigt! Der er kun indeks 0–25.
#
# Løsning: modulo med 26 sørger for at vi "går rundt":
#   (24 + 3) % 26 = 1  →  bogstav nr. 1 = B  ✓
#
# Beregn de nye indekser ved hjælp af modulo.
# Hint: negative tal virker også med modulo i Python – prøv det af.

def opgave2():
    # Vi er på Y (indeks 24) og vil 3 pladser FREM.
    # TODO: beregn det nye indeks med modulo
    frem = 0

    # Vi er på X (indeks 23) og vil 5 pladser FREM.
    # TODO: beregn det nye indeks med modulo
    frem2 = 0

    # Vi er på B (indeks 1) og vil 3 pladser TILBAGE.
    # TODO: beregn det nye indeks med modulo
    # Hint: modulo virker også for negative tal i Python
    tilbage = 0

    print("\n=== Opgave 2: Modulo og wrap-around ===")
    print(f"  Y(24) + 3 frem    → indeks {frem}  = bogstav {ALFABET[frem] if 0 <= frem < 26 else '?'}")
    print(f"  X(23) + 5 frem    → indeks {frem2} = bogstav {ALFABET[frem2] if 0 <= frem2 < 26 else '?'}")
    print(f"  B(1)  - 3 tilbage → indeks {tilbage} = bogstav {ALFABET[tilbage] if 0 <= tilbage < 26 else '?'}")


# ── Opgave 3 ──────────────────────────────────────────────
# Formål: lær at konvertere mellem bogstaver og tal med
# de indbyggede funktioner ord() og chr().
#
#   ord(tegn)  →  giver tegnets ASCII-tal  (fx ord('A') = 65)
#   chr(tal)   →  giver bogstavet for ASCII-tallet  (fx chr(65) = 'A')
#
# Fordi 'A'=65, 'B'=66, ..., 'Z'=90, gælder:
#   bogstavets indeks (0–25) = ord(bogstav) - ord('A')
#
# Implementer print_alfabet_tabel() der printer et sildeben:
# øverste række viser alle 26 bogstaver, nederste viser indekstallet.
#
# Forventet output:
#   A  B  C  D  E  F  ...  Z
#   0  1  2  3  4  5  ...  25
#
# Hint: range(26) giver tallene 0–25
# Hint: ' '.join(liste) sætter elementer sammen til én streng med mellemrum imellem

def print_alfabet_tabel():
    # TODO: print alle 26 bogstaver på én linje adskilt af mellemrum
    # TODO: print de tilsvarende indekstal (0–25) på næste linje
    pass


# ── Opgave 4 ──────────────────────────────────────────────
# Formål: øv konvertering fra indekstal til bogstaver – og
# afkod en besked der er skrevet udelukkende med tal.
#
# Hvert tal i beskeden er et indeks i alfabetet: 0=A, 1=B, ... 25=Z
# Tallene er adskilt med mellemrum.
#
# Implementer afkod_talbesked(besked) der læser beskeden og
# returnerer den tilsvarende tekst med store bogstaver.
#
# Hint: str.split() deler en streng op ved mellemrum og returnerer en liste
# Hint: int(s) konverterer en streng til et heltal
# Hint: et indeks kan omregnes til et bogstav med ord() og chr()

HEMMELIG_BESKED = "17 20 13 3 19 8 0 11 5 0 1 4 19 4 19"

def afkod_talbesked(besked):
    resultat = ""
    # TODO: gå igennem hvert tal i besked, konverter til bogstav og tilføj til resultat
    return resultat


# ─────────────────────────────────────────────────────────
def main():
    opgave1()
    opgave2()

    print("\n=== Opgave 3: Alfabetets indekstal ===")
    print_alfabet_tabel()

    print("\n=== Opgave 4: Afkod talbesked ===")
    print(f"  Kodet:   {HEMMELIG_BESKED}")
    klartekst = afkod_talbesked(HEMMELIG_BESKED)
    print(f"  Afkodet: {klartekst}")


main()
