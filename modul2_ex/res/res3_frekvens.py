"""
=============================================================
  MODUL 2  ·  Sprint 3  ·  Øvelse 3  — LØSNING
  Frekvensanalyse – find mønstret i chifferteksten
=============================================================
"""

ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

CHIFFERTEKST = (
    "P shifypualu hm oqlyaly ly kla prrl klu obyapnzal clq, tlu klu kly møslz zvt oqlt, kly møyly kpn aps klu lulzal. Mvy uåy zaqlyulyul ocpzrly kpa uhcu, clk kb, ha éu zqæs ohy sfaala olsl apklu. Shk tpn ahnl tlk kpn wå kpu ylqzl mvy kb ly MPYL{Tpu-Lulzal-Lul}"
)


# ── Pre-leveret funktion ──────────────────────────────────
def subst_afkod(tekst, noegle):
    resultat = ""
    for tegn in tekst:
        if tegn.isalpha():
            stor = tegn.upper()
            if stor in noegle.upper():
                position = noegle.upper().index(stor)
                klartegn = ALFABET[position]
                if tegn.islower():
                    klartegn = klartegn.lower()
                resultat += klartegn
            else:
                resultat += "_"
        else:
            resultat += tegn
    return resultat


# ── Opgave 1 ──────────────────────────────────────────────
def tael_bogstaver(tekst):
    antal = {}
    for tegn in tekst.upper():
        if tegn.isalpha():
            antal[tegn] = antal.get(tegn, 0) + 1
    return antal


# ── Opgave 2 ──────────────────────────────────────────────
def vis_frekvens(tekst):
    antal   = tael_bogstaver(tekst)
    if not antal:
        print("  (tael_bogstaver() ikke implementeret endnu)")
        return
    total   = sum(antal.values())
    sorteret = sorted(antal, key=lambda b: antal[b], reverse=True)

    print(f"\n{'Bogstav':>8}  {'Antal':>6}  {'Procent':>8}")
    print("-" * 28)
    for bogstav in sorteret[:6]:
        pct = antal[bogstav] / total * 100
        print(f"{bogstav:>8}  {antal[bogstav]:>6}  {pct:>7.1f}%")

    print("\nEngelsk top-6: E  T  A  O  I  N")


# ── Opgave 3 ──────────────────────────────────────────────
def byg_noegle_fra_hints():
    noegle = ['?'] * 26

    kendte = {
        # Fra flagformatet
        'P': 'C', 'I': 'B', 'C': 'Z', 'O': 'J', 'T': 'W', 'F': 'D',
        # Fra frekvensanalyse + kontekst
        'S': 'G', 'H': 'E', 'R': 'F', 'A': 'A', 'E': 'X', 'L': 'Q',
        'G': 'R', 'Y': 'S', 'U': 'P', 'N': 'V', 'M': 'I', 'D': 'M',
        'W': 'H', 'K': 'N', 'V': 'Y', 'B': 'T', 'Q': 'L',
    }

    for klar, cipher in kendte.items():
        position = ALFABET.index(klar)
        noegle[position] = cipher

    return noegle


# ─────────────────────────────────────────────────────────
def main():
    print("=== Opgave 1+2: Bogstavfrekvenser ===")
    vis_frekvens(CHIFFERTEKST)

    noegle     = byg_noegle_fra_hints()
    noegle_str = ''.join(noegle)

    print(f"\nNøgle så langt: {noegle_str}")
    print("\n=== Opgave 3: Delvist afkodet tekst ===")
    print(subst_afkod(CHIFFERTEKST, noegle_str))


main()
