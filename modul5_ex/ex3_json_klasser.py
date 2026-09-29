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


# ── Eksperimenter ─────────────────────────────────────────
# Fjern # og kør for at genopfriske json.dump:
#
# Eksperiment 1: hvad ser JSON ud?
#   import json
#   data = [{"navn": "Maria", "afdeling": "IT"}]
#   print(json.dumps(data, indent=2, ensure_ascii=False))
# ─────────────────────────────────────────────────────────


class Bruger:
    # __init__ er givet og færdig - tilføj de to metoder nedenfor

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
        # TODO: returnér den formaterede streng
        return ""   # erstat denne linje

    # ── Opgave 2 ──────────────────────────────────────────
    # Tilføj metoden til_dict(self) til klassen.
    #
    # Den skal returnere en dict med alle tre attributter:
    #   {"fornavn": ..., "efternavn": ..., "afdeling": ...}

    def til_dict(self):
        # TODO: returnér en dict med de tre attributter
        return {}   # erstat denne linje


# ── Opgave 3 ──────────────────────────────────────────────
# gem_som_json(brugere, sti)
#
# Gem en liste af Bruger-objekter som en JSON-fil.
# Brug til_dict() på hvert objekt inden du gemmer.
# Brug indent=2 og ensure_ascii=False.

def gem_som_json(brugere, sti):
    # TODO: konvertér listen med til_dict() og gem som JSON
    pass   # erstat


# ── Opgave 4 ──────────────────────────────────────────────
# hent_fra_json(sti)
#
# Indlæs JSON-filen og opret Bruger-objekter fra de gemte dicts.
# Returnér en tom liste hvis filen ikke eksisterer.
#
# Hint: Bruger(**d) opretter et objekt fra en dict

def hent_fra_json(sti):
    # TODO: indlæs JSON og opret Bruger-objekter
    # TODO: fang FileNotFoundError og returnér []
    return []   # erstat denne linje


# ─────────────────────────────────────────────────────────
def main():
    b1 = Bruger("Maria", "Hansen", "IT")
    b2 = Bruger("Jonas", "Nielsen", "HR")
    b3 = Bruger("Åse", "Dalgaard", "Ledelse")

    print("=== Opgave 1: __str__ ===")
    print(b1)   # → Maria Hansen (IT)
    print(b2)   # → Jonas Nielsen (HR)

    print("\n=== Opgave 2: til_dict ===")
    print(b1.til_dict())
    # → {'fornavn': 'Maria', 'efternavn': 'Hansen', 'afdeling': 'IT'}

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
