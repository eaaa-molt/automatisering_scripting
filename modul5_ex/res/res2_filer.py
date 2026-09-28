"""
=============================================================
  MODUL 5  ·  Sprint 2  ·  Øvelse 2
  CSV-filer
=============================================================
"""

import csv
from pathlib import Path

MAPPE = Path(__file__).parent


def laes_brugere(sti):
    try:
        with open(sti, encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []


def filtrer_aktive(brugere):
    return [b for b in brugere if b["aktiv"] == "ja"]


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
