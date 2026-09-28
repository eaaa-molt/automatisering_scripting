"""
=============================================================
  MODUL 3  ·  Sprint 4  ·  Øvelse 4
  Samlet øvelse
=============================================================
Bring trådene fra sprint 1-3 sammen i ét menu-drevet script.

Du bruger:
  - pathlib / MAPPE (sprint 1)
  - csv.DictReader / csv.DictWriter (sprint 2)
  - try/except fejlhåndtering (sprint 3)

Datafilen brugere.csv ligger i samme mappe som scriptet.

Menuen:
  1) Vis alle brugere (navn + afdeling)
  2) Tæl brugere pr. afdeling
  3) Gem aktive brugere til aktive_brugere.txt
  4) List alle .py-filer i mappen
  q) Afslut
=============================================================
"""

import csv
from pathlib import Path

MAPPE = Path(__file__).parent


# ── Opgave 1 ──────────────────────────────────────────────
# Implementer vis_brugere()
# Læs brugere.csv og print navn og afdeling for hver bruger.
# Brug try/except FileNotFoundError — print en besked hvis
# filen mangler.
#
# Forventet output (uddrag):
#   Anna Jensen — IT
#   Bjarne Nielsen — HR

def vis_brugere():
    # TODO: åbn brugere.csv med try/except FileNotFoundError
    # TODO: brug csv.DictReader og print navn + afdeling
    pass


# ── Opgave 2 ──────────────────────────────────────────────
# Implementer tael_pr_afdeling()
# Tæl brugere pr. afdeling og print oversigten.
# Brug try/except FileNotFoundError.
#
# Forventet output (rækkefølge kan variere):
#   IT: 5
#   HR: 3
#   Økonomi: 2

def tael_pr_afdeling():
    # TODO: læs brugere.csv med try/except FileNotFoundError
    # TODO: tæl med en ordbog (dict.get(noegle, 0))
    # TODO: print oversigten
    pass


# ── Opgave 3 ──────────────────────────────────────────────
# Implementer gem_aktive(filnavn)
# Læs brugere.csv og skriv kun de aktive brugeres navne
# til en tekstfil (ét navn per linje).
# Brug try/except FileNotFoundError ved læsning.
#
# Hint: aktiv == "True" (streng, ikke bool)
#
# Forventet indhold af filen:
#   Anna Jensen
#   Bjarne Nielsen
#   ...  (alle med aktiv == "True")

def gem_aktive(filnavn):
    # TODO: læs brugere.csv med try/except FileNotFoundError
    # TODO: saml navnene på aktive brugere i en liste
    # TODO: skriv navnene til filnavn med open(..., "w")
    pass


# ── Opgave 4 ──────────────────────────────────────────────
# Implementer list_filer()
# Find og print alle .py-filer i MAPPE med filnavn og størrelse.
#
# Hint: MAPPE.glob("*.py") returnerer alle .py-filer
# Hint: fil.stat().st_size giver størrelsen i bytes

def list_filer():
    # TODO: brug MAPPE.glob("*.py") og print filnavn + størrelse
    pass


# ─────────────────────────────────────────────────────────
def main():
    print("Bruger-værktøj")
    print("─" * 32)

    while True:
        print("\n1) Vis alle brugere")
        print("2) Tæl pr. afdeling")
        print("3) Gem aktive brugere til aktive_brugere.txt")
        print("4) List .py-filer i mappen")
        print("q) Afslut")
        valg = input("\nDit valg: ").strip().lower()

        if valg == "q":
            break
        elif valg == "1":
            vis_brugere()
        elif valg == "2":
            tael_pr_afdeling()
        elif valg == "3":
            gem_aktive(MAPPE / "aktive_brugere.txt")
            print("Gemt til aktive_brugere.txt")
        elif valg == "4":
            list_filer()


if __name__ == "__main__":
    main()
