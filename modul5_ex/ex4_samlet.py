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
    # TODO: åbn filen og læs med DictReader - fang FileNotFoundError
    # TODO: gå rækker igennem og spring over ved ugyldige værdier
    # TODO: opret Bruger-objekt og tilføj til listen
    # TODO: returnér listen
    return []   # erstat denne linje


# ── Opgave 2 ──────────────────────────────────────────────
# gem_ad_import(brugere, sti)
#
# Gem listen af Bruger-objekter som en JSON-fil.
# Brug til_dict() på hvert objekt.
# Print: "Gemt <antal> brugere til <filnavn>"

def gem_ad_import(brugere, sti):
    # TODO: konvertér med til_dict() og gem som JSON
    # TODO: print bekræftelse med antal og filnavn
    pass   # erstat


# ─────────────────────────────────────────────────────────
def main():
    print("=== Opgave 1: laes_og_valider ===")
    brugere = laes_og_valider(MAPPE / "brugere.csv")
    print(f"\nGyldige til AD-import: {len(brugere)}")   # → 9
    for b in brugere:
        print(f"  {b}")

    print("\n=== Opgave 2: gem_ad_import ===")
    gem_ad_import(brugere, MAPPE / "ad_import.json")
    # → Gemt 9 brugere til ad_import.json


if __name__ == "__main__":
    main()
