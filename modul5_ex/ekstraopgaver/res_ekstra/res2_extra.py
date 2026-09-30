"""
=============================================================
  MODUL 5  ·  Sprint 2  ·  Ekstraopgaver
  CSV-filer
=============================================================
Disse opgaver bygger videre på øvelse 2.
brugere.csv ligger i modul5/-mappen (to niveauer op).
=============================================================
"""

import csv
from pathlib import Path

MAPPE = Path(__file__).parent


# ── Opgave 4 ──────────────────────────────────────────────
# tael_pr_afdeling(brugere)
#
# Modtager en liste af dicts (som fra laes_brugere i øvelse 2).
# Returnér en dict med antal brugere pr. afdeling.
#
# Eksempel (med hele brugere.csv, ikke kun aktive):
#   {"IT": 5, "HR": 3, "Økonomi": 2, "Ledelse": 1, "Salg": 1}
#
# Hint: antal[afd] = antal.get(afd, 0) + 1

def tael_pr_afdeling(brugere):
    antal = {}
    for b in brugere:
        afd = b["afdeling"]
        antal[afd] = antal.get(afd, 0) + 1
    return antal


# ── Opgave 5 ──────────────────────────────────────────────
# filtrer_og_skriv(indsti, udsti, afdeling)
#
# Læs CSV fra indsti, find de aktive brugere i den givne afdeling,
# og skriv dem til udsti.
# Returnér antal skrevne rækker (0 hvis ingen match eller fil mangler).
#
# Hint: filtrer på b["aktiv"] == "ja" AND b["afdeling"] == afdeling
# Hint: fang FileNotFoundError og returnér 0

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
