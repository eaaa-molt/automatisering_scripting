"""
=============================================================
  MODUL 2  ·  Sprint 1  ·  Øvelse 1
  Caesar-cipher – enkod og afkod
=============================================================
En Caesar-cipher forskyller hvert bogstav et fast antal pladser
i alfabetet.  Shift 3: A→D, B→E, C→F  ...  Z→C

Eksempel (skift 3):
  Klar:   HELLO
  Cipher: KHOOR

Din opgave: implementer afkodning og find det rigtige skift.
=============================================================
"""

CHIFFERTEKST = "Wfaovu ly la ryhmambska chhilu p jfilyzprrlyolk. Mpuk mshnla: LH_HHYOBZ_2025"


# ── Opgave 1 ──────────────────────────────────────────────
# Implementer caesar_afkod(tekst, skift)
#
# For hvert tegn i tekst:
#   - Er det et stort bogstav?  →  skub det BAGLÆNS med skift pladser
#   - Er det et lille bogstav?  →  samme logik, men med lille alfabet
#   - Ellers?                   →  behold tegnet som det er
#
# Hint: (ord(tegn) - base - skift) % 26 + base giver det nye tegn
# Hint: base = ord('A') for store bogstaver, ord('a') for små

def caesar_afkod(tekst, skift):
    resultat = ""
    for tegn in tekst:
        if tegn.isupper():
            nyt_tegn = chr((ord(tegn) - ord('A') - skift) % 26 + ord('A'))
            resultat += nyt_tegn
        elif tegn.islower():
            nyt_tegn = chr((ord(tegn) - ord('a') - skift) % 26 + ord('a'))
            resultat += nyt_tegn
        else:
            resultat += tegn
    return resultat


# ── Opgave 2 ──────────────────────────────────────────────
# Find det rigtige skift og sæt det ind i variablen nedenfor.
# Fjern kommentarmarkeringen ved brute_force() nederst i filen
# for at prøve alle 26 muligheder – hvilket skift giver dansk tekst?

SKIFT = 7  # TODO: sæt det rigtige skift her


# ── Opgave 3 (Bonus) ──────────────────────────────────────
# Implementer caesar_enkod(tekst, skift) – det modsatte af afkod.
# Verificer: caesar_afkod(caesar_enkod("HEMMELIG", 7), 7) == "HEMMELIG"

def caesar_enkod(tekst, skift):
    resultat = ""
    for tegn in tekst:
        if tegn.isupper():
            nyt_tegn = tegn  # TODO
            resultat += nyt_tegn
        elif tegn.islower():
            nyt_tegn = tegn  # TODO
            resultat += nyt_tegn
        else:
            resultat += tegn
    return resultat


# ─────────────────────────────────────────────────────────
def brute_force():
    print("=== Brute force (alle 26 skift) ===")
    for s in range(26):
        print(f"Skift {s:2d}: {caesar_afkod(CHIFFERTEKST, s)}")


def main():
    print("Chiffertekst:")
    print(CHIFFERTEKST)
    print()

    klartekst = caesar_afkod(CHIFFERTEKST, SKIFT)
    print(f"Afkodet tekst (skift={SKIFT}):")
    print(klartekst)


main()
# Fjern kommentarmarkering nedenfor for at køre brute force:
# brute_force()
