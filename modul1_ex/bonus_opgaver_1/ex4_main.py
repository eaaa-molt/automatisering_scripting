# Modul 1 – Sprint 4: Kodestruktur og __main__
# -------------------------------------------------------
# Øvelse: Program med en liste af brugere og tre funktioner.
#         Alt kører via __main__-blokken.

# Denne linje kører altid – uanset om filen køres direkte eller importeres.
# Når Python kører filen direkte sætter den __name__ til strengen '__main__'.
# Det er præcis det vi tjekker i if-blokken nedenfor.
print(f"Fil indlæst – __name__ er: '{__name__}'")


def print_alle(brugere):
    """Printer alle brugere i listen."""
    print("Alle brugere:")
    for b in brugere:
        print("  -", b)


def find_bruger(brugere, navn):
    """Finder og returnerer en bruger (case-insensitiv).
    Returnerer None hvis ikke fundet."""
    for b in brugere:
        if b.lower() == navn.lower():
            return b
    return None


def antal_brugere(brugere):
    """Returnerer antallet af brugere i listen."""
    return len(brugere)


if __name__ == "__main__":
    brugere = ["Alice", "Bob", "Charlie", "Diana", "Erik"]

    print_alle(brugere)

    soeg = "diana"
    resultat = find_bruger(brugere, soeg)
    if resultat:
        print(f"\nFandt bruger: {resultat}")
    else:
        print(f"\nBruger '{soeg}' ikke fundet")

    print(f"\nAntal brugere: {antal_brugere(brugere)}")

# Opgave:
# 1. Tilføj en funktion 'tilfoej_bruger(brugere, navn)' der tilføjer
#    en bruger hvis de ikke allerede er på listen
# 2. Kør filen og læs linjen øverst i output:
#    "Fil indlæst – __name__ er: '__main__'"
#    Hvad tror du der ville stå hvis en anden fil importerede denne?
#    (Svar: så ville __name__ være filnavnet – fx 'ex4_main' – og
#     if-blokken ville IKKE køre. Det er hele pointen med __main__.)
# 3. Tilføj en funktion 'fjern_bruger(brugere, navn)' der fjerner
#    en bruger fra listen hvis de findes, og giver besked hvis ikke.
#    Kald den og verificer at listen er kortere bagefter.
