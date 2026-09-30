"""
=============================================================
  MODUL 5  ·  Sprint 1  ·  Ekstraopgaver
  Funktioner og fejlhåndtering
=============================================================
Disse opgaver bygger videre på øvelse 1.
Løs dem i rækkefølge - opgave 5 bruger logikken fra opgave 4.
=============================================================
"""

from pathlib import Path

MAPPE = Path(__file__).parent

TILLADTE_AFDELINGER = ["IT", "HR", "Økonomi", "Ledelse"]


# ── Opgave 4 ──────────────────────────────────────────────
# generer_logonnavn(fornavn, efternavn)
#
# Returnér et logonnavn på formatet "fornavn.efternavn"
# hvor begge dele er normaliserede (lowercase, æ→ae osv.).
#
# Eksempler:
#   generer_logonnavn("Maria", "Hansen")   →  "maria.hansen"
#   generer_logonnavn("Åse", "Dalgaard")   →  "aase.dalgaard"
#   generer_logonnavn("Mads", "Kjær")      →  "mads.kjaer"
#
# Hint: definér en lokal normaliser(s)-funktion inde i generer_logonnavn
# Hint: return f"{normaliser(fornavn)}.{normaliser(efternavn)}"

def generer_logonnavn(fornavn, efternavn):
    # TODO: definér en lokal normaliser(s) der håndterer æ/ø/å
    # TODO: sammensæt og returnér "fornavn.efternavn"
    return ""   # erstat denne linje


# ── Opgave 5 ──────────────────────────────────────────────
# valider_bruger(fornavn, efternavn, afdeling)
#
# Kontrollér alle tre felter og kast ValueError ved første fejl.
# Tjek i rækkefølgen: fornavn → efternavn → afdeling.
#
# Fejlbeskeder (nøjagtigt disse):
#   "Fornavn må ikke være tomt"
#   "Efternavn må ikke være tomt"
#   "<afdeling> er ikke en gyldig afdeling"
#
# Returnér True hvis alle tre felter er gyldige.

def valider_bruger(fornavn, efternavn, afdeling):
    # TODO: tjek fornavn - kast ValueError hvis tomt
    # TODO: tjek efternavn - kast ValueError hvis tomt
    # TODO: tjek afdeling mod TILLADTE_AFDELINGER
    # TODO: returnér True hvis alt er gyldigt
    return True   # erstat denne linje (kaster ingen fejl endnu)


# ─────────────────────────────────────────────────────────
def main():
    print("=== Opgave 4: generer_logonnavn ===")
    print(generer_logonnavn("Maria", "Hansen"))    # → maria.hansen
    print(generer_logonnavn("Åse", "Dalgaard"))    # → aase.dalgaard
    print(generer_logonnavn("Mads", "Kjær"))       # → mads.kjaer
    print(generer_logonnavn("Søren", "Ølgaard"))   # → soeren.oelgaard

    print("\n=== Opgave 5: valider_bruger ===")
    print(valider_bruger("Maria", "Hansen", "IT"))  # → True
    for fnavn, enavn, afd in [("", "Hansen", "IT"), ("Maria", "", "IT"), ("Maria", "Hansen", "Salg")]:
        try:
            valider_bruger(fnavn, enavn, afd)
        except ValueError as e:
            print(f"Fejl fanget: {e}")


if __name__ == "__main__":
    main()
