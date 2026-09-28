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

MAPPE = Path(__file__).parent.parent


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


def laes_fil(filnavn):
    """Forsøger at læse en fil. Returnerer indhold eller None."""
    try:
        with open(filnavn, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Filen '{filnavn}' blev ikke fundet.")
        return None


def konverter_til_tal(tekst):
    """Forsøger at konvertere tekst til int. Returnerer 0 ved fejl."""
    try:
        return int(tekst)
    except ValueError:
        print(f"Kan ikke konvertere '{tekst}' til heltal.")
        return 0


def tjek_bool_tekst(tekst):
    """Konverterer 'True'/'False' til bool. Kaster ValueError ved ukendt tekst."""
    if tekst.strip() == "True":
        return True
    elif tekst.strip() == "False":
        return False
    else:
        raise ValueError(f"Ukendt boolean-værdi: '{tekst}'")


def laes_brugere(filnavn):
    """Indlæser brugere fra CSV med fejlhåndtering. Returnerer liste af dicts."""
    brugere = []
    try:
        with open(filnavn, encoding="utf-8") as f:
            for raekke in csv.DictReader(f):
                try:
                    raekke["aktiv"] = tjek_bool_tekst(raekke["aktiv"])
                except ValueError as e:
                    print(f"Advarsel: springer '{raekke['navn']}' over — {e}")
                    continue
                brugere.append(raekke)
    except FileNotFoundError:
        print(f"Filen '{filnavn}' blev ikke fundet.")
        return []
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
