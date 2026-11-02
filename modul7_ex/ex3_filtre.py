# ============================================================
#  LEKTION 7  ·  Sprint 3  ·  Øvelse 3
#  LDAP-filtre - find de rigtige brugere
# ============================================================
#
#  Scriptet er næsten færdigt.
#  Din opgave: skriv ét LDAP-filter per opgave (én linje).
#  Alle andre linjer er klar til at køre.
#
#  Husk: config_ad.json skal være udfyldt inden du kører.
#  Kræver:  pip install ldap3 pycryptodome
#
#  LDAP-filter hurtigreference:
#  ┌────────────────────────────────────────────────────────┐
#  │  Simpelt:    "(department=Salg)"                       │
#  │  AND:        "(&(department=IT)(title=IT-chef))"       │
#  │  OR:         "(|(department=Salg)(department=HR))"     │
#  │  Joker:      "(cn=T*)"  "(cn=*gaard)"  "(cn=*Thomas*)" │
#  │  Eksakt tom: "(!(department=*))"  (mangler attribut)   │
#  └────────────────────────────────────────────────────────┘
#
# ============================================================

import json
from pathlib import Path
from ldap3 import Server, Connection, ALL, NTLM, SUBTREE

MAPPE = Path(__file__).parent

try:
    with open(MAPPE / "config_ad.json", encoding="utf-8") as f:
        cfg = json.load(f)
except FileNotFoundError:
    print("Fejl: config_ad.json ikke fundet.")
    print("Kopiér config_ad_template.json → config_ad.json og udfyld.")
    exit()

AD_SERVER  = cfg["server"]
AD_BRUGER  = cfg["bruger"]
AD_KODE    = cfg["adgangskode"]
AD_BASE_DN = cfg["base_dn"]
BRUGERE_OU = f"OU=Brugere,OU=Testdata,{AD_BASE_DN}"

try:
    server = Server(AD_SERVER, get_info=ALL)
    conn = Connection(server, user=AD_BRUGER, password=AD_KODE,
                      authentication=NTLM, auto_bind=True,
                      auto_referrals=False)
except Exception as e:
    print(f"Forbindelsesfejl: {e}")
    exit()


# ── Hjælpefunktion - rør ikke ved den ───────────────────
def soeg(filtr, label):
    """Kør LDAP-søgning og udskriv resultatet pænt."""
    conn.search(
        search_base   = BRUGERE_OU,
        search_filter = filtr,
        search_scope  = SUBTREE,
        attributes    = ["sAMAccountName", "cn", "department", "title"],
    )
    print(f"\n{'─' * 60}")
    print(f"  {label}  →  {len(conn.entries)} bruger(e)")
    print(f"{'─' * 60}")
    print(f"  {'Logonnavn':<28} {'Afdeling':<14} Titel")
    print(f"  {'·' * 28} {'·' * 14} {'·' * 20}")
    for e in conn.entries:
        logon = str(e.sAMAccountName)
        afd   = str(e.department)
        titel = str(e.title)
        if afd   == "[]": afd   = ""
        if titel == "[]": titel = ""
        print(f"  {logon:<28} {afd:<14} {titel}")


# ============================================================
#  Opgave 1 - simpelt filter: én afdeling
# ============================================================
#  Find alle brugere i afdelingen "Salg".
#  Attributten hedder: department
#  Eksempel:  "(department=IT)"  finder alle med department = IT

filtr1 = None #TODO

if filtr1:
    soeg(filtr1, "Opgave 1 · Brugere i Salg")
else:
    print("\nOpgave 1: filtr1 er ikke udfyldt.")


# ============================================================
#  Opgave 2 - AND-filter: to betingelser
# ============================================================
#  Find alle brugere der BÅDE er i "IT"
#  OG har titlen "Systemadministrator".
#  AND-filter:  "(&(betingelse1)(betingelse2))"
#  Titel-attributten hedder: title

filtr2 = None  #TODO

if filtr2:
    soeg(filtr2, "Opgave 2 · IT-systemadministratorer")
else:
    print("\nOpgave 2: filtr2 er ikke udfyldt.")


# ============================================================
#  Opgave 3 - OR-filter: to afdelinger på én gang
# ============================================================
#  Find alle brugere i ENTEN "Salg" ELLER "Support".
#  OR-filter:  "(|(betingelse1)(betingelse2))"

filtr3 = None  #TODO

if filtr3:
    soeg(filtr3, "Opgave 3 · Salg eller Support")
else:
    print("\nOpgave 3: filtr3 er ikke udfyldt.")


# ============================================================
#  Opgave 4 - jokertegn: delvis match på navn
# ============================================================
#  Find alle brugere hvis fulde navn (cn) begynder med "T".
#  Jokertegn:  "(cn=T*)"  ← alt der starter med T

filtr4 = None  #TODO

if filtr4:
    soeg(filtr4, "Opgave 4 · Navne der starter med T")
else:
    print("\nOpgave 4: filtr4 er ikke udfyldt.")


# ============================================================
#  Opgave 5 - jokertegn: indeholder et bestemt ord i titel
# ============================================================
#  Find alle brugere hvis titel indeholder ordet "chef".
#  Brug joker i begge ender:  "(title=*chef*)"

filtr5 = None  #TODO

if filtr5:
    soeg(filtr5, "Opgave 5 · Titler der indeholder 'chef'")
else:
    print("\nOpgave 5: filtr5 er ikke udfyldt.")


# ============================================================
#  Opgave 6 - AND med joker: attributten skal være sat
# ============================================================
#  Find alle brugere der er i "HR"
#  OG har en titel (title-feltet er sat - brug joker *).
#  "title er sat" skrives som:  (title=*)

filtr6 = None  #TODO

if filtr6:
    soeg(filtr6, "Opgave 6 · HR-brugere med en titel")
else:
    print("\nOpgave 6: filtr6 er ikke udfyldt.")


# ============================================================
#  Opgave 7 - BONUS: find brugere uden en afdeling
# ============================================================
#  Brugere hvor department-attributten IKKE er sat.
#  "attribut er ikke sat" skrives som:  (!(department=*))
#  (! = NOT, dvs. NOT department exists)

filtr7 = None  #TODO

if filtr7:
    soeg(filtr7, "BONUS · Brugere uden afdeling")
else:
    print("\nBONUS (opgave 7): filtr7 er ikke udfyldt.")


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
print("=" * 60)
