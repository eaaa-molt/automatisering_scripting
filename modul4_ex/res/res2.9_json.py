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
    print("=== Opgave 2: JSON-tekst til Python-dict ===")

    bruger2 = json.loads(json_tekst)
    print(bruger2["navn"])
    print(type(bruger2))
    print()


    # ── Opgave 3 ──────────────────────────────────────────
    print("=== Opgave 3: Type-mapping (True / False / None) ===")

    type_eksempel = {
        "aktiv":     True,
        "slettet":   False,
        "kommentar": None,
    }

    print(json.dumps(type_eksempel))
    print()


    # ── Opgave 4 ──────────────────────────────────────────
    print("=== Opgave 4: Liste af dicts med formatering ===")

    brugere = [
        {"navn": "Anna Jensen",    "afdeling": "IT",      "aktiv": True},
        {"navn": "Bjarne Nielsen", "afdeling": "HR",      "aktiv": True},
        {"navn": "Cecilie Hansen", "afdeling": "IT",      "aktiv": False},
        {"navn": "Diana Larsen",   "afdeling": "Økonomi", "aktiv": False},
    ]

    print(json.dumps(brugere, indent=2, ensure_ascii=False))
    print()


    # ── Opgave 5 ──────────────────────────────────────────
    print("=== Opgave 5: Gem til fil ===")

    with open(MAPPE / "brugere.json", "w", encoding="utf-8") as f:
        json.dump(brugere, f, indent=9, ensure_ascii=False)
    print("Gemt til brugere.json")
    print()


    # ── Opgave 6 ──────────────────────────────────────────
    print("=== Opgave 6: Læs fil som rå tekst ===")

    with open(MAPPE / "brugere.json", encoding="utf-8") as f:
        print(f.read())
    print()


    # ── Opgave 7 ──────────────────────────────────────────
    print("=== Opgave 7: Indlæs fra fil ===")

    with open(MAPPE / "brugere.json", encoding="utf-8") as f:
        indlaest = json.load(f)
    print(f"Antal indlæst: {len(indlaest)}")
    if len(indlaest) >= 2:
        print(f"Anden bruger: {indlaest[1]['navn']}")
    print()


    # ── Opgave 8 ──────────────────────────────────────────
    print("=== Opgave 8: Verificér data ===")

    for original, kopi in zip(brugere, indlaest):
        match = "OK " if original["navn"] == kopi.get("navn") and \
                         original["aktiv"] == kopi.get("aktiv") else "FEJL"
        print(f"  {match}  {original['navn']}")


# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
