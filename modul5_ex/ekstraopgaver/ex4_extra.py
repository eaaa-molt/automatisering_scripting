"""
=============================================================
  MODUL 5  ·  Sprint 4  ·  Ekstraopgaver
  AD-forberedelse
=============================================================
Disse opgaver bygger videre på øvelse 4.
Bruger-klassen herunder er identisk med ex4_samlet.py — givet og færdig.
brugere.csv ligger i modul5/-mappen (et niveau op).
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
                f" ({self.afdeling}) — {self.logonnavn}")

    def til_dict(self):
        return {
            "fornavn":   self.fornavn,
            "efternavn": self.efternavn,
            "afdeling":  self.afdeling,
            "logonnavn": self.logonnavn,
        }


# ── Opgave 3 ──────────────────────────────────────────────
# vis_rapport(brugere)
#
# Print en tabel med antal gyldige brugere pr. afdeling
# og en samlet total nederst.
#
# Eksempel (med 9 gyldige brugere fra brugere.csv):
#   Afdeling          Antal
#   ──────────────────────────
#   IT                4
#   HR                2
#   Økonomi           2
#   Ledelse           1
#   ──────────────────────────
#   I alt             9
#
# Hint: brug f"{felt:<18}" til at justere venstre kolonne

def vis_rapport(brugere):
    # TODO: tæl brugere pr. afdeling i en dict
    # TODO: print header og vandret streg
    # TODO: print én linje pr. afdeling med justeret formattering
    # TODO: print afsluttende streg og totallinje
    pass   # erstat


# ── Opgave 4 ──────────────────────────────────────────────
# find_konflikter(brugere)
#
# To Bruger-objekter har en logonnavn-konflikt hvis de får
# præcist samme logonnavn.
# Returnér en liste med de Bruger-objekter der har dubletter.
#
# Hint: tæl logonnavne i en dict
# Hint: saml dem hvor antal > 1

def find_konflikter(brugere):
    # TODO: tæl forekomster af hvert logonnavn
    # TODO: saml de Bruger-objekter hvis logonnavn optræder mere end én gang
    # TODO: returnér listen (tom liste hvis ingen konflikter)
    return []   # erstat denne linje


# ─────────────────────────────────────────────────────────
def _indlaes_gyldige():
    """Hjælpefunktion: læs og validér brugere.csv til test."""
    brugere = []
    try:
        with open(MAPPE.parent / "brugere.csv", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r["aktiv"] == "ja" and r["afdeling"] in TILLADTE_AFDELINGER:
                    brugere.append(Bruger(r["fornavn"], r["efternavn"], r["afdeling"]))
    except FileNotFoundError:
        pass
    return brugere


def main():
    brugere = _indlaes_gyldige()

    print("=== Opgave 3: vis_rapport ===")
    if brugere:
        vis_rapport(brugere)
    else:
        print("(brugere.csv ikke fundet)")

    print("\n=== Opgave 4: find_konflikter ===")
    if brugere:
        konflikter = find_konflikter(brugere)
        if konflikter:
            print("Konflikter fundet:")
            for b in konflikter:
                print(f"  {b}")
        else:
            print("Ingen logonnavn-konflikter i brugere.csv")

    print("\nTest med dubletter:")
    test = [
        Bruger("Maria", "Hansen", "IT"),
        Bruger("Maria", "Hansen", "HR"),   # ← dublet
        Bruger("Jonas", "Nielsen", "HR"),
    ]
    k = find_konflikter(test)
    print(f"Fandt {len(k)} brugere med konflikter")   # → 2


if __name__ == "__main__":
    main()
