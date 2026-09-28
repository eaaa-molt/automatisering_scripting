# Modul 1 – Sprint 2: Løkker og betingelser
# -------------------------------------------------------
# Øvelse: Print kun tal der er større end 10.
#         Beregn og print summen af alle tal i listen.

tal = [4, 15, 8, 23, 1, 17, 6, 11, 3, 19]

print("Tal større end 10:")
for t in tal:
    if t > 10:
        print(" -", t)

sum_alle = 0
for t in tal:
    sum_alle += t

print("\nSum af alle tal:", sum_alle)

# Opgave:
# 1. Ændr grænsen fra 10 til 15 – hvilke tal printes nu?
# 2. Tilføj en tæller der tæller hvor mange tal er over grænsen
# 3. Udskriv også det største tal i listen (uden at bruge max())
