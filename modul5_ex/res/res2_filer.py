"""
=============================================================
  MODUL 5  ·  Sprint 2  ·  Øvelse 2
  CSV-filer
=============================================================
Repetition af csv.DictReader og csv.DictWriter.

Vi læser brugere fra en CSV-fil, filtrerer dem
og skriver de filtrerede data til en ny fil.
Datafil: brugere.csv  (ligger i modul5/-mappen, et niveau op)
=============================================================
"""

import csv
from pathlib import Path

MAPPE = Path(__file__).parent


# ── Opgave 1 ──────────────────────────────────────────────
# laes_brugere(sti)
#
# Læs en CSV-fil med csv.DictReader.
# Returnér en liste af dicts - én dict pr. række.
# Returnér en tom liste hvis filen ikke eksisterer.
#
# Hint: list(csv.DictReader(f)) giver listen direkte
# Hint: fang FileNotFoundError med try/except

def laes_brugere(sti):
    try:
        with open(sti, encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []


# ── Opgave 2 ──────────────────────────────────────────────
# filtrer_aktive(brugere)
#
# Returnér en ny liste med kun de brugere
# hvor feltet "aktiv" har værdien "ja".
#
# Hint: gå listen igennem med en for-løkke og brug if
# Hint: eller brug en list comprehension

def filtrer_aktive(brugere):
    
    result = []
    for b in brugere:
        if b['aktiv'] == "ja":
            result.append(b)
    return result



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
    if not brugere:
        return
    felter = list(brugere[0].keys())
    with open(sti, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=felter)
        writer.writeheader()
        writer.writerows(brugere)


def main():
    datafil = MAPPE.parent / "brugere.csv"

    print("=== Opgave 1: laes_brugere ===")
    alle = laes_brugere(datafil)
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
