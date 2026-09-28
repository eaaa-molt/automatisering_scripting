"""
=============================================================
  MODUL 4  ·  Sprint 2  ·  Øvelse 2
  Metoder og __str__
=============================================================
En metode er en funktion der er defineret inde i en klasse.
Den har altid 'self' som første parameter, som er en reference
til det konkrete objekt metoden kaldes på.

  b = Bruger("Anna Jensen", "anna@firma.dk", "IT")
  b.deaktiver()      ←  kalder metoden på b
  print(b.aktiv)     →  False

I denne øvelse udvider vi Bruger-klassen med fem metoder.
=============================================================
"""

from pathlib import Path

MAPPE = Path(__file__).parent


class Bruger:
    def __init__(self, navn, email, afdeling, aktiv=True):
        self.navn      = navn
        self.email     = email
        self.afdeling  = afdeling
        self.aktiv     = aktiv

    def vis_info(self):
        status = "Aktiv" if self.aktiv else "Inaktiv"
        print(f"Navn:      {self.navn}")
        print(f"E-mail:    {self.email}")
        print(f"Afdeling:  {self.afdeling}")
        print(f"Status:    {status}")

    def deaktiver(self):
        if not self.aktiv:
            print(f"{self.navn} er allerede inaktiv.")
        else:
            self.aktiv = False
            print(f"{self.navn} er nu deaktiveret.")

    def skift_email(self, ny_email):
        gammel_email = self.email
        self.email = ny_email
        print(f"E-mail opdateret: {gammel_email} → {ny_email}")

    def __str__(self):
        status = "aktiv" if self.aktiv else "inaktiv"
        return f"Bruger({self.navn}, {self.afdeling}, {status})"

    def skift_afdeling(self, ny_afdeling):
        gammel = self.afdeling
        self.afdeling = ny_afdeling
        print(f"Afdeling opdateret: {gammel} → {ny_afdeling}")


def main():
    b = Bruger("Anna Jensen", "anna@firma.dk", "IT")

    print("=== Opgave 1: vis_info ===")
    b.vis_info()

    print("\n=== Opgave 2: deaktiver (første gang) ===")
    b.deaktiver()
    print("aktiv er nu:", b.aktiv)

    print("\n=== Opgave 2: deaktiver (anden gang) ===")
    b.deaktiver()   # skal printe at brugeren allerede er inaktiv

    print("\n=== Opgave 3: skift_email ===")
    b.skift_email("anna.jensen@nytfirma.dk")
    print("email er nu:", b.email)

    print("\n=== Opgave 4: __str__ ===")
    print(b)

    print("\n=== Opgave 5: skift_afdeling ===")
    b.skift_afdeling("Drift")
    print("afdeling er nu:", b.afdeling)

    # Test med en liste og __str__
    print("\n=== Bonus: Liste med __str__ ===")
    brugere = [
        Bruger("Bjarne Nielsen", "bjarne@firma.dk", "HR"),
        Bruger("Cecilie Hansen", "cecilie@firma.dk", "IT", aktiv=False),
        Bruger("Diana Larsen",   "diana@firma.dk",   "Økonomi"),
    ]
    for bruger in brugere:
        print(bruger)   # kalder __str__ automatisk


# ─────────────────────────────────────────────────────────
if __name__ == "__main__":
    main()
