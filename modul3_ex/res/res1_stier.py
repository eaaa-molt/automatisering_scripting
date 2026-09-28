"""
=============================================================
  MODUL 3  ·  Sprint 1  ·  Øvelse 1
  Stier og tekstfiler
=============================================================
Python kan arbejde med filer på din computer.
For at finde de rigtige filer skal vi bruge filstier.

  MAPPE = Path(__file__).parent

Denne linje giver os stien til mappen scriptet ligger i.
Vi bruger den til at finde andre filer i samme mappe — det
gør scriptet robust uanset hvor på computeren det kører.

I denne øvelse lærer vi at skrive til og læse fra tekstfiler.
=============================================================
"""

from pathlib import Path

MAPPE = Path(__file__).parent.parent


# ── Eksperimenter ─────────────────────────────────────────
# Kør disse linjer én ad gangen og observer outputtet.
# Fjern # for at aktivere:
#
# Eksperiment 1: Hvad er MAPPE?
#   print(MAPPE)
#
# Eksperiment 2: Eksisterer mappen?
#   print(MAPPE.exists())
#
# Eksperiment 3: Hvad er der i mappen?
#   for f in MAPPE.iterdir():
#       print(f.name)
#
# Eksperiment 4: Byg en filsti med /
#   fil = MAPPE / "test.txt"
#   print(fil)
#   print(fil.exists())   # eksisterer filen endnu?
# ─────────────────────────────────────────────────────────


def skriv_navne():
    navne = [
        "Anna Jensen",
        "Bjarne Nielsen",
        "Cecilie Hansen",
        "Diana Larsen",
        "Esben Madsen",
    ]
    with open(MAPPE / "navne.txt", "w", encoding="utf-8") as f:
        for navn in navne:
            f.write(navn + "\n")


def vis_navne():
    with open(MAPPE / "navne.txt", "r", encoding="utf-8") as f:
        for linje in f:
            print(linje.strip())


def taеl_navne():
    antal = 0
    with open(MAPPE / "navne.txt", "r", encoding="utf-8") as f:
        for linje in f:
            if linje.strip():
                antal += 1
    print(f"Antal navne: {antal}")


def tilfoej_navne():
    nye_navne = ["Freja Olsen", "Gorm Poulsen"]
    with open(MAPPE / "navne.txt", "a", encoding="utf-8") as f:
        for navn in nye_navne:
            f.write(navn + "\n")


def soeg_i_fil(soegeord):
    fundet = []
    with open(MAPPE / "navne.txt", "r", encoding="utf-8") as f:
        for linje in f:
            if soegeord in linje:
                fundet.append(linje.strip())
    if fundet:
        for navn in fundet:
            print(f"Fundet: {navn}")
    else:
        print(f"Ingen navne indeholder '{soegeord}'")


# ─────────────────────────────────────────────────────────
def main():
    print("── Opgave 1: skriv navne ──")
    skriv_navne()
    print("Skrevet til navne.txt\n")

    print("── Opgave 2: vis navne ──")
    vis_navne()

    print("\n── Opgave 3: tæl navne ──")
    taеl_navne()

    print("\n── Opgave 4: tilføj navne ──")
    tilfoej_navne()
    taеl_navne()   # forventet: 7

    print("\n── Opgave 5: søg ──")
    soeg_i_fil("Nielsen")
    soeg_i_fil("Hansen")
    soeg_i_fil("Mortensen")   # ingen match


if __name__ == "__main__":
    main()
