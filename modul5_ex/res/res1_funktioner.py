"""
=============================================================
  MODUL 5  ·  Sprint 1  ·  Øvelse 1
  Funktioner og fejlhåndtering
=============================================================
"""

from pathlib import Path

MAPPE = Path(__file__).parent

TILLADTE_AFDELINGER = ["IT", "HR", "Økonomi", "Ledelse"]


def normaliser_tegn(tekst):
    s = tekst.lower()
    for fra, til in [("æ", "ae"), ("ø", "oe"), ("å", "aa")]:
        s = s.replace(fra, til)
    return s


def laes_fil(sti):
    try:
        with open(sti, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None


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
        print(f"Fil indlæst — {len(indhold)} tegn")

    print("\n=== Opgave 3: tjek_afdeling ===")
    print(tjek_afdeling("IT"))
    print(tjek_afdeling("Økonomi"))
    try:
        print(tjek_afdeling("Salg"))
    except ValueError as e:
        print(f"Fejl fanget: {e}")


if __name__ == "__main__":
    main()
