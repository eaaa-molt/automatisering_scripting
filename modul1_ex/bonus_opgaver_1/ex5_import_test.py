# Modul 1 – Sprint 4 (bonus): Import-test
# -------------------------------------------------------
# Øvelse: Kør DENNE fil og læs output nøje.
#         Sammenlign med hvad du så da du kørte ex4_main.py direkte.
#
# Kør ex4_main.py først, og notér output.
# Kør derefter denne fil – hvad er anderledes?

from ex4_main import print_alle, find_bruger, antal_brugere

# Hvad sker der når ovenstående linje køres?
# Python indlæser ex4_main.py og kører alt koden i den –
# BORTSET FRA det der ligger inde i:  if __name__ == "__main__":
#
# Det betyder:
#   ✓  print(f"Fil indlæst – __name__ er: ...") kører  →  men printer 'ex4_main'
#   ✓  Alle tre funktioner defineres og er tilgængelige her
#   ✗  if __name__ == "__main__": blokken kører IKKE  →  ingen brugerliste, ingen søgning
#
# Prøv det:

print("\n--- Vi er nu i ex5_import_test.py ---")
print(f"Denne fils __name__ er: '{__name__}'")

# Funktionerne fra ex4_main er tilgængelige og virker fint
mine_brugere = ["Alice", "Bob", "Charlie"]
print()
print_alle(mine_brugere)
print(f"\nAntal: {antal_brugere(mine_brugere)}")

resultat = find_bruger(mine_brugere, "bob")
print(f"Søgte efter 'bob' – fandt: {resultat}")

# Opgave:
# 1. Sammenlign output herfra med output fra ex4_main.py kørt direkte:
#    - Hvad printer __name__ de to steder?
#    - Hvad kørte IKKE da vi importerede?
# 2. Hvad ville ske hvis ex4_main IKKE havde if __name__ == "__main__": ?
#    Fjern den fra ex4_main (kommenter den ud) og kør ex5 igen –
#    hvad sker der nu?
