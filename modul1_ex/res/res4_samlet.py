"""
=============================================================
  MODUL 1  ·  Sprint 4  ·  Øvelse 4  — LØSNING
  Samlet – Importér og brug dine egne moduler
=============================================================
"""

from ex2_loekker import tael_tegn, er_staerk
from ex3_funktioner import beregn_score, styrke_label, analyser, generer_adgangskode


TESTKODEORD = [
    "hej123",
    "P@ssw0rd!",
    "Tr0ub4dor&3",
    "abc",
    "Sommer2024!",
    "K0rr3kt#Hest+Batteri",
]


# ── Opgave 2 ──────────────────────────────────────────────
def analyser_liste(kodeord_liste):
    print(f"\n  {'Kodeord':<24} {'Score':>5}  Label")
    print("  " + "─" * 42)
    for kode in kodeord_liste:
        rapport = analyser(kode)
        print(f"  {kode:<24} {rapport['score']:>5.2f}  {rapport['label']}")


# ── Opgave 3 ──────────────────────────────────────────────
def generer_og_analyser(antal=5):
    print(f"\n  {'Kodeord':<24} {'Score':>5}  Label")
    print("  " + "─" * 42)
    for _ in range(antal):
        kode = generer_adgangskode()
        rapport = analyser(kode)
        print(f"  {kode:<24} {rapport['score']:>5.2f}  {rapport['label']}")


# ── Opgave 4 ──────────────────────────────────────────────
def kun_staerke(kodeord_liste):
    return [kode for kode in kodeord_liste if er_staerk(kode)]


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
