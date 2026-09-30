"""
=============================================================
  MODUL 5  ·  Sprint 1  ·  Øvelse 1
  Funktioner og fejlhåndtering
=============================================================
Repetition af def, return, try/except og raise ValueError.

Vi bygger tre hjælpefunktioner som alle bruges igen
i øvelse 3 og 4 - og i modul 7 når vi automatiserer AD.
=============================================================
"""

from pathlib import Path

MAPPE = Path(__file__).parent

TILLADTE_AFDELINGER = ["IT", "HR", "Økonomi", "Ledelse"]


# ── Opgave 1 ──────────────────────────────────────────────
# normaliser_tegn(tekst)
#
# Erstat danske specialtegn i en streng:
#   æ → ae,  ø → oe,  å → aa
#   (og de store varianter: Æ, Ø, Å)
# Gør desuden teksten til lowercase.
# Returnér den normaliserede streng.
#
# Eksempler:
#   normaliser_tegn("Søren")    →  "soeren"
#   normaliser_tegn("Ølgaard")  →  "oelgaard"
#   normaliser_tegn("ÅSE")      →  "aase"
#
# Hint: brug s.lower() og derefter s.replace(fra, til)
#       for hvert tegn-par i en liste

def normaliser_tegn(tekst):
    s = tekst.lower()
    for fra, til in [("æ", "ae"), ("ø", "oe"), ("å", "aa")]:
        s = s.replace(fra, til)
    return s


# ── Opgave 2 ──────────────────────────────────────────────
# laes_fil(sti)
#
# Åbner en fil og returnerer indholdet som én streng.
# Returnér None hvis filen ikke eksisterer - ingen crash.
#
# Hint: brug try/except FileNotFoundError
# Hint: åbn med encoding="utf-8"

def laes_fil(sti):
    try:
        with open(sti, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


# ── Opgave 3 ──────────────────────────────────────────────
# tjek_afdeling(afdeling)
#
# Kontrollér at afdelingen er i TILLADTE_AFDELINGER.
# Returnér afdelingen uændret hvis den er gyldig.
# Kast ValueError med en beskrivende besked hvis ikke.
#
# Eksempler:
#   tjek_afdeling("IT")     →  "IT"
#   tjek_afdeling("Salg")   →  ValueError: "Salg er ikke en gyldig afdeling"
#
# Hint: if afdeling not in TILLADTE_AFDELINGER:
# Hint: raise ValueError(f"...")

def tjek_afdeling(afdeling):
    if afdeling not in TILLADTE_AFDELINGER:
        raise ValueError(f"{afdeling} er ikke en gyldig afdeling")
    return afdeling


def main():
    print("=== Opgave 1: normaliser_tegn ===")
    print(normaliser_tegn("Søren"))       # → soeren
    print(normaliser_tegn("Ølgaard"))     # → oelgaard
    print(normaliser_tegn("Åse"))         # → aase
    print(normaliser_tegn("Maria"))       # → maria

    print("\n=== Opgave 2: laes_fil ===")
    print(laes_fil("mangler.txt"))
    indhold = laes_fil(MAPPE.parent / "brugere.csv")
    if indhold is not None:
        print(f"Fil indlæst - {len(indhold)} tegn")

    print("\n=== Opgave 3: tjek_afdeling ===")
    print(tjek_afdeling("IT"))
    print(tjek_afdeling("Økonomi"))
    try:
        print(tjek_afdeling("Salg"))
    except ValueError as e:
        print(f"Fejl fanget: {e}")


if __name__ == "__main__":
    main()
