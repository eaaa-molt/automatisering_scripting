"""
=============================================================
  MODUL 2  ·  Sprint 1  ·  Øvelse 1  — LØSNING
  Caesar-cipher – enkod og afkod
=============================================================
"""

CHIFFERTEKST = "Wfaovu ly la ryhmambska chhilu p jfilyzprrlyolk. Mpuk mshnla: LH_HHYOBZ_2025"


# ── Opgave 1 ──────────────────────────────────────────────
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
SKIFT = 7


# ── Opgave 3 (Bonus) ──────────────────────────────────────
def caesar_enkod(tekst, skift):
    resultat = ""
    for tegn in tekst:
        if tegn.isupper():
            nyt_tegn = chr((ord(tegn) - ord('A') + skift) % 26 + ord('A'))
            resultat += nyt_tegn
        elif tegn.islower():
            nyt_tegn = chr((ord(tegn) - ord('a') + skift) % 26 + ord('a'))
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

    print()
    test = caesar_afkod(caesar_enkod("HEMMELIG", SKIFT), SKIFT)
    print(f"Bonus – verificering: {test}")


main()