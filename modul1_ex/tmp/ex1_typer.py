"""
=============================================================
  MODUL 1  ·  Sprint 1  ·  Øvelse 1
  Variabler & Datatyper
=============================================================
Vi logger oplysninger om en adgangskode.
Hvert stykke information skal gemmes i den rette Python-type.

  Information    Python-type   Eksempel
  -----------------------------------------
  selve koden    str           "P@ssw0rd!"
  længde         int           9
  styrke-score   float         0.75
  godkendt       bool          True

Din opgave: opret variablerne, print dem pænt, og
lær hvordan Python håndterer typekonvertering.
=============================================================
"""


# ── Opgave 1 ──────────────────────────────────────────────
# Opret de fire variabler herunder med passende værdier.

kodeord  = "P@ssword"      # TODO: vælg en adgangskode som streng
laengde  = len(kodeord)       # TODO: brug len() på kodeord
score    = 0.8     # TODO: gæt en score mellem 0.0 og 1.0
godkendt = True


# ── Opgave 2 ──────────────────────────────────────────────
# Skriv print_typer() der printer type() for alle fire variabler.
#
# Hvad returnerer isinstance(True, int)?
# Skriv en kommentar i koden der forklarer resultatet.

def print_typer():
    print(type(kodeord))
    print(type(laengde))
    print(type(score))
    print(type(godkendt))


# ── Opgave 3 ──────────────────────────────────────────────
# En bruger har tastet kode-længden som tekst: "12"
# Skriv konverter_laengde(laengde_str) der:
#   1. Konverterer strengen til int
#   2. Returnerer resultatet
#   3. Returnerer None hvis konverteringen fejler
#
# Hint: int() konverterer en streng til heltal,
#       men ikke alle strenge er gyldige tal

def konverter_laengde(laengde_str):
    try:
        return int(laengde_str)
    except ValueError:
        return None

   
# ── Opgave 4 ──────────────────────────────────────────────
# Skriv bool_fra_tekst(tekst) der konverterer tekststrenge til bool:
#   "true",  "ja",  "1"→  True
#   "false", "nej", "0"   →  False
#   alt andet             →  None
#
# Hint: str har en metode der konverterer til lowercase
# Hint: en if/elif-kæde med in-operatoren virker fint her

def bool_fra_tekst(tekst):
    t = tekst.lower()
    if t in ("true",  "ja",  "1"):
        return True
    elif t in ("false", "nej", "0"):
        return False
    else:
        return None


# ── Opgave 5 ──────────────────────────────────────────────
# Udskriv de fire variabler med én f-string i dette format:
#
#   Kode: P@ssw0rd!  |  Længde: 9  |  Score: 0.75  |  Godkendt: True

print(f"Kode: {kodeord}  |  Længde: {laengde}  |  Score: {score}  |  Godkendt: {godkendt}")


# ─────────────────────────────────────────────────────────
def main():
    print("=== Opgave 2: Typer ===")
    print_typer()

    print("\n=== Opgave 3: Konvertering ===")
    for s in ["12", "8", "ikke-et-tal", "", "0"]:
        print(f"  konverter_laengde({s!r}) = {konverter_laengde(s)}")

    print("\n=== Opgave 4: Bool fra tekst ===")
    for s in ["true", "False", "ja", "nej", "1", "0", "måske"]:
        print(f"  bool_fra_tekst({s!r}) = {bool_fra_tekst(s)}")


main()
