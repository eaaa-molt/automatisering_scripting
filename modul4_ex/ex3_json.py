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


# ── Eksperimenter ─────────────────────────────────────────
# Kør disse eksperimenter én ad gangen ved at fjerne #
# og observere outputtet — de behøver ikke at virke!
#
# Eksperiment 1: Prøv at serialisere et objekt direkte
#
#   b = Bruger("Anna Jensen", "anna@firma.dk", "IT")
#   print(json.dumps(b))
#
# → Hvad sker der? Læs fejlmeldingen. Hvad kan json ikke?
#
# ─────────────────────────────────────────────────────────
# Eksperiment 2: Undersøg __dict__
#
#   b = Bruger("Anna Jensen", "anna@firma.dk", "IT")
#   print(b.__dict__)
#
# → Hvad returnerer __dict__? Hvilken type er det?
#   Prøv: print(type(b.__dict__))
#
# ─────────────────────────────────────────────────────────
# Eksperiment 3: Prøv ** til at oprette et objekt fra en dict
#
#   d = {"navn": "Bjarne Nielsen", "email": "bjarne@firma.dk",
#         "afdeling": "HR", "aktiv": True}
#   b = Bruger(**d)
#   print(b.navn)
#
# → Virker det? Prøv at ændre en nøgle i d til noget forkert
#   og se hvad fejlmeldingen siger.
# ─────────────────────────────────────────────────────────


# ── Opgave 1 ──────────────────────────────────────────────
# Implementer til_dict(bruger) → dict
#
# Returnér en Python-ordbog med brugerens fire attributter.
# Du har nu set hvad __dict__ returnerer — brug det.
#
# Funktionen skal virke sådan her:
#   b = Bruger("Anna Jensen", "anna@firma.dk", "IT")
#   d = til_dict(b)
#   print(d["navn"])      →  "Anna Jensen"
#   print(d["aktiv"])     →  True
#   print(type(d))        →  <class 'dict'>

def til_dict(bruger):
    """Konverterer et Bruger-objekt til en Python-ordbog."""
    # TODO: returnér brugerens attributter som en ordbog
    return {}   # midlertidig tom ordbog — erstat med din løsning


# ── Opgave 2 ──────────────────────────────────────────────
# Implementer fra_dict(d) → Bruger
#
# Modtager en ordbog og returnerer et Bruger-objekt.
# Du har set at Bruger(**d) virker i Eksperiment 3.
#
# Prøv begge varianter og vælg den du forstår bedst:
#   Variant A: opret Bruger med d["navn"], d["email"] osv.
#   Variant B: brug ** til at udpakke ordbogen
#
# Funktionen skal virke sådan her:
#   d = {"navn": "Anna Jensen", "email": "anna@firma.dk",
#         "afdeling": "IT", "aktiv": True}
#   b = fra_dict(d)
#   print(b.navn)         →  "Anna Jensen"
#   print(type(b))        →  <class '__main__.Bruger'>

def fra_dict(d):
    """Konverterer en ordbog til et Bruger-objekt."""
    # TODO: opret og returner et Bruger-objekt ud fra ordbogen d
    return Bruger("", "", "")   # midlertidig dummy — erstat med din løsning


# ── Opgave 3 ──────────────────────────────────────────────
# Implementer gem_brugere(brugere, filnavn)
#
# Nu er vi klar til JSON!
# Gem en liste af Bruger-objekter som en JSON-fil.
#
# Fremgangsmåde:
#   1. Byg en liste af dicts — brug til_dict() på hvert objekt
#   2. Åbn filen til skrivning med open() og encoding="utf-8"
#   3. Skriv listen til filen med json.dump()
#      Brug indent=2 så filen er læsbar, og ensure_ascii=False
#      så danske tegn gemmes korrekt.
#
# Hint: brug MAPPE / filnavn som filsti

def gem_brugere(brugere, filnavn):
    """Gemmer en liste af Bruger-objekter i en JSON-fil."""
    # TODO: konvertér hvert Bruger-objekt til en dict med til_dict()
    # TODO: åbn filen og gem listen med json.dump()
    pass


# ── Opgave 4 ──────────────────────────────────────────────
# Implementer indlaes_brugere(filnavn) → list[Bruger]
#
# Indlæs JSON-filen og konvertér indholdet til Bruger-objekter.
#
# Fremgangsmåde:
#   1. Åbn filen til læsning med open() og encoding="utf-8"
#   2. Brug json.load() for at indlæse listen af dicts
#   3. Konvertér hvert dict til et Bruger-objekt med fra_dict()
#   4. Returnér listen af Bruger-objekter

def indlaes_brugere(filnavn):
    """Indlæser brugere fra en JSON-fil og returnerer en liste af Bruger-objekter."""
    # TODO: åbn filen og indlæs data med json.load()
    # TODO: konvertér hvert dict til et Bruger-objekt med fra_dict()
    # TODO: returnér listen
    return []   # midlertidig tom liste — erstat med din løsning


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
