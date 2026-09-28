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

MAPPE = Path(__file__).parent.parent


def vis_brugere():
    try:
        with open(MAPPE / "brugere.csv", encoding="utf-8") as f:
            for raekke in csv.DictReader(f):
                print(f"{raekke['navn']} — {raekke['afdeling']}")
    except FileNotFoundError:
        print("Filen 'brugere.csv' blev ikke fundet.")


def tael_pr_afdeling():
    tael = {}
    try:
        with open(MAPPE / "brugere.csv", encoding="utf-8") as f:
            for raekke in csv.DictReader(f):
                afd = raekke["afdeling"]
                tael[afd] = tael.get(afd, 0) + 1
    except FileNotFoundError:
        print("Filen 'brugere.csv' blev ikke fundet.")
        return
    for afd, antal in tael.items():
        print(f"{afd}: {antal}")


def gem_aktive(filnavn):
    aktive = []
    try:
        with open(MAPPE / "brugere.csv", encoding="utf-8") as f:
            for raekke in csv.DictReader(f):
                if raekke["aktiv"] == "True":
                    aktive.append(raekke["navn"])
    except FileNotFoundError:
        print("Filen 'brugere.csv' blev ikke fundet.")
        return
    with open(filnavn, "w", encoding="utf-8") as f:
        for navn in aktive:
            f.write(navn + "\n")


def list_filer():
    for fil in sorted(MAPPE.glob("*.py")):
        print(f"{fil.name:<30} {fil.stat().st_size} bytes")


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
