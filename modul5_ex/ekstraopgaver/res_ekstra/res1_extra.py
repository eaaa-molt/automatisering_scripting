"""
=============================================================
  MODUL 5  ·  Sprint 1  ·  Ekstraopgaver
  Funktioner og fejlhåndtering
=============================================================
"""

from pathlib import Path

MAPPE = Path(__file__).parent

TILLADTE_AFDELINGER = ["IT", "HR", "Økonomi", "Ledelse"]


def generer_logonnavn(fornavn, efternavn):
    def normaliser(s):
        s = s.lower()
        for fra, til in [("æ", "ae"), ("ø", "oe"), ("å", "aa")]:
            s = s.replace(fra, til)
        return s
    return f"{normaliser(fornavn)}.{normaliser(efternavn)}"


def valider_bruger(fornavn, efternavn, afdeling):
    if not fornavn.strip():
        raise ValueError("Fornavn må ikke være tomt")
    if not efternavn.strip():
        raise ValueError("Efternavn må ikke være tomt")
    if afdeling not in TILLADTE_AFDELINGER:
        raise ValueError(f"{afdeling} er ikke en gyldig afdeling")
    return True


def main():
    print("=== Opgave 4: generer_logonnavn ===")
    print(generer_logonnavn("Maria", "Hansen"))    # → maria.hansen
    print(generer_logonnavn("Åse", "Dalgaard"))    # → aase.dalgaard
    print(generer_logonnavn("Mads", "Kjær"))       # → mads.kjaer
    print(generer_logonnavn("Søren", "Ølgaard"))   # → soeren.oelgaard

    print("\n=== Opgave 5: valider_bruger ===")
    print(valider_bruger("Maria", "Hansen", "IT"))
    for fnavn, enavn, afd in [("", "Hansen", "IT"), ("Maria", "", "IT"), ("Maria", "Hansen", "Salg")]:
        try:
            valider_bruger(fnavn, enavn, afd)
        except ValueError as e:
            print(f"Fejl fanget: {e}")


if __name__ == "__main__":
    main()
