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

    # ── Opgave 1 ──────────────────────────────────────────
    # Implementer vis_info(self)
    #
    # Printer alle fire attributter med en label foran.
    # Brug f-strings og print én attribut per linje.
    #
    # Forventet output:
    #   Navn:      Anna Jensen
    #   E-mail:    anna@firma.dk
    #   Afdeling:  IT
    #   Status:    Aktiv
    #
    # Hint: brug "Aktiv" hvis self.aktiv er True, ellers "Inaktiv"

    def vis_info(self):
        # TODO: print navn med label
        # TODO: print e-mail med label
        # TODO: print afdeling med label
        # TODO: beregn status-tekst og print den
        pass


    # ── Opgave 2 ──────────────────────────────────────────
    # Implementer deaktiver(self)
    #
    # Tjek først om brugeren allerede er inaktiv.
    # Hvis ja: print en besked om at brugeren allerede er inaktiv.
    # Hvis nej: sæt self.aktiv til False og print en bekræftelse.
    #
    # Forventet output (hvis aktiv):
    #   Anna Jensen er nu deaktiveret.
    # Forventet output (hvis allerede inaktiv):
    #   Anna Jensen er allerede inaktiv.

    def deaktiver(self):
        # TODO: tjek om brugeren allerede er inaktiv og print besked
        # TODO: ellers sæt aktiv til False og print bekræftelse
        pass


    # ── Opgave 3 ──────────────────────────────────────────
    # Implementer skift_email(self, ny_email)
    #
    # Gem den nuværende e-mail i en variabel (gammel_email),
    # opdater self.email til ny_email, og print ændringen.
    #
    # Forventet output:
    #   E-mail opdateret: anna@firma.dk → anna.jensen@nytfirma.dk

    def skift_email(self, ny_email):
        # TODO: gem den nuværende self.email i en variabel
        # TODO: opdater self.email til ny_email
        # TODO: print ændringen med gammel og ny e-mail
        pass


    # ── Opgave 4 ──────────────────────────────────────────
    # Implementer __str__(self)
    #
    # __str__ kaldes automatisk når man bruger print() på objektet
    # eller str(b). Den skal RETURNERE (ikke printe) en streng.
    #
    # Forventet output:
    #   Bruger(Anna Jensen, IT, aktiv)
    #   Bruger(Cecilie Hansen, IT, inaktiv)
    #
    # Hint: beregn status-teksten i en variabel, brug den i return

    def __str__(self):
        # TODO: beregn status-tekst (aktiv/inaktiv)
        # TODO: returner en streng med navn, afdeling og status
        return ""   # midlertidig tom streng — erstat med din løsning


    # ── Opgave 5 ──────────────────────────────────────────
    # Implementer skift_afdeling(self, ny_afdeling)
    #
    # Gem den nuværende afdeling i en variabel,
    # opdater self.afdeling til ny_afdeling, og print ændringen.
    #
    # Forventet output:
    #   Afdeling opdateret: IT → Drift

    def skift_afdeling(self, ny_afdeling):
        # TODO: gem den nuværende self.afdeling i en variabel
        # TODO: opdater self.afdeling til ny_afdeling
        # TODO: print ændringen
        pass


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
