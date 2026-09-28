"""
=============================================================
  MODUL 2  ·  Sprint 4  ·  Øvelse 4
  Samlet – Importér og brug dine egne cipher-funktioner
=============================================================
Saml dit cipher-bibliotek i ét menu-drevet script.
Du importerer funktioner direkte fra de andre øvelsesfiler.

Struktur:
  ex4_samlet.py    ← dette script
  ex1_caesar.py    ← caesar_afkod, caesar_enkod
  ex2_substitution.py ← subst_afkod, subst_enkod
  ex3_frekvens.py  ← tael_bogstaver, vis_frekvens

Menuen:
  1) Caesar-afkod en tekst
  2) Substitution-afkod en tekst
  3) Vis bogstavfrekvenser
  q) Afslut
=============================================================
"""

# ── Opgave 1 ──────────────────────────────────────────────
# Importér funktionerne nedenfor fra de rette øvelsesfiler.
#
# Hint: en .py-fil i samme mappe kan importeres som et modul
# Hint: du behøver ikke importere alle funktioner – kun dem du bruger
# Hint: from <filnavn> import <funktion1>, <funktion2>

# TODO: skriv dine import-linjer her


# ── Opgave 2 ──────────────────────────────────────────────
# Implementer vis_kortlaegning(noegle)
# Print en oversigt over hvilke cipher-bogstaver der svarer til hvilke klarbogstaver.
# Format (én linje per bogstav der er kortlagt):
#
#   Cipher X  →  Klar E
#   Cipher G  →  Klar T
#   ...
#
# Hint: brug enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ") til at løbe igennem nøglen
# Hint: spring bogstaver over der er '?' (endnu ikke kortlagt)

def vis_kortlaegning(noegle):
    pass  # TODO


# ── Opgave 3 ──────────────────────────────────────────────
# Implementer gaet_caesar_skift(tekst)
# Find det mest sandsynlige Caesar-skift automatisk.
#
# Fremgangsmåde: E er det hyppigste bogstav i engelsk tekst.
#   Det hyppigste bogstav i chifferteksten svarer sandsynligvis til E.
#   skift = (ord(hyppigste_bogstav) - ord('E')) % 26
#
# Returnér skiftet som int.
#
# Hint: brug tael_bogstaver() fra ex3_frekvens
# Hint: max(antal, key=lambda b: antal[b]) giver det hyppigste bogstav

def gaet_caesar_skift(tekst):
    return 0  # TODO: erstat med korrekt beregning


# ─────────────────────────────────────────────────────────
def main():
    print("Cipher-analyseværktøj")
    print("─" * 32)

    while True:
        print("\n1) Caesar-afkod en tekst")
        print("2) Substitution-afkod en tekst")
        print("3) Vis bogstavfrekvenser")
        print("q) Afslut")
        valg = input("\nDit valg: ").strip().lower()

        if valg == "q":
            break

        elif valg == "1":
            tekst = input("Chiffertekst: ")
            skift = gaet_caesar_skift(tekst)
            print(f"Gættet skift: {skift}")
            resultat = caesar_afkod(tekst, skift)
            print(f"Afkodet: {resultat}")

        elif valg == "2":
            tekst  = input("Chiffertekst: ")
            noegle = input("Nøgle (26 bogstaver): ").strip().upper()
            if len(noegle) == 26:
                print(f"Afkodet: {subst_afkod(tekst, noegle)}")
                vis_kortlaegning(noegle)
            else:
                print("Nøglen skal være præcis 26 bogstaver.")

        elif valg == "3":
            tekst = input("Tekst til frekvensanalyse: ")
            vis_frekvens(tekst)


main()
