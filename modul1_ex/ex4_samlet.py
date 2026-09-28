"""
=============================================================
  MODUL 1  ·  Sprint 4  ·  Øvelse 4
  Samlet – Importér og brug dine egne moduler
=============================================================
Saml dit adgangskode-analyseværktøj i ét menu-drevet script.
Du importerer funktioner direkte fra de andre øvelsesfiler —
ingen kopiering, ingen mellemfil.

Struktur:
  ex4_samlet.py      ← dette script (main)
  ex2_loekker.py     ← tael_tegn, er_staerk
  ex3_funktioner.py  ← beregn_score, styrke_label, analyser,
                        generer_adgangskode

Menuen:
  1) Analyser én adgangskode (bruger taster selv)
  2) Analyser TESTKODEORD-listen
  3) Generér og analyser tilfældige kodeord
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


TESTKODEORD = [
    "hej123",
    "P@ssw0rd!",
    "Tr0ub4dor&3",
    "abc",
    "Sommer2024!",
    "K0rr3kt#Hest+Batteri",
]


# ── Opgave 2 ──────────────────────────────────────────────
# Implementer analyser_liste(kodeord_liste)
# Analyser hvert kodeord i listen og print resultatet som en tabel:
#
#   Kodeord                  Score  Label
#   ──────────────────────────────────────────
#   hej123                    0.40  Middel
#   P@ssw0rd!                 0.80  Meget stærk
#   ...
#
# Hint: brug analyser() på hvert kodeord i listen

def analyser_liste(kodeord_liste):
    pass  # TODO


# ── Opgave 3 ──────────────────────────────────────────────
# Implementer generer_og_analyser(antal=5)
# Generér 'antal' tilfældige kodeord og print en analyse af hvert.
#
# Hint: brug generer_adgangskode() og analyser()

def generer_og_analyser(antal=5):
    pass  # TODO


# ── Opgave 4 ──────────────────────────────────────────────
# Implementer kun_staerke(kodeord_liste)
# Returnér en ny liste med kun de kodeord der er stærke.
#
# Hint: brug er_staerk() fra ex2_loekker

def kun_staerke(kodeord_liste):
    pass  # TODO


# ─────────────────────────────────────────────────────────
def main():
    print("Adgangskode-analyseværktøj")
    print("─" * 32)

    while True:
        print("\n1) Analyser én adgangskode")
        print("2) Analyser TESTKODEORD-listen")
        print("3) Generér og analyser tilfældige kodeord")
        print("q) Afslut")
        valg = input("\nDit valg: ").strip().lower()

        if valg == "q":
            break

        elif valg == "1":
            kode = input("Adgangskode: ")
            rapport = analyser(kode)
            if rapport:
                for noegle, vaerdi in rapport.items():
                    print(f"  {noegle:<10}: {vaerdi}")

        elif valg == "2":
            analyser_liste(TESTKODEORD)

        elif valg == "3":
            generer_og_analyser()


main()
