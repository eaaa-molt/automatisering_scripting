"""
=============================================================
  MODUL 3  ·  Sprint 2  ·  Øvelse 2
  CSV-filer
=============================================================
CSV (Comma-Separated Values) er et tekstformat til tabel-data.
En CSV-fil ser sådan ud:

  navn,email,afdeling,aktiv
  Anna Jensen,anna@firma.dk,IT,True
  Bjarne Nielsen,bjarne@firma.dk,HR,True

Den første linje er kolonnenavne (header).
De følgende linjer er data — én række per linje.

Python's csv-modul har to nyttige klasser:
  csv.DictReader  →  læs rækker som ordbøger (nøgle = kolonnenavn)
  csv.DictWriter  →  skriv rækker fra ordbøger

Datafilen brugere.csv ligger i samme mappe som scriptet.
=============================================================
"""

import csv
from pathlib import Path

MAPPE = Path(__file__).parent.parent


# ── Eksperimenter ─────────────────────────────────────────
# Kør disse linjer og observer outputtet.
# Fjern # for at aktivere:
#
# Eksperiment 1: Læs den første række
#   with open(MAPPE / "brugere.csv", encoding="utf-8") as f:
#       laeseren = csv.DictReader(f)
#       raekke = next(laeseren)       # hent første række
#       print(raekke)                 # hvad er typen?
#       print(raekke["navn"])         # adgang via kolonnenavn
#
# Eksperiment 2: Se kolonnenavnene (fieldnames)
#   with open(MAPPE / "brugere.csv", encoding="utf-8") as f:
#       laeseren = csv.DictReader(f)
#       print(laeseren.fieldnames)    # hvad returnerer dette?
# ─────────────────────────────────────────────────────────


def vis_alle_brugere():
    with open(MAPPE / "brugere.csv", encoding="utf-8") as f:
        laeseren = csv.DictReader(f)
        for raekke in laeseren:
            print(f"{raekke['navn']} — {raekke['afdeling']}")


def tael_pr_afdeling():
    afdelinger = []
    with open(MAPPE / "brugere.csv", encoding="utf-8") as f:
        laeseren = csv.DictReader(f)
        for raekke in laeseren:
            afdelinger.append(raekke["afdeling"])

    tael = {}
    for afd in afdelinger:
        if afd not in tael:
            tael[afd] = 0
        tael[afd] += 1

    for afd, antal in tael.items():
        print(f"{afd}: {antal}")


def filtrer_til_csv():
    aktive_it = []
    with open(MAPPE / "brugere.csv", encoding="utf-8") as f:
        laeseren = csv.DictReader(f)
        feltnavne = laeseren.fieldnames
        for raekke in laeseren:
            if raekke["afdeling"] == "IT" and raekke["aktiv"] == "True":
                aktive_it.append(raekke)
    with open(MAPPE / "it_aktive.csv", "w", newline="", encoding="utf-8") as f:
        skriveren = csv.DictWriter(f, fieldnames=feltnavne)
        skriveren.writeheader()
        skriveren.writerows(aktive_it)


def verificer_csv():
    with open(MAPPE / "it_aktive.csv", encoding="utf-8") as f:
        laeseren = csv.DictReader(f)
        raekker = list(laeseren)
    print(f"Aktive IT-brugere: {len(raekker)}")
    for raekke in raekker:
        print(raekke["navn"])


# ─────────────────────────────────────────────────────────
def main():
    print("── Opgave 1: vis alle brugere ──")
    vis_alle_brugere()

    print("\n── Opgave 2: tæl pr. afdeling ──")
    tael_pr_afdeling()

    print("\n── Opgave 3: filtrer til CSV ──")
    filtrer_til_csv()
    print("Skrevet til it_aktive.csv")

    print("\n── Opgave 4: verificér ──")
    verificer_csv()


if __name__ == "__main__":
    main()
