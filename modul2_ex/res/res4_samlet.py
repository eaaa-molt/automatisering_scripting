"""
=============================================================
  MODUL 2  ·  Sprint 4  ·  Øvelse 4  — LØSNING
  Samlet – Importér og brug dine egne cipher-funktioner
=============================================================
"""

from res1_caesar import caesar_afkod
from res2_substitution import subst_afkod
from res3_frekvens import tael_bogstaver, vis_frekvens


# ── Opgave 2 ──────────────────────────────────────────────
def vis_kortlaegning(noegle):
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("\nKortlægning (cipher → klar):")
    for i, cipher in enumerate(noegle.upper()):
        if cipher != '?':
            print(f"  Cipher {cipher}  →  Klar {alfabet[i]}")


# ── Opgave 3 ──────────────────────────────────────────────
def gaet_caesar_skift(tekst):
    antal = tael_bogstaver(tekst)
    if not antal:
        return 0
    hyppigste = max(antal, key=lambda b: antal[b])
    skift = (ord(hyppigste) - ord('E')) % 26
    return skift


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
