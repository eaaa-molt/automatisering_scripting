"""
=============================================================
  MODUL 3  ·  Sprint 3  ·  Øvelse 3
  Fejlhåndtering
=============================================================
Når Python møder noget uventet — en fil der ikke findes,
et tal der ikke kan konverteres — stopper scriptet med en
fejlmeddelelse og en traceback.

Det kan vi undgå med try/except:

  try:
      # kode der kan fejle
  except FejlType:
      # hvad skal der ske i stedet

Vi kan også selv kaste en fejl med raise:

  raise ValueError("Noget gik galt")

Det bruges til at afvise ugyldigt input i vores egne
funktioner.
=============================================================
"""

import csv
from pathlib import Path

MAPPE = Path(__file__).parent


# ── Eksperimenter ─────────────────────────────────────────
# Kør disse eksperimenter og observer hvad der sker.
# Fjern # for at aktivere ét ad gangen:
#
# Eksperiment 1: Hvad sker der uden try/except?
#   with open(MAPPE / "INGEN_FIL.txt", encoding="utf-8") as f:
#       print(f.read())
#   → Scriptet crasher med FileNotFoundError.
#     Læs traceback-teksten — hvilken linje fejler?
#
# Eksperiment 2: ValueError
#   tal = int("ikke et tal")
#   → Hvad fortæller fejlmeldingen?
#
# Eksperiment 3: int("3.14")
#   tal = int("3.14")
#   → Overraskende? Hvad er forskellen på int() og float()?
# ─────────────────────────────────────────────────────────


# ── Opgave 1 ──────────────────────────────────────────────
# Implementer laes_fil(filnavn) → str eller None
#
# Forsøg at åbne og læse en fil.
# Returnér indholdet som én streng hvis filen findes.
# Hvis filen ikke eksisterer: print en venlig besked
# og returnér None.
#
# Hint:
#   - Brug try/except FileNotFoundError
#   - I try-blokken: åbn filen og returnér indholdet
#   - I except-blokken: print en besked og returnér None

def laes_fil(filnavn):
    """Forsøger at læse en fil. Returnerer indhold eller None."""
    # TODO: brug try til at åbne filen med open() og with
    # TODO: brug except FileNotFoundError til at håndtere fejlen
    # TODO: i except-blokken: print en besked og returnér None
    pass


# ── Opgave 2 ──────────────────────────────────────────────
# Implementer konverter_til_tal(tekst) → int
#
# Forsøg at konvertere teksten til et heltal med int().
# Hvis det mislykkes: print en besked og returnér 0.
#
# Test i main():
#   konverter_til_tal("42")     →  42
#   konverter_til_tal("abc")    →  0  (og en besked)
#   konverter_til_tal("3.14")   →  0  (og en besked)
#
# Hint:
#   - Brug try/except ValueError
#   - Returnér int(tekst) i try-blokken
#   - Returnér 0 i except-blokken

def konverter_til_tal(tekst):
    """Forsøger at konvertere tekst til int. Returnerer 0 ved fejl."""
    # TODO: try → return int(tekst)
    # TODO: except ValueError → print besked, return 0
    pass


# ── Opgave 3 ──────────────────────────────────────────────
# Implementer tjek_bool_tekst(tekst) → bool
#
# CSV-filer gemmer "aktiv"-feltet som teksten "True" eller "False".
# Vi vil konvertere det til en rigtig Python bool.
# Men hvis teksten er noget helt andet, skal vi give en fejl.
#
# Returnér True  hvis tekst.strip() er "True"
# Returnér False hvis tekst.strip() er "False"
# I alle andre tilfælde: kast en ValueError med en forklarende besked.
#
# Test i main() med try/except:
#   tjek_bool_tekst("True")   →  True
#   tjek_bool_tekst("False")  →  False
#   tjek_bool_tekst("ja")     →  ValueError kastes
#
# Hint:
#   - raise ValueError("din besked her") kaster en fejl
#   - Den der kalder funktionen kan fange den med except ValueError

def tjek_bool_tekst(tekst):
    """Konverterer 'True'/'False' til bool. Kaster ValueError ved ukendt tekst."""
    # TODO: if tekst.strip() == "True": return True
    # TODO: elif tekst.strip() == "False": return False
    # TODO: else: raise ValueError med en forklarende besked
    pass


# ── Opgave 4 ──────────────────────────────────────────────
# Implementer laes_brugere(filnavn) → list[dict]
#
# Læs brugere fra en CSV-fil.
# Returnér en liste af dicts hvor "aktiv" er en rigtig bool.
#
# Håndtér to slags fejl:
#   - Filen eksisterer ikke  →  print besked, returnér []
#   - "aktiv"-feltet er ugyldigt  →  print advarsel for den række,
#     spring den over og fortsæt (brug continue)
#
# Brug tjek_bool_tekst() inde i løkken til at konvertere aktiv-feltet.
# Pak kaldet ind i try/except ValueError.
#
# Hint:
#   - Ydre try/except: FileNotFoundError → return []
#   - Indre try/except inde i for-løkken: ValueError → continue

def laes_brugere(filnavn):
    """Indlæser brugere fra CSV med fejlhåndtering. Returnerer liste af dicts."""
    brugere = []
    # TODO: try/except FileNotFoundError rundt om hele blokken
    # TODO: åbn filen med csv.DictReader
    # TODO: for hver række: forsøg at konvertere aktiv med tjek_bool_tekst()
    #       ved ValueError: print advarsel og spring rækken over med continue
    # TODO: tilføj rækken (med konverteret aktiv) til brugere
    return brugere


# ─────────────────────────────────────────────────────────
def main():
    print("── Opgave 1: laes_fil ──")
    indhold = laes_fil(MAPPE / "brugere.csv")
    if indhold is not None:
        linjer = indhold.strip().split("\n")
        print(f"Læst {len(linjer)} linjer")
    else:
        print("Returnerede None som forventet")

    print()
    mangler = laes_fil(MAPPE / "UKENDT.csv")
    print("Manglende fil returnerede:", mangler)

    print("\n── Opgave 2: konverter_til_tal ──")
    for tekst in ["42", "abc", "3.14", "-7"]:
        resultat = konverter_til_tal(tekst)
        print(f"  '{tekst}'  →  {resultat}")

    print("\n── Opgave 3: tjek_bool_tekst ──")
    for tekst in ["True", "False", " True ", "ja", "1"]:
        try:
            vaerdi = tjek_bool_tekst(tekst)
            print(f"  '{tekst}'  →  {vaerdi} ({type(vaerdi).__name__})")
        except ValueError as e:
            print(f"  '{tekst}'  →  ValueError: {e}")

    print("\n── Opgave 4: laes_brugere ──")
    brugere = laes_brugere(MAPPE / "brugere.csv")
    print(f"Indlæst {len(brugere)} brugere")
    for b in brugere[:3]:
        print(f"  {b['navn']}  aktiv={b['aktiv']}  ({type(b['aktiv']).__name__})")

    print()
    mangler = laes_brugere(MAPPE / "UKENDT.csv")
    print("Manglende fil returnerede:", mangler)


if __name__ == "__main__":
    main()
