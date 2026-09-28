"""
=============================================================
  MODUL 5  ·  Sprint 4  ·  Ekstraopgaver
  AD-forberedelse
=============================================================
"""

import csv
import json
from pathlib import Path

MAPPE = Path(__file__).parent

TILLADTE_AFDELINGER = ["IT", "HR", "Økonomi", "Ledelse"]


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


def vis_rapport(brugere):
    antal = {}
    for b in brugere:
        antal[b.afdeling] = antal.get(b.afdeling, 0) + 1
    streg = "─" * 26
    print(f"{'Afdeling':<18}{'Antal'}")
    print(streg)
    for afd, n in antal.items():
        print(f"{afd:<18}{n}")
    print(streg)
    print(f"{'I alt':<18}{len(brugere)}")


def find_konflikter(brugere):
    antal = {}
    for b in brugere:
        antal[b.logonnavn] = antal.get(b.logonnavn, 0) + 1
    return [b for b in brugere if antal[b.logonnavn] > 1]


def _indlaes_gyldige():
    brugere = []
    try:
        with open(MAPPE.parent.parent / "brugere.csv", encoding="utf-8") as f:
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
            for b in konflikter:
                print(f"  {b}")
        else:
            print("Ingen logonnavn-konflikter i brugere.csv")

    print("\nTest med dubletter:")
    test = [
        Bruger("Maria", "Hansen", "IT"),
        Bruger("Maria", "Hansen", "HR"),
        Bruger("Jonas", "Nielsen", "HR"),
    ]
    k = find_konflikter(test)
    print(f"Fandt {len(k)} brugere med konflikter")   # → 2


if __name__ == "__main__":
    main()
