"""
=============================================================
  MODUL 5  ·  Sprint 3  ·  Øvelse 3
  JSON og klasser
=============================================================
"""

import json
from pathlib import Path

MAPPE = Path(__file__).parent


class Bruger:
    def __init__(self, fornavn, efternavn, afdeling):
        self.fornavn   = fornavn
        self.efternavn = efternavn
        self.afdeling  = afdeling

    def __str__(self):
        return f"{self.fornavn} {self.efternavn} ({self.afdeling})"

    def til_dict(self):
        return {
            "fornavn":   self.fornavn,
            "efternavn": self.efternavn,
            "afdeling":  self.afdeling,
        }


def gem_som_json(brugere, sti):
    data = [b.til_dict() for b in brugere]
    with open(sti, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def hent_fra_json(sti):
    try:
        with open(sti, encoding="utf-8") as f:
            data = json.load(f)
        return [Bruger(**d) for d in data]
    except FileNotFoundError:
        return []


def main():
    b1 = Bruger("Maria", "Hansen", "IT")
    b2 = Bruger("Jonas", "Nielsen", "HR")
    b3 = Bruger("Åse", "Dalgaard", "Ledelse")

    print("=== Opgave 1: __str__ ===")
    print(b1)
    print(b2)

    print("\n=== Opgave 2: til_dict ===")
    print(b1.til_dict())

    print("\n=== Opgave 3: gem_som_json ===")
    gem_som_json([b1, b2, b3], MAPPE / "brugere.json")
    print("Gemt til brugere.json")

    print("\n=== Opgave 4: hent_fra_json ===")
    genfundet = hent_fra_json(MAPPE / "brugere.json")
    for b in genfundet:
        print(b)
    print(hent_fra_json(MAPPE / "mangler.json"))   # → []


if __name__ == "__main__":
    main()
