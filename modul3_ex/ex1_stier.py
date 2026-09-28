"""
=============================================================
  MODUL 3  ·  Sprint 1  ·  Øvelse 1
  Stier og tekstfiler
=============================================================
Python kan arbejde med filer på din computer.
For at finde de rigtige filer skal vi bruge filstier.

  MAPPE = Path(__file__).parent

Denne linje giver os stien til mappen scriptet ligger i.
Vi bruger den til at finde andre filer i samme mappe — det
gør scriptet robust uanset hvor på computeren det kører.

I denne øvelse lærer vi at skrive til og læse fra tekstfiler.
=============================================================
"""

from pathlib import Path

MAPPE = Path(__file__).parent


# ── Eksperimenter ─────────────────────────────────────────
# Kør disse linjer én ad gangen og observer outputtet.
# Fjern # for at aktivere:
#
# Eksperiment 1: Hvad er MAPPE?
# print(MAPPE)
#
# Eksperiment 2: Eksisterer mappen?
print(MAPPE.exists())
#
# Eksperiment 3: Hvad er der i mappen?
for f in MAPPE.iterdir():
    print(f.name)
#
# Eksperiment 4: Byg en filsti med /
#   fil = MAPPE / "test.txt"
#   print(fil)
#   print(fil.exists())   # eksisterer filen endnu?
# ─────────────────────────────────────────────────────────


# ── Opgave 1 ──────────────────────────────────────────────
# Skriv en liste af navne til filen "navne.txt".
# Ét navn per linje.
#
# Navne der skal skrives:
#   Anna Jensen, Bjarne Nielsen, Cecilie Hansen,
#   Diana Larsen, Esben Madsen
#
# Fremgangsmåde:
#   1. Opbyg filstien med MAPPE / "navne.txt"
#   2. Åbn filen til skrivning med open(..., "w", encoding="utf-8")
#   3. Brug with-blokken (filen lukkes automatisk bagefter)
#   4. Skriv hvert navn med f.write(navn + "\n")
#      Husk \n for at starte en ny linje efter hvert navn
#
# Når du er færdig, åbn navne.txt i en teksteditor og tjek indholdet.

def skriv_navne():
    navne = [
        "Anna Jensen",
        "Bjarne Nielsen",
        "Cecilie Hansen",
        "Diana Larsen",
        "Esben Madsen",
    ]
    # TODO: åbn filen til skrivning med "w" og encoding="utf-8"
    # TODO: gå navne igennem og skriv hvert navn med \n til sidst
    pass


# ── Opgave 2 ──────────────────────────────────────────────
# Læs "navne.txt" og print alle navne.
# Brug .strip() på hver linje for at fjerne linjeskift (\n).
#
# Forventet output:
#   Anna Jensen
#   Bjarne Nielsen
#   Cecilie Hansen
#   Diana Larsen
#   Esben Madsen

def vis_navne():
    # TODO: åbn filen til læsning med "r" (eller udelad mode — "r" er standard)
    # TODO: gå filen igennem linje for linje i en for-løkke
    # TODO: print hver linje — husk .strip() for at fjerne \n
    pass


# ── Opgave 3 ──────────────────────────────────────────────
# Tæl hvor mange navne der er i filen.
# Print antallet til sidst.
#
# Hint: du kan bruge en tæller-variabel i løkken,
#       eller bruge readlines() til at få en liste af linjer.
#
# Forventet output:
#   Antal navne: 5

def taеl_navne():
    antal = 0
    # TODO: åbn filen og tæl linjerne
    # TODO: print antallet
    pass


# ── Opgave 4 ──────────────────────────────────────────────
# Tilføj to nye navne til filen uden at slette dem der allerede er der.
# Brug tilstand "a" (append) i stedet for "w".
#
# Nye navne: "Freja Olsen" og "Gorm Poulsen"
#
# Kald bagefter taеl_navne() og tjek at antallet nu er 7.

def tilfoej_navne():
    nye_navne = ["Freja Olsen", "Gorm Poulsen"]
    # TODO: åbn filen med "a" (append) og encoding="utf-8"
    # TODO: skriv de to nye navne
    pass


# ── Opgave 5 ──────────────────────────────────────────────
# Søg i filen efter navne der indeholder søgeordet "Nielsen".
# Print alle matchende navne.
# Print også en besked hvis ingen navne matcher.
#
# Hint: brug "søgeord in linje" som betingelse i if-sætningen
#
# Forventet output:
#   Fundet: Bjarne Nielsen

def soeg_i_fil(soegeord):
    fundet = []
    # TODO: åbn filen og gå linjerne igennem
    # TODO: tilføj linjen til fundet-listen hvis soegeord er i den (husk .strip())
    # TODO: print de fundne navne, eller en besked om at ingen matchede
    pass


# ─────────────────────────────────────────────────────────
def main():
    print("── Opgave 1: skriv navne ──")
    skriv_navne()
    print("Skrevet til navne.txt\n")

    print("── Opgave 2: vis navne ──")
    vis_navne()

    print("\n── Opgave 3: tæl navne ──")
    taеl_navne()

    print("\n── Opgave 4: tilføj navne ──")
    tilfoej_navne()
    taеl_navne()   # forventet: 7

    print("\n── Opgave 5: søg ──")
    soeg_i_fil("Nielsen")
    soeg_i_fil("Hansen")
    soeg_i_fil("Mortensen")   # ingen match


if __name__ == "__main__":
    main()
