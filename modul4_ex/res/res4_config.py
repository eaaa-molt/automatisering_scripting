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
    "afdeling":      "IT",
    "vis_inaktive":  false
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
def laes_config(filnavn="config.json"):
    """Indlæser og returnerer config-filen som en ordbog."""
    with open(MAPPE / filnavn, encoding="utf-8") as f:
        return json.load(f)


def main():
    config = laes_config()
    alle = [Bruger(**d) for d in ALLE_BRUGERE_DATA]

    print(alle)

    print("=== Opgave 2: Rapport-titel som overskrift ===")
    titel = config["rapport_titel"]
    print(f"  {titel}")
    print()

    print("=== Opgave 3 + 4: Filtrer på afdeling og vis_inaktive ===")
    afdeling     = config["afdeling"]
    vis_inaktive = config["vis_inaktive"]

    for b in alle:
        if b.afdeling != afdeling:
            continue
        if not vis_inaktive and not b.aktiv:
            continue
        print(b)

    print("\n=== Opgave 5: Skift config.json og kør igen ===")
    # Ingen kodeændringer — skift sker udelukkende i config.json.
    print("  (Ingen kodeændringer — skift afdeling eller titel i config.json)")


# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
