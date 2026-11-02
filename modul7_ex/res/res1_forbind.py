# ============================================================
#  LEKTION 7  ·  Sprint 1  ·  Øvelse 1 · LØSNINGSFORSLAG
#  Den første forbindelse til AD
# ============================================================
#
#  OPSÆTNING (gøres én gang på din computer):
#
#    1. Åbn en terminal i VS Code
#    2. Kør følgende to kommandoer:
#
#         pip install ldap3
#         pip install pycryptodome
#
#       (pycryptodome er nødvendig på nyere systemer - se note nedenfor)
#
#    3. Bekræft:  python -c "import ldap3; print(ldap3.__version__)"
#    4. Udfyld dine fire oplysninger herunder
#    5. Kør scriptet:  python ex1_forbind.py
#
#  Du skal være på lab-netværket (eller have VPN aktiv).
#  Brug de personlige AD-konti I oprettede i lektion 6.
#  Koden kører lokalt - du RDP'er kun ind for at bruge ADUC.
#
#  FEJL: "unsupported hash type MD4"?
#    NTLM-autentifikation bruger MD4-hashing. Nyere versioner af
#    OpenSSL (3.x) deaktiverer MD4 som standard. pycryptodome
#    giver ldap3 en alternativ MD4-implementering og løser fejlen.
#    Løsning:  pip install pycryptodome
#
# ============================================================

from ldap3 import Server, Connection, ALL, NTLM, SUBTREE

# ── Udfyld disse fire linjer ─────────────────────────────
AD_SERVER  = "10.160.0.220"          # ← DC'ens IP-adresse
#              Brug IP - ikke hostname - da DNS-opslag ikke
#              er tilgængeligt på lab-netværket.
#              IP-adressen finder du i Øvelse 0 (Confluence) eller
#              ved at spørge Michael.
AD_BRUGER  = "CSIK_DC_1\\dit.navn"   # ← DOMÆNE\\logonnavn
AD_KODE    = "DinAdgangskode"         # ← din AD-adgangskode
AD_BASE_DN = "DC=CSIK_DC_1,DC=local" # ← se defaultNamingContext i Øvelse 0
# ─────────────────────────────────────────────────────────


# ============================================================
#  Del 1 - Opret forbindelsen og tjek at den virker
# ============================================================

print("=" * 60)
print("  Del 1 · Forbind til AD")
print("=" * 60)
print()
print(f"Forbinder til  : {AD_SERVER}")
print(f"Som bruger     : {AD_BRUGER}")
print()

try:
    server = Server(AD_SERVER, get_info=ALL)
    conn = Connection(
        server,
        user            = AD_BRUGER,
        password        = AD_KODE,
        authentication  = NTLM,
        auto_bind       = True,
        auto_referrals  = False,   # undgå LDAPSocketOpenError ved søgning
    )
    print(f"Forbundet      : {conn.bound}")        # True = godkendt
    print(f"Server-host    : {conn.server.host}")
    print(f"LDAP-port      : {conn.server.port}")  # standard = 389
    print()
    print(">>> Python taler nu med AD. <<<")

except Exception as e:
    print(f"FEJL: {e}")
    print()
    print("Mulige årsager:")
    print("  · Forkert AD_BRUGER  (husk: DOMÆNE\\\\logonnavn)")
    print("  · Forkert AD_KODE    (prøv samme kode i RDP)")
    print("  · Ikke på lab-netværket")
    exit()


# ============================================================
#  Del 2 - Udforsk serverens AD-information
# ============================================================

print()
print("=" * 60)
print("  Del 2 · Server-information fra AD")
print("=" * 60)
print()

info = server.info

# Naming contexts = rodnoderne i AD-træet
print("Naming contexts (rodnoder i AD-træet):")
for nc in info.naming_contexts:
    print(f"  {nc}")

print()
print("Understøttede LDAP-versioner:")
for ver in info.supported_ldap_versions:
    print(f"  {ver}")

def _hent(key, fallback="?"):
    """Hent en enkelt værdi fra info.other - håndter både str og list."""
    v = info.other.get(key, fallback)
    return v[0] if isinstance(v, list) else v

print(f"\nDC'ens fulde DNS-navn    : {_hent('dnsHostName', 'ikke tilgængelig')}")

func_level = _hent("domainFunctionality")
print(f"Domain functional level  : {func_level}")
print("  (0=Win2000  2=2003  3=2008  4=2008R2  5=2012  6=2012R2  7=2016+)")

print(f"Forest functional level  : {_hent('forestFunctionality')}")
print(f"Schema naming context    : {_hent('schemaNamingContext')}")


# ============================================================
#  Del 3 - Tæl objekter i AD
# ============================================================

print()
print("=" * 60)
print("  Del 3 · Hvor mange objekter er der i AD?")
print("=" * 60)
print()

# Find den korrekte domæne-base DN automatisk fra naming contexts.
# AD returnerer stille 0 resultater hvis search_base ikke matcher -
# derfor henter vi den rigtige DN direkte fra serverens rootDSE
# i stedet for at stole blindt på AD_BASE_DN-konstanten.
SOeGE_BASE = AD_BASE_DN
for nc in info.naming_contexts:
    # Domæne-NC starter med DC= og indeholder ikke CN=
    if nc.upper().startswith("DC=") and "CN=" not in nc.upper():
        SOeGE_BASE = nc
        break

print(f"Søger fra : {SOeGE_BASE}")
if SOeGE_BASE.lower() != AD_BASE_DN.lower():
    print(f"NOTE: Din AD_BASE_DN ({AD_BASE_DN}) matcher ikke")
    print(f"      serverens faktiske DN ({SOeGE_BASE}).")
    print(f"      Ret AD_BASE_DN øverst i filen - og i config_ad.json.")
print()

# Brugere
conn.search(SOeGE_BASE, "(objectClass=user)", SUBTREE, attributes=[])
bruger_antal = len(conn.entries)
print(f"Bruger-objekter (user)    : {bruger_antal}")

# Grupper
conn.search(SOeGE_BASE, "(objectClass=group)", SUBTREE, attributes=[])
gruppe_antal = len(conn.entries)
print(f"Gruppe-objekter (group)   : {gruppe_antal}")

# Computere
conn.search(SOeGE_BASE, "(objectClass=computer)", SUBTREE, attributes=[])
computer_antal = len(conn.entries)
print(f"Computer-objekter         : {computer_antal}")

# Organisationsenheder
conn.search(SOeGE_BASE, "(objectClass=organizationalUnit)", SUBTREE, attributes=[])
ou_antal = len(conn.entries)
print(f"OU-objekter               : {ou_antal}")

print(f"\nTotal objekter i søgningen: {bruger_antal + gruppe_antal + computer_antal + ou_antal}")


# ============================================================
#  Del 4 - Eksperiment: forkert adgangskode
# ============================================================

print()
print("=" * 60)
print("  Del 4 · Eksperiment - hvad sker med forkert kode?")
print("=" * 60)
print()

FORKERT_KODE = "DetErForkert99!"

try:
    server2 = Server(AD_SERVER, get_info=ALL)
    conn2 = Connection(
        server2,
        user           = AD_BRUGER,
        password       = FORKERT_KODE,
        authentication = NTLM,
        auto_bind      = True,
    )
    print("Forbundet - det burde ikke ske!")
except Exception as e:
    print(f"Fejltype   : {type(e).__name__}")
    print(f"Fejlbesked : {e}")
    print()
    print("(Forventet - AD afviste den forkerte adgangskode)")


conn.unbind()
print()


# ============================================================
#  Observationsopgaver
# ============================================================

print("=" * 60)
print("  Observationsopgaver - brug output + ADUC til at svare")
print("=" * 60)
print()
print("Del 1:")
print("  A. Hvad er LDAP-porten? Er det den samme som HTTP (80)?")
print("  B. Hvad betyder conn.bound = True?")
print("  C. Åbn ADUC via RDP - er det det samme AD du ser der?")
print()
print("Del 2:")
print("  A. Hvad er DC'ens fulde DNS-navn?")
print("  B. Hvad er domain functional level? Hvilket Windows Server")
print("     svarer det til? (se tabellen i output)")
print("  C. Hvad er en naming context?")
print("     Find rodnoden i ADUC-træet - matcher det?")
print()
print("Del 3:")
print("  A. Hvor mange bruger-objekter fandt Python?")
print("     Tæl i ADUC - er det det samme?")
print("     OBS: user-objekter inkluderer computer-konti i AD.")
print("          Prøv at trække computer_antal fra bruger_antal.")
print("  B. Kan du se OU-objekterne i ADUC?")
print("     Svarer ou_antal til antallet af mapper du ser?")
print()
print("Del 4:")
print("  A. Hvad hedder Python-fejltypen ved forkert kode?")
print("  B. Prøv selv: ret AD_KODE til noget forkert øverst")
print("     i filen og kør igen. Ser du den samme fejltype?")
print("  C. BONUS: I har ikke adgang til DC'en, men Michael kan vise")
print("     Event Viewer → Windows Logs → Security, Event ID 4625.")
print("     Hvad tror du, der bliver logget ved et mislykket login?")
print("=" * 60)
