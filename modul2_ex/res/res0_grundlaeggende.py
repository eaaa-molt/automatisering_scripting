"""
=============================================================
  MODUL 2  ·  Sprint 0  ·  Øvelse 0  — LØSNING
  Grundlæggende: aritmetik, modulo og alfabetets indekstal
=============================================================
"""

ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# ── Opgave 1 ──────────────────────────────────────────────
def opgave1():
    a = 17 + 9
    b = 30 - 4
    c = 7 * 4
    d = 29 // 26
    e = 29 % 26
    f = 52 % 26
    g = 53 % 26

    print("=== Opgave 1: Aritmetik ===")
    print(f"  17 + 9       = {a}")
    print(f"  30 - 4       = {b}")
    print(f"  7 * 4        = {c}")
    print(f"  29 // 26     = {d}   (hvor mange hele 26'ere går der i 29?)")
    print(f"  29 % 26      = {e}   (hvad er resten?)")
    print(f"  52 % 26      = {f}")
    print(f"  53 % 26      = {g}")


# ── Opgave 2 ──────────────────────────────────────────────
def opgave2():
    frem    = (24 + 3) % 26   # 1 → B
    frem2   = (23 + 5) % 26   # 2 → C
    tilbage = (1 - 3) % 26    # 24 → Y

    print("\n=== Opgave 2: Modulo og wrap-around ===")
    print(f"  Y(24) + 3 pladser frem  → indeks {frem}  = {ALFABET[frem]}")
    print(f"  X(23) + 5 pladser frem  → indeks {frem2} = {ALFABET[frem2]}")
    print(f"  B(1)  - 3 pladser tilbage → indeks {tilbage} = {ALFABET[tilbage]}")


# ── Opgave 3 ──────────────────────────────────────────────
def print_alfabet_tabel():
    bogstaver = []
    indekstal = []
    for i in range(26):
        bogstaver.append(chr(i + ord('A')))
        indekstal.append(f"{i:<2}")
    print('  '.join(bogstaver))
    print(' '.join(indekstal))
    print(indekstal)

# ── Opgave 4 ──────────────────────────────────────────────
HEMMELIG_BESKED = "17 20 13 3 19 8 0 11 5 0 1 4 19 4 19"

def afkod_talbesked(besked):
    resultat = ""
    for tal in besked.split():
        resultat += chr(int(tal) + ord('A'))
        resultat += " "
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
