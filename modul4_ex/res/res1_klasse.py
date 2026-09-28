"""
=============================================================
  MODUL 4  ·  Sprint 1  ·  Øvelse 1
  Fra ordbog til klasse
=============================================================
Vi har tidligere brugt ordbøger til at samle data om en bruger:

  bruger = {
      "navn":      "Anna Jensen",
      "email":     "anna@firma.dk",
      "afdeling":  "IT",
      "aktiv":     True,
  }

En klasse giver os det samme — plus metoder og et fast format.
I dette modul bygger vi en Bruger-klasse trin for trin.
=============================================================
"""

from pathlib import Path

MAPPE = Path(__file__).parent


# ── Opgave 1 ──────────────────────────────────────────────
class Bruger:
    def __init__(self, navn, email, afdeling, aktiv=True):
        self.navn     = navn
        self.email    = email
        self.afdeling = afdeling
        self.aktiv    = aktiv


# ── Eksperimenter ─────────────────────────────────────────
# Kør disse linjer én ad gangen og observer outputtet.
# Fjern # for at aktivere ét ad gangen — sæt # tilbage igen bagefter.
#
# Eksperiment 1: Hvad er typen af et Bruger-objekt?
#   b = Bruger("Anna Jensen", "anna@firma.dk", "IT")
#   print(type(b))
#   → <class '__main__.Bruger'>
#
# Eksperiment 2: Hvad hedder klassen som tekst?
#   b = Bruger("Anna Jensen", "anna@firma.dk", "IT")
#   print(b.__class__.__name__)
#   → Bruger
#
# Eksperiment 3: Er b en instans af Bruger?
#   b = Bruger("Anna Jensen", "anna@firma.dk", "IT")
#   print(isinstance(b, Bruger))
#   → True
#
# Eksperiment 4: Hvad indeholder objektet?
#   b = Bruger("Anna Jensen", "anna@firma.dk", "IT")
#   print(b.__dict__)
#   → {'navn': 'Anna Jensen', 'email': 'anna@firma.dk',
#      'afdeling': 'IT', 'aktiv': True}
# ─────────────────────────────────────────────────────────


def main():
    print("=== Opgave 2: Opret Bruger-objekter ===")
    b1 = Bruger("Anna Jensen",    "anna@firma.dk",    "IT")
    b2 = Bruger("Bjarne Nielsen", "bjarne@firma.dk",  "HR")
    b3 = Bruger("Cecilie Hansen", "cecilie@firma.dk", "IT", aktiv=False)

    print(f"{b1.navn} | {b1.email} | {b1.aktiv}")
    print(f"{b2.navn} | {b2.email} | {b2.aktiv}")
    print(f"{b3.navn} | {b3.email} | {b3.aktiv}")

    print("\n=== Opgave 3: Liste og .append() ===")
    brugere = [b1, b2, b3]
    b4 = Bruger("Diana Larsen", "diana@firma.dk", "Økonomi", aktiv=False)
    brugere.append(b4)
    print(f"Antal brugere: {len(brugere)}")

    print("\n=== Opgave 4: For-løkke med navn og afdeling ===")
    for b in brugere:
        print(f"{b.navn} — {b.afdeling}")

    print("\n=== Opgave 5: Tæl aktive og inaktive ===")
    aktive = 0
    inaktive = 0
    for b in brugere:
        if b.aktiv:
            aktive += 1
        else:
            inaktive += 1
    print(f"Aktive: {aktive}")
    print(f"Inaktive: {inaktive}")


# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
