# ============================================================
#  LEKTION 7  ·  Sprint 2  ·  Øvelse 2 · LØSNINGSFORSLAG
#  Læs og udforsk brugere fra AD
# ============================================================
#
#  Scriptet er færdigt - udfyld config_ad.json og kør det.
#  Din opgave er at OBSERVERE output og besvare spørgsmålene
#  i bunden ved at sammenligne med ADUC.
#
#  Kræver:  pip install ldap3 pycryptodome
#  Fejl "unsupported hash type MD4"? → pip install pycryptodome
#
# ============================================================

import json
from pathlib import Path
from ldap3 import Server, Connection, ALL, NTLM, SUBTREE

MAPPE = Path(__file__).parent

# ── Indlæs forbindelsesoplysninger fra config_ad.json ────
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

# ── Opret forbindelsen ───────────────────────────────────
try:
    server = Server(AD_SERVER, get_info=ALL)
    conn = Connection(server, user=AD_BRUGER, password=AD_KODE,
                      authentication=NTLM, auto_bind=True,
                      auto_referrals=False)
except Exception as e:
    print(f"Forbindelsesfejl: {e}")
    exit()


# ============================================================
#  Del 1 - List alle brugere
# ============================================================

print("=" * 65)
print("  Del 1 · Alle brugere i Testdata")
print("=" * 65)

conn.search(
    search_base   = BRUGERE_OU,
    search_filter = "(objectClass=user)",
    search_scope  = SUBTREE,
    attributes    = ["sAMAccountName", "cn", "department", "title"],
)

print(f"\nFandt {len(conn.entries)} brugere:\n")
print(f"  {'Logonnavn':<28} {'Afdeling':<14} Titel")
print(f"  {'─'*28} {'─'*14} {'─'*24}")

for entry in conn.entries:
    logon = str(entry.sAMAccountName)
    afd   = str(entry.department)
    titel = str(entry.title)
    if afd   == "[]": afd   = ""
    if titel == "[]": titel = ""
    print(f"  {logon:<28} {afd:<14} {titel}")


# ============================================================
#  Del 2 - Tæl brugere pr. afdeling
# ============================================================

print()
print("=" * 65)
print("  Del 2 · Antal brugere pr. afdeling")
print("=" * 65)
print()

# Gennemgå alle entries fra Del 1 og tæl
tæller = {}
for entry in conn.entries:
    afd = str(entry.department)
    if afd == "[]":
        afd = "(ingen afdeling)"
    tæller[afd] = tæller.get(afd, 0) + 1

for afd, antal in sorted(tæller.items()):
    print(f"  {afd:<20} {antal} bruger(e)")

print(f"\n  Total: {sum(tæller.values())}")


# ============================================================
#  Del 3 - Aktive vs. deaktiverede konti
# ============================================================

print()
print("=" * 65)
print("  Del 3 · Aktive og deaktiverede konti")
print("=" * 65)
print()
print("  userAccountControl-værdier:")
print("  512  = aktiv konto")
print("  514  = deaktiveret konto")
print("  66048 = aktiv, kode udløber aldrig")
print("  66050 = deaktiveret, kode udløber aldrig")
print()

conn.search(
    search_base   = BRUGERE_OU,
    search_filter = "(objectClass=user)",
    search_scope  = SUBTREE,
    attributes    = ["sAMAccountName", "cn", "department", "userAccountControl"],
)

print(f"  {'Logonnavn':<28} {'UAC-værdi':<12} Status")
print(f"  {'─'*28} {'─'*12} {'─'*16}")

aktive    = 0
deaktiverede = 0

for entry in conn.entries:
    logon = str(entry.sAMAccountName)
    uac   = str(entry.userAccountControl)
    if uac == "[]":
        uac = "?"

    # bit 1 (=2) i UAC angiver deaktiveret
    try:
        uac_tal = int(uac)
        if uac_tal & 2:
            status = "DEAKTIVERET"
            deaktiverede += 1
        else:
            status = "aktiv"
            aktive += 1
    except ValueError:
        status = "?"

    print(f"  {logon:<28} {uac:<12} {status}")

print()
print(f"  Aktive:       {aktive}")
print(f"  Deaktiverede: {deaktiverede}")


# ============================================================
#  Del 4 - Se alle attributter for én bruger
# ============================================================

print()
print("=" * 65)
print("  Del 4 · Alle attributter for thomas.bjerregaard")
print("=" * 65)
print()

conn.search(
    search_base   = AD_BASE_DN,
    search_filter = "(sAMAccountName=thomas.bjerregaard)",
    search_scope  = SUBTREE,
    attributes    = ["*"],
)

if conn.entries:
    bruger = conn.entries[0]
    print(f"  Fuldt DN: {bruger.entry_dn}")
    print()
    for attr_navn, attr_vaerdi in sorted(bruger.entry_attributes_as_dict.items()):
        if attr_vaerdi and str(attr_vaerdi) not in ["[]", "['']"]:
            print(f"  {attr_navn:<30} {attr_vaerdi}")
else:
    print("  Brugeren thomas.bjerregaard blev ikke fundet.")


# ============================================================
#  Del 5 - Brugere med specialtegn i navnet
# ============================================================

print()
print("=" * 65)
print("  Del 5 · Brugere med æ, ø eller å i fuldt navn")
print("=" * 65)
print()
print(f"  {'Fuldt navn (cn)':<30} Logonnavn (sAMAccountName)")
print(f"  {'─'*30} {'─'*28}")

conn.search(
    search_base   = BRUGERE_OU,
    search_filter = "(objectClass=user)",
    search_scope  = SUBTREE,
    attributes    = ["sAMAccountName", "cn"],
)

fundet = 0
for entry in conn.entries:
    navn  = str(entry.cn)
    logon = str(entry.sAMAccountName)
    if any(c in navn.lower() for c in "æøå"):
        print(f"  {navn:<30} {logon}")
        fundet += 1

if fundet == 0:
    print("  Ingen brugere med æ/ø/å fundet.")
else:
    print(f"\n  {fundet} bruger(e) med specialtegn i navnet.")


# ============================================================
#  Del 6 - Sammenlign to specifikke brugere: Maja og Rikke
# ============================================================

print()
print("=" * 65)
print("  Del 6 · Nærkig på Maja Aggerholm og Rikke Svenningsen")
print("=" * 65)
print()

for logonnavn in ["maja.aggerholm", "rikke.svenningsen"]:
    conn.search(
        search_base   = AD_BASE_DN,
        search_filter = f"(sAMAccountName={logonnavn})",
        search_scope  = SUBTREE,
        attributes    = ["cn", "department", "title",
                         "userAccountControl", "memberOf"],
    )
    if conn.entries:
        e = conn.entries[0]
        uac = str(e.userAccountControl)
        try:
            deaktiveret = bool(int(uac) & 2)
        except:
            deaktiveret = False

        print(f"  {str(e.cn)}")
        print(f"    Afdeling    : {e.department}")
        print(f"    Titel       : {e.title}")
        print(f"    UAC         : {uac}  ({'DEAKTIVERET' if deaktiveret else 'aktiv'})")
        grupper = list(e.memberOf.values) if e.memberOf.values else []
        print(f"    Grupper ({len(grupper)})  :", end="")
        if grupper:
            for i, g in enumerate(grupper):
                kort = g.split(",")[0].replace("CN=", "")
                print(f"{'':17}{kort}" if i > 0 else f" {kort}")
        else:
            print(" (ingen)")
        print()
    else:
        print(f"  {logonnavn} ikke fundet")
        print()


conn.unbind()


# ============================================================
#  Observationsopgaver
# ============================================================

print("=" * 65)
print("  Observationsopgaver - brug output + ADUC til at svare")
print("=" * 65)
print()
print("Del 1 - Alle brugere:")
print("  A. Hvor mange brugere er der i alt?")
print("     Åbn ADUC → OU=Testdata → OU=Brugere og tæl.")
print("     Stemmer det med Python-output?")
print("  B. Er alle afdelinger repræsenteret? Hvilke ser du?")
print("  C. Er der brugere uden titel? Hvem?")
print()
print("Del 2 - Afdeling-tælling:")
print("  A. Hvilken afdeling har flest brugere?")
print("  B. Er der brugere med '(ingen afdeling)'?")
print("     Find dem i ADUC - er afdelingsfeltet tomt der?")
print()
print("Del 3 - Aktive vs. deaktiverede:")
print("  A. Hvor mange er deaktiverede?")
print("  B. Find de deaktiverede brugere i ADUC.")
print("     Properties → Account-faneblad:")
print("     Er 'Account is disabled' markeret?")
print("  C. Ser du forskel i Del 1-tabellen på aktive og")
print("     deaktiverede - eller er de ens der?")
print("     Hvad mangler for at skelne dem i Del 1?")
print()
print("Del 4 - Alle attributter (thomas.bjerregaard):")
print("  A. Find attributten 'userAccountControl'.")
print("     Hvad er værdien? (512 = aktiv, 514 = deaktiveret)")
print("  B. Find 'memberOf' - hvilke grupper er Thomas med i?")
print("     Åbn Thomas i ADUC → Member Of-fanen og sammenlign.")
print("  C. Find 'whenCreated' - hvornår blev kontoen oprettet?")
print("  D. Hvilke attributter er sat med værdier?")
print("     Hvilke er tomme (findes ikke i listen)?")
print()
print("Del 5 - Specialtegn:")
print("  A. Har logonnavnene bevaret æ, ø og å?")
print("     Eller er de erstattet med noget andet?")
print("  B. Kig på Søndergaard og Møller - hvad er logonnavnet?")
print("     Hvad er reglen for konvertering?")
print()
print("Del 6 - Maja og Rikke:")
print("  A. Begge er deaktiverede - er de i de samme grupper?")
print("  B. Åbn begge i ADUC → Member Of-fanen.")
print("     Er der forskel på hvilke grupper de er med i?")
print("  C. Hvad sker der hvis en deaktiveret bruger prøver")
print("     at logge ind med RDP? Prøv det og se fejlbeskeden.")
print("=" * 65)
