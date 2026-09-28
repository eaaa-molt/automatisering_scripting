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
# Definer klassen Bruger med en __init__-metode.
#
# __init__ kaldes automatisk når man skriver: Bruger(...)
# Den modtager argumenter og skal gemme dem som attributter
# på objektet ved hjælp af self.
#
# Klassen skal have fire attributter:
#   navn      – str, brugerens fulde navn
#   email     – str, e-mail-adresse
#   afdeling  – str, hvilken afdeling
#   aktiv     – bool, er kontoen aktiv? (standardværdi: True)
#
# Hint: hver attribut tildeles med self.attribut = argument
#
# Når du er færdig, skal disse linjer virke uden fejl:
#   b = Bruger("Anna Jensen", "anna@firma.dk", "IT")
#   print(b.navn)      →  Anna Jensen
#   print(b.aktiv)     →  True

class Bruger:
    def __init__(self, navn, email, afdeling, aktiv=True):
        # TODO: gem hvert af de fire argumenter som en attribut på self
        pass


# ── Eksperimenter ─────────────────────────────────────────
# Kør disse linjer én ad gangen og observer outputtet.
# Fjern # for at aktivere ét ad gangen — sæt # tilbage igen bagefter.
#
# OBS: løs opgave 1 først, ellers virker eksperimenterne ikke.
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


# ── Opgave 2 ──────────────────────────────────────────────
# Opret tre Bruger-objekter med nedenstående data.
# Print derefter navn, e-mail og aktiv-status for alle tre.
#
# Data:
#   Anna Jensen    anna@firma.dk      IT        aktiv
#   Bjarne Nielsen bjarne@firma.dk    HR        aktiv
#   Cecilie Hansen cecilie@firma.dk   IT        inaktiv
#
# Forventet output (én linje pr. bruger):
#   Anna Jensen | anna@firma.dk | True
#   Bjarne Nielsen | bjarne@firma.dk | True
#   Cecilie Hansen | cecilie@firma.dk | False

def main():
    print("=== Opgave 2: Opret Bruger-objekter ===")
    # TODO: opret b1 (Anna Jensen)
    # TODO: opret b2 (Bjarne Nielsen)
    # TODO: opret b3 (Cecilie Hansen — husk at angive aktiv=False)

    # TODO: print navn, e-mail og aktiv-status for b1
    # TODO: print navn, e-mail og aktiv-status for b2
    # TODO: print navn, e-mail og aktiv-status for b3


    # ── Opgave 3 ──────────────────────────────────────────
    # Sæt de tre brugere i en liste kaldet 'brugere'.
    # Tilføj bagefter en fjerde bruger:
    #   Diana Larsen  diana@firma.dk  Økonomi  inaktiv
    # Print listens længde med len() til sidst.
    #
    # Forventet output:
    #   Antal brugere: 4

    print("\n=== Opgave 3: Liste og .append() ===")
    brugere = []  # TODO: erstat [] med de tre brugerobjekter

    # TODO: opret b4 (Diana Larsen) og tilføj til listen med .append()

    # TODO: print listens længde


    # ── Opgave 4 ──────────────────────────────────────────
    # Gå listen igennem med en for-løkke og print navn og
    # afdeling for hver bruger på formatet:
    #   <navn> — <afdeling>
    #
    # Forventet output:
    #   Anna Jensen — IT
    #   Bjarne Nielsen — HR
    #   Cecilie Hansen — IT
    #   Diana Larsen — Økonomi

    print("\n=== Opgave 4: For-løkke med navn og afdeling ===")
    for b in brugere:
        pass  # TODO: erstat pass med en print-linje


    # ── Opgave 5 ──────────────────────────────────────────
    # Brug en for-løkke til at tælle, hvor mange brugere
    # der er aktive, og hvor mange der er inaktive.
    # Print begge tal til sidst.
    #
    # Hint: opret to tælle-variable (fx aktive = 0) og brug
    #       if/else inde i løkken til at opdatere dem.
    #
    # Forventet output:
    #   Aktive: 2
    #   Inaktive: 2

    print("\n=== Opgave 5: Tæl aktive og inaktive ===")
    aktive = 0
    inaktive = 0
    # TODO: gå brugere igennem og opdater aktive / inaktive
    # TODO: print aktive
    # TODO: print inaktive


# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
