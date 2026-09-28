"""
=============================================================
  MODUL 1  ·  Sprint 1  ·  Øvelse 1  — LØSNING
  Variabler & Datatyper
=============================================================
"""


# ── Opgave 1 ──────────────────────────────────────────────
kodeord  = "P@ssw0rd!"
laengde  = len(kodeord)
score    = 0.75
godkendt = True


# ── Opgave 2 ──────────────────────────────────────────────
def print_typer():
    print(f"  kodeord  : {type(kodeord)}")
    print(f"  laengde  : {type(laengde)}")
    print(f"  score    : {type(score)}")
    print(f"  godkendt : {type(godkendt)}")
    # isinstance(True, int) returnerer True fordi bool er en underklasse af int


# ── Opgave 3 ──────────────────────────────────────────────
def konverter_laengde(laengde_str):
    try:
        return int(laengde_str)
    except ValueError:
        return None


# ── Opgave 4 ──────────────────────────────────────────────
def bool_fra_tekst(tekst):
    t = tekst.lower()
    if t in ("true", "ja", "1"):
        return True
    elif t in ("false", "nej", "0"):
        return False
    return None


# ── Opgave 5 ──────────────────────────────────────────────
print(f"Kode: {kodeord}  |  Længde: {laengde}  |  Score: {score}  |  Godkendt: {godkendt}")


# ─────────────────────────────────────────────────────────
def main():
    print("=== Opgave 2: Typer ===")
    print_typer()

    print("\n=== Opgave 3: Konvertering ===")
    for s in ["12", "8", "ikke-et-tal", "", "0"]:
        print(f"  konverter_laengde({s!r}) = {konverter_laengde(s)}")

    print("\n=== Opgave 4: Bool fra tekst ===")
    for s in ["true", "False", "ja", "nej", "1", "0", "måske"]:
        print(f"  bool_fra_tekst({s!r}) = {bool_fra_tekst(s)}")


main()
