"""
=============================================================
  MODUL 5  ·  Sprint 2  ·  Ekstraopgaver
  CSV-filer
=============================================================
"""

import csv
from pathlib import Path

MAPPE = Path(__file__).parent


def tael_pr_afdeling(brugere):
    antal = {}
    for b in brugere:
        afd = b["afdeling"]
        antal[afd] = antal.get(afd, 0) + 1
    return antal


def filtrer_og_skriv(indsti, udsti, afdeling):
    try:
        with open(indsti, encoding="utf-8") as f:
            brugere = list(csv.DictReader(f))
    except FileNotFoundError:
        return 0
    filtrerede = [b for b in brugere if b["aktiv"] == "ja" and b["afdeling"] == afdeling]
    if not filtrerede:
        return 0
    felter = list(filtrerede[0].keys())
    with open(udsti, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=felter)
        writer.writeheader()
        writer.writerows(filtrerede)
    return len(filtrerede)


def main():
    datafil = MAPPE.parent.parent / "brugere.csv"

    def laes_csv(sti):
        try:
            with open(sti, encoding="utf-8") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            return []

    print("=== Opgave 4: tael_pr_afdeling ===")
    alle = laes_csv(datafil)
    if alle:
        antal = tael_pr_afdeling(alle)
        for afd, n in antal.items():
            print(f"  {afd}: {n}")

    print("\n=== Opgave 5: filtrer_og_skriv ===")
    n = filtrer_og_skriv(datafil, MAPPE / "it_brugere.csv", "IT")
    print(f"Skrevet: {n} IT-brugere")

    n2 = filtrer_og_skriv(datafil, MAPPE / "hr_brugere.csv", "HR")
    print(f"Skrevet: {n2} HR-brugere")

    n3 = filtrer_og_skriv(MAPPE.parent.parent / "mangler.csv", MAPPE / "ud.csv", "IT")
    print(f"Manglende fil: {n3}")


if __name__ == "__main__":
    main()
