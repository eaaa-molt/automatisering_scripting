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

MAPPE = Path(__file__).parent


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


# ── Opgave 1 ──────────────────────────────────────────────
# Læs alle rækker fra brugere.csv og print navn og afdeling
# for hver bruger.
#
# Fremgangsmåde:
#   1. Åbn filen med open(..., encoding="utf-8")
#   2. Opret en csv.DictReader og gå rækkerne igennem
#   3. Print navn og afdeling for hver række
#
# Forventet output (første to linjer):
#   Anna Jensen — IT
#   Bjarne Nielsen — HR

def vis_alle_brugere():
    with open (MAPPE / "brugere.csv", encoding="UTF-8") as f:
        brugerordbog = csv.DictReader(f)
        print(brugerordbog)
        for række in brugerordbog:
            navn     = række["navn"]
            afdeling = række["afdeling"]
            aktiv    = række["aktiv"] == "True"  # streng → bool
            print(f"{navn:^20} — {afdeling:^30} — {aktiv}")





    # TODO: åbn brugere.csv og opret en csv.DictReader
    # TODO: gå rækkerne igennem med en for-løkke
    # TODO: print navn og afdeling for hver række
    pass


# ── Opgave 2 ──────────────────────────────────────────────
# Tæl hvor mange brugere der er i hver afdeling.
# Print resultatet som en oversigt.
#
# Hint: brug en ordbog til at holde styr på tællingen.
#       For hvert afdelingsnavn: øg tælleren med 1.
#       Brug dict.get(noegle, 0) for at starte fra 0.
#
# Forventet output (rækkefølge kan variere):
#   IT: 5
#   HR: 3
#   Økonomi: 2

def tael_pr_afdeling():
    tael = {}
    # TODO: åbn brugere.csv og gå rækkerne igennem
    # TODO: for hver række: opdater tael[afdeling] med +1
    # TODO: print oversigten
    pass


# ── Opgave 3 ──────────────────────────────────────────────
# Filtrer brugere.csv og skriv kun aktive IT-brugere til
# en ny fil: it_aktive.csv
#
# Fremgangsmåde:
#   1. Læs alle rækker fra brugere.csv
#   2. Behold kun dem hvor afdeling == "IT" og aktiv == "True"
#      Bemærk: "aktiv" er en streng i CSV — ikke en bool!
#   3. Skriv de filtrerede rækker til it_aktive.csv med DictWriter
#      Brug de samme kolonnenavne (fieldnames) som originalen
#      Husk writeheader() og newline="" i open()
#
# Hint: få kolonnenavnene fra laeseren.fieldnames

def filtrer_til_csv():
    # TODO: læs brugere.csv med DictReader og saml de ønskede rækker i en liste
    # TODO: åbn it_aktive.csv til skrivning med DictWriter
    # TODO: kald writeheader() og skriv rækkerne
    pass


# ── Opgave 4 ──────────────────────────────────────────────
# Læs it_aktive.csv og verificér at filtreringen er korrekt.
# Print antal rækker og alle navne.
#
# Forventet output:
#   Aktive IT-brugere: 3
#   Anna Jensen
#   Esben Madsen
#   Gorm Poulsen

def verificer_csv():
    # TODO: åbn it_aktive.csv med DictReader
    # TODO: print antal rækker og alle navne
    pass


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
