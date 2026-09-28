"""
=============================================================
  MODUL 1  ·  Sprint 3  ·  Øvelse 3  — LØSNING
  Funktioner
=============================================================
"""

import random
import string


# ── Pre-leveret funktion ──────────────────────────────────
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
def beregn_score(kodeord):
    score = 0.0
    antal = tael_tegn(kodeord)
    if len(kodeord) >= 12:
        score += 0.20
    if antal['stort'] >= 1:
        score += 0.20
    if antal['lille'] >= 1:
        score += 0.20
    if antal['ciffer'] >= 1:
        score += 0.20
    if antal['specielt'] >= 1:
        score += 0.20
    return round(score, 2)


# ── Opgave 2 ──────────────────────────────────────────────
def styrke_label(score):
    if score <= 0.4:
        return "Svag"
    elif score <= 0.6:
        return "Middel"
    elif score <= 0.8:
        return "Stærk"
    else:
        return "Meget stærk"


# ── Opgave 3 ──────────────────────────────────────────────
def analyser(kodeord):
    score = beregn_score(kodeord)
    return {
        'kodeord': kodeord,
        'laengde': len(kodeord),
        'tegn':    tael_tegn(kodeord),
        'score':   score,
        'label':   styrke_label(score),
    }


# ── Opgave 4 (Bonus) ──────────────────────────────────────
def generer_adgangskode(laengde=12, specialtegn=True):
    tegn = string.ascii_letters + string.digits
    if specialtegn:
        tegn += string.punctuation
    return ''.join(random.choices(tegn, k=laengde))


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
