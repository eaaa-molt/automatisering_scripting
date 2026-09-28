"""
=============================================================
  MODUL 1  ·  Sprint 3  ·  Øvelse 3
  Funktioner
=============================================================
Vi bygger et komplet analyse-bibliotek til adgangskoder.
Funktionerne herfra genbruges i Øvelse 4.

En styrke-score beregnes ud fra fem kriterier:
  1. Længde ≥ 12 tegn           (+0.20)
  2. Mindst 1 stort bogstav     (+0.20)
  3. Mindst 1 lille bogstav     (+0.20)
  4. Mindst 1 ciffer            (+0.20)
  5. Mindst 1 specialtegn       (+0.20)
=============================================================
"""

import random
import string


# ── Pre-leveret funktion – du behøver ikke ændre noget her ──
# Genbruger logikken fra Øvelse 2.
def tael_tegn(kodeord):
    """Returnerer dict med antal store/små/cifre/specielle tegn."""
    antal = {'stort': 0, 'lille': 0, 'ciffer': 0, 'specielt': 0}
    for tegn in kodeord:
        if tegn.isupper():
            antal['stort'] += 1
        elif tegn.islower():
            antal['lille'] += 1
        elif tegn.isdigit():
            antal['ciffer'] += 1
        else:
            antal['specielt'] += 1
    return antal


# ── Opgave 1 ──────────────────────────────────────────────
# Skriv beregn_score(kodeord) der returnerer en float 0.0–1.0.
# Hvert af de fem kriterier øverst i filen giver +0.20.
#
# Hint: start med score = 0.0 og læg til for hvert opfyldt kriterie
# Hint: brug tael_tegn() til at hente antal af hver type

def beregn_score(kodeord):
    pass  # TODO


# ── Opgave 2 ──────────────────────────────────────────────
# Skriv styrke_label(score) der returnerer:
#   0.0–0.4   →  "Svag"
#   0.4–0.6   →  "Middel"
#   0.6–0.8   →  "Stærk"
#   0.8–1.0   →  "Meget stærk"

def styrke_label(score):
    pass  # TODO


# ── Opgave 3 ──────────────────────────────────────────────
# Skriv analyser(kodeord) der returnerer en dict med:
#   'kodeord'  →  selve kodeordet (str)
#   'laengde'  →  antal tegn (int)
#   'tegn'     →  resultat fra tael_tegn() (dict)
#   'score'    →  resultat fra beregn_score() (float)
#   'label'    →  resultat fra styrke_label() (str)
#
# Hint: kald dine egne funktioner inde i analyser()

def analyser(kodeord):
    pass  # TODO


# ── Opgave 4 (Bonus) ──────────────────────────────────────
# Skriv generer_adgangskode(laengde=12, specialtegn=True)
# der genererer et tilfældigt kodeord der består af:
#   - store og små bogstaver  (string.ascii_letters)
#   - cifre                   (string.digits)
#   - specialtegn, hvis True  (string.punctuation)
#
# Hint: random.choices(population, k=laengde) trækker k tegn
# Hint: ''.join(liste) sætter en liste af tegn sammen til en streng

def generer_adgangskode(laengde=12, specialtegn=True):
    pass  # TODO


# ─────────────────────────────────────────────────────────
TESTKODER = ["hej123", "P@ssw0rd!", "Tr0ub4dor&3", "abc", "Sommer2024!", "K0rr3kt#Hest+Batteri"]


def main():
    print("=== Opgave 1+2: Score og label ===")
    for kode in TESTKODER:
        s = beregn_score(kode)
        print(f"  {kode:<22}  score={s}  →  {styrke_label(s)}")

    print("\n=== Opgave 3: Fuld analyse ===")
    rapport = analyser("P@ssw0rd!")
    if rapport:
        for noegle, vaerdi in rapport.items():
            print(f"  {noegle:<10}: {vaerdi}")

    print("\n=== Opgave 4 (Bonus): Generér kodeord ===")
    for _ in range(3):
        kode = generer_adgangskode()
        if kode:
            s = beregn_score(kode)
            print(f"  {kode:<20}  →  {styrke_label(s)}")


main()
