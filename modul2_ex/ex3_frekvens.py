"""
=============================================================
  MODUL 2  ·  Sprint 3  ·  Øvelse 3
  Frekvensanalyse – find mønstret i chifferteksten
=============================================================
Når vi ikke kender nøglen, kan vi gætte os frem ved at se på
hvilke bogstaver der optræder hyppigst.

I engelsk tekst er de hyppigste bogstaver (top 6):
  E  T  A  O  I  N

Flagformatet er picoCTF{...}
Fra chiffertekstens slutning "cbzjZWD{..." kan vi aflæse:
  c→p,  b→i,  z→c,  j→o,  Z→C,  W→T,  D→F

Din opgave: brug disse hints + frekvensanalyse til at afkode teksten.
=============================================================
"""

ALFABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

CHIFFERTEKST = (
    "ZWDg (gejfw djf zacwpfx wex dqar) afx a wscx jd zjicpwxf gxzpfbws zjicxwbwbjv. "
    "Zjvwxgwavwg afx cfxgxvwxm hbwe a gxw jd zeaqqxvrxg hebze wxgw wexbf zfxawbybws, "
    "wxzevbzaq (avm rjjrqbvr) gnbqqg, avm cfjtqxi-gjqybvr atbqbws. Zeaqqxvrxg pgpaqqs "
    "zjyxf a vpitxf jd zawxrjfbxg, avm hexv gjqyxm, xaze sbxqmg a gwfbvr (zaqqxm a dqar) "
    "hebze bg gptibwwxm wj av jvqbvx gzjfbvr gxfybzx. ZWDg afx a rfxaw has wj qxafv a "
    "hbmx affas jd zjicpwxf gxzpfbws gnbqqg bv a gadx, qxraq xvybfjvixvw, avm afx ejgwxm "
    "avm cqasxm ts iavs gxzpfbws rfjpcg afjpvm wex hjfqm djf dpv avm cfazwbzx. Djf webg "
    "cfjtqxi, wex dqar bg: cbzjZWD{DF3LP3VZS_4774ZN5_4F3_Z001_4871X6DT}"
)


# ── Pre-leveret funktion – du behøver ikke ændre noget her ──
# Afkoder tekst med noegle; skriver '_' for bogstaver der endnu ikke er kortlagt.
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
                resultat += tegn.upper()
        else:
            resultat += tegn
    return resultat


# ── Opgave 1 ──────────────────────────────────────────────
# Implementer tael_bogstaver(tekst)
# Tæl hvor mange gange hvert bogstav optræder (ignorer alt andet).
# Returnér en dict, fx: {'A': 12, 'B': 3, ...}
#
# Hint: brug tegn.upper() så store og små bogstaver tælles samlet
# Hint: antal[tegn] = antal.get(tegn, 0) + 1  øger tælleren for tegnet

def tael_bogstaver(tekst):
    antal = {}
    for tegn in tekst.upper():
        if tegn.isalpha():
            pass  # TODO
    return antal


# ── Opgave 2 ──────────────────────────────────────────────
# Implementer vis_frekvens(tekst)
# Print de 6 hyppigste bogstaver og deres procentvise forekomst.
#
# Hint: sorted(antal, key=lambda b: antal[b], reverse=True) sorterer
#       bogstaverne fra hyppigst til sjældnest

def vis_frekvens(tekst):
    antal   = tael_bogstaver(tekst)
    if not antal:
        print("  (tael_bogstaver() ikke implementeret endnu)")
        return
    total   = sum(antal.values())
    sorteret = []  # TODO: sorter bogstaverne fra hyppigst til sjældnest

    print(f"\n{'Bogstav':>8}  {'Antal':>6}  {'Procent':>8}")
    print("-" * 28)
    for bogstav in sorteret[:6]:
        pct = antal[bogstav] / total * 100
        print(f"{bogstav:>8}  {antal[bogstav]:>6}  {pct:>7.1f}%")

    print("\nEngelsk top-6: E  T  A  O  I  N")


# ── Opgave 3 ──────────────────────────────────────────────
# Udvid 'kendte'-dicten i byg_noegle_fra_hints() med flere bogstaver.
# Brug frekvenstabellen: hyppige cipher-bogstaver svarer sandsynligvis
# til E, T, A, O, I, N i klarteksten.
#
# Arbejdsgangen:
#   1. Kør scriptet og se frekvenstabellen
#   2. Gæt et nyt bogstav og tilføj det til 'kendte'
#   3. Kør igen og se om teksten giver mere mening
#   4. Gentag til du kan læse hele teksten

def byg_noegle_fra_hints():
    noegle = ['?'] * 26

    # Kendte mappinger fra flagformatet (klar → cipher):
    kendte = {
        'P': 'C',
        'I': 'B',
        'C': 'Z',
        'O': 'J',
        'T': 'W',
        'F': 'D',
        'E': 'X',
        # TODO: tilføj flere kendte bogstaver her, fx:
        # 'E': 'X',
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
