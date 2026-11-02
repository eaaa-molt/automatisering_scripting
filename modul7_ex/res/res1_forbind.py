# ============================================================
#  LEKTION 7  ·  Sprint 1  ·  Øvelse 1 · LØSNINGSFORSLAG
#  Den første forbindelse til AD
# ============================================================
#
#  OPSÆTNING (gøres én gang i VS Codes terminal):
#
#    python -m pip install ldap3 pycryptodome
#
#  Du skal være på lab-netværket (eller have VPN aktiv).
#  Brug din personlige AD-konto fra lektion 6.
#  Koden kører lokalt - du RDP'er kun ind for at bruge ADUC.
#
#  FEJL: "unsupported hash type MD4"?
#    NTLM bruger MD4, som nyere OpenSSL har slået fra.
#    pycryptodome giver ldap3 sin egen MD4. Installér den.
#
#  DIN OPGAVE:
#    Opgave 1  udfyld de fire konstanter og skriv forbindelsen
#    Opgave 2  kør og observér (intet at skrive)
#    Opgave 3  skriv tre søgninger efter eksemplet
#    Opgave 4  kør og observér (intet at skrive)
#    Svar på observationsopgaverne i bunden af output.
#
# ============================================================

from ldap3 import Server, Connection, ALL, NTLM, SUBTREE


# ── Opgave 1 · Udfyld de fire konstanter ─────────────────

AD_SERVER  = "10.160.0.220"          # ← DC'ens IP-adresse (Øvelse 0, Del 0)
AD_BRUGER  = "CSIK_DC_1\\dit.logonnavn"   # ← DOMÆNE\\logonnavn
AD_KODE    = "DinAdgangskode"        # ← din AD-adgangskode
AD_BASE_DN = "DC=CSIK_DC_1,DC=local" # ← defaultNamingContext (Øvelse 0, Del 5)


# ── Opgave 1 · Opret forbindelsen ────────────────────────

print("=" * 60)
print("  Opgave 1 · Forbind til AD")
print("=" * 60)

try:
    server = Server(AD_SERVER, get_info=ALL)

    conn = Connection(
        server,
        user           = AD_BRUGER,
        password       = AD_KODE,
        authentication = NTLM,
        auto_bind      = True,
        auto_referrals = False,
    )

except Exception as e:
    print(f"FEJL: {e}")
    print("Mulige årsager:")
    print("  · Forkert AD_BRUGER  (husk: DOMÆNE\\\\logonnavn)")
    print("  · Forkert AD_KODE    (prøv samme kode i RDP)")
    print("  · Ikke på lab-netværket / VPN")
    raise SystemExit

# ── Rør ikke herunder ─────────────────────────────────────
if conn is None:
    print("Opgave 1: server og conn er ikke udfyldt endnu.")
    raise SystemExit

print(f"Forbundet      : {conn.bound}")        # True = godkendt
print(f"Server-host    : {conn.server.host}")
print(f"LDAP-port      : {conn.server.port}")  # standard = 389
print(">>> Python taler nu med AD. <<<")


# ── Opgave 2 · Server-information (kør og observér) ──────

print()
print("=" * 60)
print("  Opgave 2 · Server-information fra AD")
print("=" * 60)

info = server.info


def hent(noegle, standard="?"):
    """Hent én værdi fra info.other (kan være str eller list)."""
    v = info.other.get(noegle, standard)
    return v[0] if isinstance(v, list) else v


print("Naming contexts (rodnoder i AD-træet):")
for nc in info.naming_contexts:
    print(f"  {nc}")

print(f"\nDC'ens fulde DNS-navn    : {hent('dnsHostName')}")
print(f"Domain functional level  : {hent('domainFunctionality')}")
print("  (0=Win2000  2=2003  3=2008  4=2008R2  5=2012  6=2012R2  7=2016+)")
print(f"Forest functional level  : {hent('forestFunctionality')}")


# ── Opgave 3 · Tæl objekter i AD ─────────────────────────

print()
print("=" * 60)
print("  Opgave 3 · Hvor mange objekter er der i AD?")
print("=" * 60)

# Eksempel - tæl brugere. attributes=[] betyder: hent kun DN
conn.search(AD_BASE_DN, "(objectClass=user)", SUBTREE, attributes=[])
bruger_antal = len(conn.entries)
print(f"Bruger-objekter (user)    : {bruger_antal}")

conn.search(AD_BASE_DN, "(objectClass=group)", SUBTREE, attributes=[])
gruppe_antal = len(conn.entries)

conn.search(AD_BASE_DN, "(objectClass=computer)", SUBTREE, attributes=[])
computer_antal = len(conn.entries)

conn.search(AD_BASE_DN, "(objectClass=organizationalUnit)", SUBTREE, attributes=[])
ou_antal = len(conn.entries)

print(f"Gruppe-objekter (group)   : {gruppe_antal}")
print(f"Computer-objekter         : {computer_antal}")
print(f"OU-objekter               : {ou_antal}")
if bruger_antal == 0:
    print("NOTE: 0 brugere betyder næsten altid, at AD_BASE_DN er forkert.")


# ── Opgave 4 · Forkert adgangskode (kør og observér) ─────

print()
print("=" * 60)
print("  Opgave 4 · Hvad sker der med en forkert kode?")
print("=" * 60)

try:
    Connection(Server(AD_SERVER), user=AD_BRUGER, password="DetErForkert99!",
               authentication=NTLM, auto_bind=True)
    print("Forbundet - det burde ikke ske!")
except Exception as e:
    print(f"Fejltype   : {type(e).__name__}")
    print(f"Fejlbesked : {e}")

conn.unbind()


# ============================================================
#  Observationsopgaver
# ============================================================

print()
print("=" * 60)
print("  Observationsopgaver - brug output + ADUC til at svare")
print("=" * 60)
print("Opgave 1:")
print("  A. Hvad er LDAP-porten? Er det den samme som HTTP (80)?")
print("  B. Hvad betyder conn.bound = True?")
print("Opgave 2:")
print("  A. Hvad er DC'ens fulde DNS-navn?")
print("  B. Hvilken Windows Server svarer domain functional level til?")
print("  C. Find rodnoden i ADUC-træet - matcher den en naming context?")
print("Opgave 3:")
print("  A. Computer-konti er også user-objekter i AD.")
print("     Hvor mange rigtige brugere er der så (bruger - computer)?")
print("  B. Kan du se OU'erne i ADUC? Passer ou_antal nogenlunde?")
print("Opgave 4:")
print("  A. Hvad hedder Python-fejltypen ved forkert kode?")
print("  B. BONUS: Michael kan vise Event ID 4625 på DC'en.")
print("     Hvad tror du, der bliver logget ved et mislykket login?")
print("=" * 60)
