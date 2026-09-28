"""
=============================================================
  MODUL 4  ·  Sprint 4  ·  Øvelse 4
  Config-mønsteret
=============================================================
Forestil dig at du har bygget et script der viser brugere
fra IT-afdelingen. Næste uge skal det vise HR i stedet.

Uden config:  du åbner scriptet og ændrer koden.
Med config:   du åbner config.json og ændrer én linje.

Det er pointen med config-mønsteret: adskil indstillinger
fra kode. Scriptet forbliver uberørt — kun data ændres.

config.json ser sådan ud:
  {
    "rapport_titel": "IT-afdeling – brugerrapport",
    "afdeling":      "IT"
  }
=============================================================
"""

import json
from pathlib import Path

MAPPE = Path(__file__).parent

ALLE_BRUGERE_DATA = [
    {"navn": "Anna Jensen",    "email": "anna@firma.dk",    "afdeling": "IT",      "aktiv": True},
    {"navn": "Bjarne Nielsen", "email": "bjarne@firma.dk",  "afdeling": "HR",      "aktiv": True},
    {"navn": "Cecilie Hansen", "email": "cecilie@firma.dk", "afdeling": "IT",      "aktiv": False},
    {"navn": "Diana Larsen",   "email": "diana@firma.dk",   "afdeling": "Økonomi", "aktiv": False},
    {"navn": "Esben Madsen",   "email": "esben@firma.dk",   "afdeling": "IT",      "aktiv": True},
    {"navn": "Freja Olsen",    "email": "freja@firma.dk",   "afdeling": "HR",      "aktiv": True},
    {"navn": "Gorm Poulsen",   "email": "gorm@firma.dk",    "afdeling": "IT",      "aktiv": True},
]


class Bruger:
    def __init__(self, navn, email, afdeling, aktiv=True):
        self.navn     = navn
        self.email    = email
        self.afdeling = afdeling
        self.aktiv    = aktiv

    def __str__(self):
        status = "aktiv" if self.aktiv else "inaktiv"
        return f"Bruger({self.navn}, {self.afdeling}, {status})"


# ── Opgave 1 ──────────────────────────────────────────────
# Implementer laes_config(filnavn)
#
# Åbn config.json og returnér indholdet som en Python-ordbog.
# Brug json.load() inde i en with-blok.

def laes_config(filnavn="config.json"):
    """Indlæser og returnerer config-filen som en ordbog."""
    # TODO: åbn filen og returnér indholdet med json.load()
    return {}   # midlertidig tom ordbog — erstat med din løsning


def main():
    config = laes_config()
    alle = [Bruger(**d) for d in ALLE_BRUGERE_DATA]

    print("=== Opgave 2: Rapport-titel som overskrift ===")
    # Hent rapport_titel fra config og print den som overskrift.
    # Forventet output (når config er indlæst):
    #   === IT-afdeling – brugerrapport ===

    # TODO: hent config["rapport_titel"] og print den som overskrift
    print()


    print("\n=== Opgave 3: Filtrer på afdeling ===")
    # Hent afdeling fra config.
    # Gå alle brugere igennem og print dem der hører til den afdeling.
    # Forventet output (med "IT" i config):
    #   Bruger(Anna Jensen, IT, aktiv)
    #   Bruger(Cecilie Hansen, IT, inaktiv)
    #   Bruger(Esben Madsen, IT, aktiv)
    #   Bruger(Gorm Poulsen, IT, aktiv)

    # TODO: hent config["afdeling"]
    # TODO: gå alle brugere igennem og print dem fra den afdeling
    print()


    print("\n=== Opgave 4: vis_inaktive ===")
    # Tilføj selv nøglen "vis_inaktive" til config.json
    # (sæt den til false).
    # Brug den derefter her i koden til at styre om inaktive
    # brugere skal med i outputtet.
    #
    # Test: sæt vis_inaktive til true og kør igen — hvad sker der?

    # TODO: brug config["vis_inaktive"] til at filtrere inaktive fra


    print("\n=== Opgave 5: Skift config.json og kør igen ===")
    # Åbn config.json og skift "afdeling" til "HR".
    # Kør scriptet igen uden at ændre noget i koden.
    #
    # Hvad sker der med outputtet?
    # Prøv også at ændre "rapport_titel".
    # Hvad er fordelen ved at styre disse ting fra config.json
    # frem for at hardkode dem direkte i scriptet?


# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
