"""
=============================================================
  MODUL 4  ·  Sprint 3  ·  Øvelse 3
  JSON: gem og indlæs objekter
=============================================================
JSON (JavaScript Object Notation) er et tekstformat til data.
Det bruges overalt: API'er, konfigurationsfiler, databaser.

Python's json-modul kan:
  json.dumps(obj)        →  Python-objekt  til JSON-tekst
  json.loads(tekst)      →  JSON-tekst     til Python-objekt
  json.dump(obj, fil)    →  skriv direkte til en fil
  json.load(fil)         →  læs direkte fra en fil

MEN: json kender ikke vores Bruger-klasse.
Vi skal selv oversætte: Bruger → dict → JSON og tilbage igen.
=============================================================
"""

import json
from pathlib import Path

MAPPE = Path(__file__).parent


class Bruger:
    def __init__(self, navn, email, afdeling, aktiv=True):
        self.navn     = navn
        self.email    = email
        self.afdeling = afdeling
        self.aktiv    = aktiv

    def __str__(self):
        status = "aktiv" if self.aktiv else "inaktiv"
        return f"Bruger({self.navn}, {self.afdeling}, {status})"


def til_dict(bruger):
    """Konverterer et Bruger-objekt til en Python-ordbog."""
    return bruger.__dict__


def fra_dict(d):
    """Konverterer en ordbog til et Bruger-objekt."""
    return Bruger(**d)


def gem_brugere(brugere, filnavn):
    """Gemmer en liste af Bruger-objekter i en JSON-fil."""
    data = [til_dict(b) for b in brugere]
    with open(MAPPE / filnavn, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def indlaes_brugere(filnavn):
    """Indlæser brugere fra en JSON-fil og returnerer en liste af Bruger-objekter."""
    with open(MAPPE / filnavn, encoding="utf-8") as f:
        data = json.load(f)
    return [fra_dict(d) for d in data]


def main():
    brugere = [
        Bruger("Anna Jensen",    "anna@firma.dk",    "IT"),
        Bruger("Bjarne Nielsen", "bjarne@firma.dk",  "HR"),
        Bruger("Cecilie Hansen", "cecilie@firma.dk", "IT",      aktiv=False),
        Bruger("Diana Larsen",   "diana@firma.dk",   "Økonomi", aktiv=False),
        Bruger("Esben Madsen",   "esben@firma.dk",   "IT"),
    ]

    # ── Test opgave 1 og 2 ────────────────────────────────
    print("=== Opgave 1 og 2: til_dict og fra_dict ===")
    b = brugere[0]
    d = til_dict(b)
    print("til_dict:", d)
    b2 = fra_dict(d)
    print("fra_dict:", b2)
    print("Samme navn?", b.navn == b2.navn)

    # ── Test opgave 3 ─────────────────────────────────────
    print("\n=== Opgave 3: gem_brugere ===")
    gem_brugere(brugere, "brugere.json")
    print("Gemt til brugere.json")

    # ── Test opgave 4 ─────────────────────────────────────
    print("\n=== Opgave 4: indlaes_brugere ===")
    indlaest = indlaes_brugere("brugere.json")
    for b in indlaest:
        print(b)

    # ── Kontrol ───────────────────────────────────────────
    print("\n=== Kontrol ===")
    print(f"Gemt: {len(brugere)}  /  Indlæst: {len(indlaest)}")
    for original, kopi in zip(brugere, indlaest):
        match = "OK  " if original.navn == kopi.navn and original.aktiv == kopi.aktiv else "FEJL"
        print(f"  {match}  {original.navn}")


# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
