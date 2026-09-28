"""
=============================================================
  MODUL 4  ·  Øvelse 2.9
  JSON — fra Python til tekst og tilbage
=============================================================
JSON (JavaScript Object Notation) er et tekstformat til data.
Det bruges overalt: API'er, konfigurationsfiler, databaser.

Python har et indbygget json-modul med fire centrale funktioner:

  json.dumps(obj)      →  Python-objekt  til JSON-tekst (streng)
  json.loads(tekst)    →  JSON-tekst     til Python-objekt

  json.dump(obj, fil)  →  skriv direkte til en fil
  json.load(fil)       →  læs direkte fra en fil

I denne øvelse arbejder vi med plain Python-dicts.
=============================================================
"""

import json
from pathlib import Path

MAPPE = Path(__file__).parent


def main():

    # ── Opgave 1 ──────────────────────────────────────────
    # Vi starter med et Python-dict. Print det og observer typen.
    # Konvertér det derefter til JSON-tekst med json.dumps()
    # og print resultatet igen.
    #
    # Sammenlign de to outputs — hvad er ens, hvad er forskelligt?
    # Bemærk især hvad der sker med True.
    #
    # Prøv bagefter at køre denne linje og læs fejlmeldingen:
    #   print(json_tekst["navn"])
    # Sammenlign med:
    #   print(bruger["navn"])

    print("=== Opgave 1: Python-dict til JSON-tekst ===")

    bruger = {
        "navn":     "Anna Jensen",
        "email":    "anna@firma.dk",
        "afdeling": "IT",
        "aktiv":    True,
    }

    print("Python-dict:")
    print(bruger)
    print(type(bruger))
    print()

    json_tekst = json.dumps(bruger)

    print("JSON-tekst:")
    print(json_tekst)
    print(type(json_tekst))
    print()


    # ── Opgave 2 ──────────────────────────────────────────
    # Konvertér json_tekst tilbage til et Python-dict med
    # json.loads() og gem resultatet i bruger2.
    # Print bruger2["navn"] og type(bruger2).
    #
    # Forventet output:
    #   Anna Jensen
    #   <class 'dict'>

    print("=== Opgave 2: JSON-tekst til Python-dict ===")

    bruger2 = {}   # TODO: brug json.loads() på json_tekst
    print(bruger2.get("navn", "(ikke indlæst endnu)"))
    print(type(bruger2))
    print()


    # ── Opgave 3 ──────────────────────────────────────────
    # Python og JSON bruger ikke de samme navne for alle typer.
    # Konvertér nedenstående dict til JSON-tekst og print resultatet.
    # Observer hvad der sker med True, False og None.
    #
    # Forventet output:
    #   {"aktiv": true, "slettet": false, "kommentar": null}
    #
    # Python → JSON: True → true / False → false / None → null

    print("=== Opgave 3: Type-mapping (True / False / None) ===")

    type_eksempel = {
        "aktiv":     True,
        "slettet":   False,
        "kommentar": None,
    }

    # TODO: konvertér type_eksempel til JSON-tekst og print det
    print()


    # ── Opgave 4 ──────────────────────────────────────────
    # Arbejd med en liste af dicts.
    # Konvertér listen til JSON-tekst med indent=2 (pæn formatering)
    # og ensure_ascii=False (så æøå bevares korrekt).
    # Print resultatet.
    #
    # Hint: json.dumps(obj, indent=2, ensure_ascii=False)

    print("=== Opgave 4: Liste af dicts med formatering ===")

    brugere = [
        {"navn": "Anna Jensen",    "afdeling": "IT",      "aktiv": True},
        {"navn": "Bjarne Nielsen", "afdeling": "HR",      "aktiv": True},
        {"navn": "Cecilie Hansen", "afdeling": "IT",      "aktiv": False},
        {"navn": "Diana Larsen",   "afdeling": "Økonomi", "aktiv": False},
    ]

    # TODO: konvertér brugere til JSON-tekst med indent=2 og ensure_ascii=False
    print()


    # ── Opgave 5 ──────────────────────────────────────────
    # Gem listen brugere i en JSON-fil kaldet "brugere.json".
    # Brug json.dump() inde i en with-blok.
    # Brug igen indent=2 og ensure_ascii=False.
    #
    # Hint: with open(MAPPE / "brugere.json", "w", encoding="utf-8") as f:

    print("=== Opgave 5: Gem til fil ===")

    # TODO: gem brugere til brugere.json med json.dump()
    print("Gemt til brugere.json")
    print()


    # ── Opgave 6 ──────────────────────────────────────────
    # Åbn brugere.json som en almindelig tekstfil og print indholdet.
    # Brug open() med encoding="utf-8" og f.read().
    #
    # Dette viser at en JSON-fil bare er tekst — ingen magi.

    print("=== Opgave 6: Læs fil som rå tekst ===")

    # TODO: åbn brugere.json og print den rå tekst
    print()


    # ── Opgave 7 ──────────────────────────────────────────
    # Indlæs nu brugere.json igen som Python-data med json.load().
    # Gem resultatet i indlaest.
    # Print listens længde og den anden brugers navn.
    #
    # Forventet output:
    #   Antal indlæst: 4
    #   Anden bruger: Bjarne Nielsen

    print("=== Opgave 7: Indlæs fra fil ===")

    indlaest = []   # TODO: brug json.load() til at indlæse brugere.json
    print(f"Antal indlæst: {len(indlaest)}")
    if len(indlaest) >= 2:
        print(f"Anden bruger: {indlaest[1].get('navn', '?')}")
    print()


    # ── Opgave 8 ──────────────────────────────────────────
    # Verificér at data er bevaret korrekt.
    # Gå den originale liste og den indlæste igennem parallelt
    # med zip() og kontrollér at navn og aktiv-status matcher.
    #
    # Forventet output:
    #   OK  Anna Jensen
    #   OK  Bjarne Nielsen
    #   OK  Cecilie Hansen
    #   OK  Diana Larsen

    print("=== Opgave 8: Verificér data ===")

    for original, kopi in zip(brugere, indlaest):
        match = "OK " if original["navn"] == kopi.get("navn") and \
                         original["aktiv"] == kopi.get("aktiv") else "FEJL"
        print(f"  {match}  {original['navn']}")


# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
