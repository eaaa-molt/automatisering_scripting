# ============================================================
#  LEKTION 7  ·  Sprint 3  ·  Øvelse 3 · LØSNINGSFORSLAG
#  LDAP-filtre - find de rigtige brugere
# ============================================================
#
#  Kræver: config_ad.json i samme mappe (kopiér template-filen)
#  Forbindelsen klares af ad_hjaelp.py - den skal du ikke røre.
#
#  DIN OPGAVE:
#    Skriv ét LDAP-filter pr. opgave - erstat None med en streng.
#    Opgave 1-6 er obligatoriske, Opgave 7 er BONUS.
#
#  LDAP-filter hurtigreference:
#  ┌────────────────────────────────────────────────────────┐
#  │  Simpelt:    "(department=Salg)"                       │
#  │  AND:        "(&(department=IT)(title=IT-chef))"       │
#  │  OR:         "(|(department=Salg)(department=HR))"     │
#  │  Joker:      "(cn=T*)"  "(cn=*gaard)"  "(cn=*Thomas*)" │
#  │  Er sat:     "(title=*)"                               │
#  │  Ikke sat:   "(!(department=*))"                       │
#  └────────────────────────────────────────────────────────┘
#
# ============================================================

from ldap3 import SUBTREE
from ad_hjaelp import forbind, vis_brugere

conn, AD_BASE_DN = forbind()
BRUGERE_OU = f"OU=Brugere,OU=Testdata,{AD_BASE_DN}"


# ── Hjælpefunktion - rør ikke ved den ────────────────────
def soeg(filtr, overskrift):
    """Kør filteret mod OU=Brugere og vis resultatet."""
    if not filtr:
        print(f"\n{overskrift}: filteret er ikke udfyldt endnu.")
        return
    conn.search(BRUGERE_OU, filtr, SUBTREE,
                attributes=["sAMAccountName", "department", "title"])
    vis_brugere(conn.entries, overskrift)


# ── Opgave 1 · simpelt filter: én afdeling ───────────────
#  Find alle brugere i afdelingen "Salg".
#  Attributten hedder: department
#  Eksempel:  "(department=IT)"  finder alle med department = IT

filtr1 = "(department=Salg)"

soeg(filtr1, "Opgave 1 · Brugere i Salg")


# ── Opgave 2 · AND-filter: to betingelser ────────────────
#  Find alle brugere der BÅDE er i "IT"
#  OG har titlen "Systemadministrator".
#  AND-filter:  "(&(betingelse1)(betingelse2))"
#  Titel-attributten hedder: title

filtr2 = "(&(department=IT)(title=Systemadministrator))"

soeg(filtr2, "Opgave 2 · IT-systemadministratorer")


# ── Opgave 3 · OR-filter: to afdelinger på én gang ───────
#  Find alle brugere i ENTEN "Salg" ELLER "Support".
#  OR-filter:  "(|(betingelse1)(betingelse2))"

filtr3 = "(|(department=Salg)(department=Support))"

soeg(filtr3, "Opgave 3 · Salg eller Support")


# ── Opgave 4 · jokertegn: delvis match på navn ───────────
#  Find alle brugere hvis fulde navn (cn) begynder med "T".
#  Jokertegn:  "(cn=T*)"  ← alt der starter med T

filtr4 = "(cn=T*)"

soeg(filtr4, "Opgave 4 · Navne der starter med T")


# ── Opgave 5 · jokertegn: indeholder et bestemt ord i titel ───
#  Find alle brugere hvis titel indeholder ordet "chef".
#  Brug joker i begge ender:  "(title=*chef*)"

filtr5 = "(title=*chef*)"

soeg(filtr5, "Opgave 5 · Titler der indeholder 'chef'")


# ── Opgave 6 · AND med joker: attributten skal være sat ───
#  Find alle brugere der er i "HR"
#  OG har en titel (title-feltet er sat - brug joker *).
#  "title er sat" skrives som:  (title=*)

filtr6 = "(&(department=HR)(title=*))"

soeg(filtr6, "Opgave 6 · HR-brugere med en titel")


# ── Opgave 7 · BONUS: find brugere uden en afdeling ──────
#  Brugere hvor department-attributten IKKE er sat.
#  "attribut er ikke sat" skrives som:  (!(department=*))
#  (! = NOT, dvs. NOT department exists)
#  Kombinér det med (objectClass=user) i et AND-filter.
#  Ellers kommer OU=Brugere selv med: den har heller ingen afdeling.

filtr7 = "(&(objectClass=user)(!(department=*)))"

soeg(filtr7, "BONUS · Brugere uden afdeling")


conn.unbind()


# ============================================================
#  Observationsopgaver
# ============================================================

print()
print("=" * 60)
print("  Observationsopgaver - sammenlign med ADUC")
print("=" * 60)
print()
print("Opgave 1 - Salg:")
print("  A. Åbn ADUC → OU=Testdata → OU=Brugere.")
print("     Tæl Salg-brugere manuelt. Stemmer antallet?")
print("  B. Prøv at ændre 'Salg' til 'salg' (lille s).")
print("     Giver LDAP-filtre forskel på store og små bogstaver?")
print()
print("Opgave 2 - IT-systemadministratorer:")
print("  A. Åbn én af dem i ADUC → General-faneblad.")
print("     Ser du feltet Title = 'Systemadministrator'?")
print("  B. Hvad sker der hvis du bytter department og title om?")
print("     Er resultatet det samme?")
print()
print("Opgave 3 - Salg eller Support:")
print("  A. Er antallet præcis Salg-antal + Support-antal?")
print("     Sammenlign med Opgave 1-resultatet.")
print()
print("Opgave 4 - T-navne:")
print("  A. Find selv alle T-navne i ADUC.")
print("     Er de alle med? Mangler nogen?")
print("  B. Prøv (cn=*gaard) - hvem returneres?")
print("     Og (cn=*sen) - hvem returneres?")
print()
print("Opgave 5 - Chef-titler:")
print("  A. Hvilke titler indeholder 'chef'?")
print("     Er der forskel på 'IT-chef' og 'IT-Chef'?")
print()
print("Opgave 6 - HR med titel:")
print("  A. Er alle HR-brugere med? Mangler nogen?")
print("  B. mikkel.elmquist har titlen HR-konsulent. Er han med?")
print("     Åbn ham i ADUC - hvad står der i Department-feltet?")
print()
print("BONUS - Uden afdeling:")
print("  A. Er der brugere uden afdeling?")
print("     Find dem i ADUC - er Department-feltet tomt der?")
print("  B. Hvad ville scriptet fra lektion 5, øvelse 4 have gjort med dem?")
print("  C. Prøv kun (!(department=*)). Hvorfor kommer der en tom linje med?")
print("     Hint: SUBTREE søger også i selve search_base (OU=Brugere).")
print("=" * 60)
