"""
=============================================================
  MODUL 5  ·  Sprint 2  ·  Øvelse 2
  CSV-filer
=============================================================
Repetition af csv.DictReader og csv.DictWriter.

Vi læser brugere fra en CSV-fil, filtrerer dem
og skriver de filtrerede data til en ny fil.
Datafil: brugere.csv  (ligger i samme mappe som scriptet)
=============================================================
"""

import csv
from pathlib import Path

MAPPE = Path(__file__).parent


# ── Eksperimenter ─────────────────────────────────────────
# Fjern # og kør linjerne for at genopfriske DictReader:
#
# Eksperiment 1: åbn brugere.csv manuelt og print første linje
#   with open(MAPPE / "brugere.csv", encoding="utf-8") as f:
#       laeseren = csv.DictReader(f)
#       print(next(laeseren))
#
# Eksperiment 2: hvad returnerer DictReader?
#   print(type(next(laeseren)))   # → <class 'dict'>
# ─────────────────────────────────────────────────────────


# ── Opgave 1 ──────────────────────────────────────────────
# laes_brugere(sti)
#
# Læs en CSV-fil med csv.DictReader.
# Returnér en liste af dicts — én dict pr. række.
# Returnér en tom liste hvis filen ikke eksisterer.
#
# Hint: list(csv.DictReader(f)) giver listen direkte
# Hint: fang FileNotFoundError med try/except

def laes_brugere(sti):
    # TODO: åbn filen med encoding="utf-8"
    # TODO: brug csv.DictReader og returnér listen
    # TODO: fang FileNotFoundError og returnér []
    return []   # erstat denne linje


# ── Opgave 2 ──────────────────────────────────────────────
# filtrer_aktive(brugere)
#
# Returnér en ny liste med kun de brugere
# hvor feltet "aktiv" har værdien "ja".
#
# Hint: gå listen igennem med en for-løkke og brug if
# Hint: eller brug en list comprehension

def filtrer_aktive(brugere):
    # TODO: gå brugere igennem og saml dem med aktiv == "ja"
    # TODO: returnér den filtrerede liste
    return []   # erstat denne linje


# ── Opgave 3 ──────────────────────────────────────────────
# skriv_brugere(brugere, sti)
#
# Skriv listen af dicts til en CSV-fil med csv.DictWriter.
# Første linje skal være en header med kolonnenavnene.
# Gør intet hvis listen er tom.
#
# Hint: brug feltnavne fra første element:
#       list(brugere[0].keys())
# Hint: kald writeheader() og derefter writerows(brugere)
# Hint: åbn med newline="" og encoding="utf-8"

def skriv_brugere(brugere, sti):
    # TODO: tjek om listen er tom — returnér i så fald straks
    # TODO: åbn filen og opret DictWriter med feltnavne
    # TODO: skriv header og derefter alle rækker
    pass   # erstat


# ─────────────────────────────────────────────────────────
def main():
    print("=== Opgave 1: laes_brugere ===")
    alle = laes_brugere(MAPPE / "brugere.csv")
    print(f"Indlæste: {len(alle)} brugere")   # → 12
    if alle:
        print(alle[0])

    print("\n=== Opgave 2: filtrer_aktive ===")
    aktive = filtrer_aktive(alle)
    print(f"Aktive: {len(aktive)}")            # → 10

    print("\n=== Opgave 3: skriv_brugere ===")
    skriv_brugere(aktive, MAPPE / "aktive_brugere.csv")
    kontrol = laes_brugere(MAPPE / "aktive_brugere.csv")
    print(f"Gemt og genlæst: {len(kontrol)}")  # → 10


if __name__ == "__main__":
    main()
