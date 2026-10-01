"""
=============================================================
  MODUL 5  ·  Sprint 3  ·  Øvelse 3
  JSON og klasser
=============================================================
Repetition af class, __init__, __str__ og json.dump/load.

Bruger-klassen får en __init__ der er færdig.
Din opgave er at tilføje to metoder til klassen
og to funktioner der gemmer/henter fra JSON.
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

    # ── Opgave 1 ──────────────────────────────────────────
    # Tilføj metoden __str__(self) til klassen.
    #
    # Den skal returnere en streng på formatet:
    #   "Maria Hansen (IT)"
    #
    # Hint: f"{self.fornavn} {self.efternavn} ({self.afdeling})"

    def __str__(self):
        return f"{self.fornavn} {self.efternavn} ({self.afdeling})"

    # ── Opgave 2 ──────────────────────────────────────────
    # Tilføj metoden til_dict(self) til klassen.
    #
    # Den skal returnere en dict med alle tre attributter:
    #   {"fornavn": ..., "efternavn": ..., "afdeling": ...}

    def til_dict(self):
        return {
            "fornavn":   self.fornavn,
            "efternavn": self.efternavn,
            "afdeling":  self.afdeling,
        }


# ── Opgave 3 ──────────────────────────────────────────────
# gem_som_json(brugere, sti)
#
# Gem en liste af Bruger-objekter som en JSON-fil.
# Brug til_dict() på hvert objekt inden du gemmer.
# Brug indent=2 og ensure_ascii=False.

def gem_som_json(brugere, sti):
    bruger_dicts = []
    for bruger in brugere:
        bruger_dicts.append(bruger.til_dict())
    with open(sti, "w", encoding="utf-8") as f:
        json.dump(bruger_dicts, f, indent=2, ensure_ascii=False)


# ── Opgave 4 ──────────────────────────────────────────────
# hent_fra_json(sti)
#
# Indlæs JSON-filen og opret Bruger-objekter fra de gemte dicts.
# Returnér en tom liste hvis filen ikke eksisterer.
#
# Hint: Bruger(**d) opretter et objekt fra en dict

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
