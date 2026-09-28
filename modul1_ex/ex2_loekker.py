"""
=============================================================
  MODUL 1  ·  Sprint 2  ·  Øvelse 2
  Løkker & Betingelser
=============================================================
En adgangskode analyseres tegn for tegn.
Vi klassificerer og tæller hver tegntype.

Tegnkategorier:
  "stort"    →  store bogstaver  (A-Z)
  "lille"    →  små bogstaver    (a-z)
  "ciffer"   →  tal              (0-9)
  "specielt" →  alt andet        (@ # ! $ % ...)

Din opgave: byg funktioner der gennemgår en adgangskode
og afgør om den lever op til minimumskravene.
=============================================================
"""

TESTLISTE = [
    "hej123",
    "P@ssw0rd!",
    "abc",
    "Administrator1",
    "qwerty",
    "Tr0ub4dor&3",
    "x",
    "Sommer2024!",
]


# ── Opgave 1 ──────────────────────────────────────────────
# Skriv klassificer_tegn(tegn) der returnerer én af:
#   "stort", "lille", "ciffer", "specielt"
#
# Hint: strenge har metoder der tjekker tegn-typen
#       (.isupper(), .islower(), .isdigit())

def klassificer_tegn(tegn):
    pass  # TODO


# ── Opgave 2 ──────────────────────────────────────────────
# Skriv tael_tegn(kodeord) der gennemgår hvert tegn med en for-løkke.
# Returnér en dict med antallet af hvert kategori, fx:
#   {'stort': 1, 'lille': 6, 'ciffer': 2, 'specielt': 1}
#
# Hint: kald klassificer_tegn() for hvert tegn
# Hint: start med denne dict og læg 1 til den rigtige nøgle:
#   antal = {'stort': 0, 'lille': 0, 'ciffer': 0, 'specielt': 0}

def tael_tegn(kodeord):
    antal = {'stort': 0, 'lille': 0, 'ciffer': 0, 'specielt': 0}
    pass  # TODO


# ── Opgave 3 ──────────────────────────────────────────────
# Skriv er_staerk(kodeord) der returnerer True
# hvis kodeordet opfylder ALLE fire krav:
#   - mindst 8 tegn
#   - mindst 1 stort bogstav
#   - mindst 1 ciffer
#   - mindst 1 specialtegn
#
# Hint: kald tael_tegn() og gem resultatet i en variabel

def er_staerk(kodeord):
    pass  # TODO


# ── Opgave 4 ──────────────────────────────────────────────
# Gennemgå TESTLISTE med en WHILE-løkke (ikke for).
# Returnér en ny liste med kun de kodeord der IKKE er stærke.
#
# Hint: while i < len(liste): ...

def find_svage(kodeord_liste):
    resultat = []
    i = 0
    # TODO: while-løkke der tilføjer svage kodeord til resultat
    return resultat


# ─────────────────────────────────────────────────────────
def main():
    print("=== Opgave 1: Klassificering af tegn ===")
    for tegn in ["A", "z", "5", "@", "!"]:
        print(f"  {tegn!r} → {klassificer_tegn(tegn)}")

    print("\n=== Opgave 2: Tæl tegn ===")
    for kode in ["P@ssw0rd!", "hej123"]:
        print(f"  {kode!r}: {tael_tegn(kode)}")

    print("\n=== Opgave 3: Er stærk? ===")
    for kode in TESTLISTE:
        print(f"  {kode:<22} → {er_staerk(kode)}")

    print("\n=== Opgave 4: Svage kodeord ===")
    svage = find_svage(TESTLISTE)
    for kode in svage:
        print(f"  {kode}")


main()
