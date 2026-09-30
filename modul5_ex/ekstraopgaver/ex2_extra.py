"""
=============================================================
  MODUL 5  ·  Sprint 2  ·  Ekstraopgaver
  CSV-filer
=============================================================
Disse opgaver bygger videre på øvelse 2.
brugere.csv ligger i modul5/-mappen (et niveau op).
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
    # TODO: gå brugere igennem og tæl pr. afdeling med .get()
    # TODO: returnér den færdige dict
    return {}   # erstat denne linje


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
    # TODO: læs CSV fra indsti - fang FileNotFoundError og returnér 0
    # TODO: filtrer aktive brugere i den givne afdeling
    # TODO: skriv resultatet til udsti (gør intet hvis listen er tom)
    # TODO: returnér antal skrevne rækker
    return 0   # erstat denne linje


# ─────────────────────────────────────────────────────────
def main():
    def laes_csv(sti):
        try:
            with open(sti, encoding="utf-8") as f:
                return list(csv.DictReader(f))
        except FileNotFoundError:
            return []

    print("=== Opgave 4: tael_pr_afdeling ===")
    alle = laes_csv(MAPPE.parent / "brugere.csv")
    if alle:
        antal = tael_pr_afdeling(alle)
        for afd, n in antal.items():
            print(f"  {afd}: {n}")

    print("\n=== Opgave 5: filtrer_og_skriv ===")
    n = filtrer_og_skriv(MAPPE.parent / "brugere.csv", MAPPE / "it_brugere.csv", "IT")
    print(f"Skrevet: {n} IT-brugere")          # → 4

    n2 = filtrer_og_skriv(MAPPE.parent / "brugere.csv", MAPPE / "hr_brugere.csv", "HR")
    print(f"Skrevet: {n2} HR-brugere")         # → 2

    n3 = filtrer_og_skriv(MAPPE.parent / "mangler.csv", MAPPE / "ud.csv", "IT")
    print(f"Manglende fil: {n3}")              # → 0


if __name__ == "__main__":
    main()
