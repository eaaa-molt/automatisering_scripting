"""
=============================================================
  MODUL 5  ·  Sprint 4  ·  Øvelse 4
  AD-forberedelse (samlet øvelse)
=============================================================
Kombiner CSV-læsning, validering og JSON-eksport.

Bruger-klassen er givet og færdig.
Din opgave er to funktioner:
  1. laes_og_valider  - læs CSV og filtrer ugyldige rækker
  2. gem_ad_import    - gem de gyldige brugere som JSON

Outputfilen ad_import.json er den vi åbner igen i modul 7
når vi automatiserer oprettelsen af AD-konti med Python.
=============================================================
"""

import csv
import json
from pathlib import Path

MAPPE = Path(__file__).parent

TILLADTE_AFDELINGER = ["IT", "HR", "Økonomi", "Ledelse"]


# ── Bruger-klassen er givet og færdig ─────────────────────

class Bruger:
    def __init__(self, fornavn, efternavn, afdeling):
        self.fornavn   = fornavn
        self.efternavn = efternavn
        self.afdeling  = afdeling
        self.logonnavn = self._beregn_logonnavn()

    def _beregn_logonnavn(self):
        def normaliser(s):
            s = s.lower()
            for fra, til in [("æ","ae"), ("ø","oe"), ("å","aa"),
                              ("Æ","ae"), ("Ø","oe"), ("Å","aa")]:
                s = s.replace(fra, til)
            return s
        return f"{normaliser(self.fornavn)}.{normaliser(self.efternavn)}"

    def __str__(self):
        return (f"{self.fornavn} {self.efternavn}"
                f" ({self.afdeling}) - {self.logonnavn}")

    def til_dict(self):
        return {
            "fornavn":   self.fornavn,
            "efternavn": self.efternavn,
            "afdeling":  self.afdeling,
            "logonnavn": self.logonnavn,
        }


# ── Opgave 1 ──────────────────────────────────────────────
# laes_og_valider(sti)
#
# Læs CSV-filen og opret Bruger-objekter for gyldige rækker.
# Spring en række over og print en advarsel hvis:
#   - aktiv != "ja"
#   - afdeling ikke er i TILLADTE_AFDELINGER
#
# Returnér en liste af de gyldige Bruger-objekter.
# Returnér en tom liste ved FileNotFoundError.

def laes_og_valider(sti):
    brugere = []
    try:
        with open(sti, encoding="utf-8") as f:
            for raekke in csv.DictReader(f):
                if raekke["aktiv"] != "ja":
                    print(f"  Spring over (inaktiv): {raekke['fornavn']} {raekke['efternavn']}")
                    continue
                if raekke["afdeling"] not in TILLADTE_AFDELINGER:
                    print(f"  Spring over (ugyldig afdeling '{raekke['afdeling']}'): "
                          f"{raekke['fornavn']} {raekke['efternavn']}")
                    continue
                brugere.append(Bruger(raekke["fornavn"], raekke["efternavn"], raekke["afdeling"]))
    except FileNotFoundError:
        return []
    return brugere


# ── Opgave 2 ──────────────────────────────────────────────
# gem_ad_import(brugere, sti)
#
# Gem listen af Bruger-objekter som en JSON-fil.
# Brug til_dict() på hvert objekt.
# Print: "Gemt <antal> brugere til <filnavn>"

def gem_ad_import(brugere, sti):
    data = [b.til_dict() for b in brugere]
    with open(sti, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Gemt {len(brugere)} brugere til {sti.name}")


def main():
    datafil = MAPPE.parent / "brugere.csv"

    print("=== Opgave 1: laes_og_valider ===")
    brugere = laes_og_valider(datafil)
    print(f"\nGyldige til AD-import: {len(brugere)}")
    for b in brugere:
        print(f"  {b}")

    print("\n=== Opgave 2: gem_ad_import ===")
    gem_ad_import(brugere, MAPPE / "ad_import.json")


if __name__ == "__main__":
    main()
