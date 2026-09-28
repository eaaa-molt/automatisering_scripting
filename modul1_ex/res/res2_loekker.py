"""
=============================================================
  MODUL 1  ·  Sprint 2  ·  Øvelse 2  — LØSNING
  Løkker & Betingelser
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
def klassificer_tegn(tegn):
    if tegn.isupper():
        return "stort"
    elif tegn.islower():
        return "lille"
    elif tegn.isdigit():
        return "ciffer"
    else:
        return "specielt"


# ── Opgave 2 ──────────────────────────────────────────────
def tael_tegn(kodeord):
    antal = {'stort': 0, 'lille': 0, 'ciffer': 0, 'specielt': 0}
    for tegn in kodeord:
        kategori = klassificer_tegn(tegn)
        antal[kategori] += 1
    return antal


# ── Opgave 3 ──────────────────────────────────────────────
def er_staerk(kodeord):
    antal = tael_tegn(kodeord)
    return (len(kodeord) >= 8 and
            antal['stort'] >= 1 and
            antal['ciffer'] >= 1 and
            antal['specielt'] >= 1)


# ── Opgave 4 ──────────────────────────────────────────────
def find_svage(kodeord_liste):
    resultat = []
    i = 0
    while i < len(kodeord_liste):
        if not er_staerk(kodeord_liste[i]):
            resultat.append(kodeord_liste[i])
        i += 1
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
