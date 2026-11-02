# ============================================================
#  LEKTION 7  ·  Sprint 4  ·  Øvelse 4 · LØSNINGSFORSLAG
#  Grupper - member og memberOf til bunds
# ============================================================
#
#  To spørgsmål går igen hele tiden i det virkelige AD-liv:
#
#    A) Hvem er MED i en gruppe?    → member-attributten
#    B) Hvilke grupper er nogen i?  → memberOf-attributten
#
#  Denne øvelse udforsker begge retninger grundigt.
#  Del 1-7 er færdige - kør og observér.
#  Del 8: skriv to linjer.
#  Husk: config_ad.json skal være udfyldt inden du kører.
#  Kræver:  pip install ldap3 pycryptodome
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
GRUPPER_OU = f"OU=Grupper,OU=Testdata,{AD_BASE_DN}"
BRUGERE_OU = f"OU=Brugere,OU=Testdata,{AD_BASE_DN}"

try:
    server = Server(AD_SERVER, get_info=ALL)
    conn = Connection(server, user=AD_BRUGER, password=AD_KODE,
                      authentication=NTLM, auto_bind=True,
                      auto_referrals=False)
except Exception as e:
    print(f"Forbindelsesfejl: {e}")
    exit()


def kort_navn(dn):
    """CN=GRP_IT_Admins,OU=... → GRP_IT_Admins"""
    return dn.split(",")[0].replace("CN=", "")


# ============================================================
#  Del 1 - Alle grupper: hvad findes der?
# ============================================================

print("=" * 65)
print("  Del 1 · Alle grupper i Testdata")
print("=" * 65)
print()

conn.search(
    search_base   = GRUPPER_OU,
    search_filter = "(objectClass=group)",
    search_scope  = SUBTREE,
    attributes    = ["cn", "groupType", "member"],
)

print(f"  Fandt {len(conn.entries)} grupper:\n")
print(f"  {'Gruppenavn':<30} {'Type':<20} {'Medlemmer'}")
print(f"  {'─'*30} {'─'*20} {'─'*10}")

for grp in conn.entries:
    navn  = str(grp.cn)
    gt    = str(grp.groupType)
    antal = len(grp.member.values) if grp.member.values else 0
    # Bit 0x80000000 = sikkerhedsgruppe. Er den sat, er tallet negativt.
    if int(gt) < 0:
        type_label = "Sikkerhedsgruppe"
    else:
        type_label = "Distribution"
    print(f"  {navn:<30} {type_label:<20} {antal}")


# ============================================================
#  Del 2 - member: hvem er med i GRP_IT_Admins?
# ============================================================

print()
print("=" * 65)
print("  Del 2 · member - hvem er med i GRP_IT_Admins?")
print("=" * 65)
print()
print("  'member' læses fra GRUPPEN og indeholder DN'erne")
print("  på alle der er med. Hvert DN er en fuld adresse.")
print()

conn.search(
    search_base   = GRUPPER_OU,
    search_filter = "(cn=GRP_IT_Admins)",
    search_scope  = SUBTREE,
    attributes    = ["member"],
)

if conn.entries:
    medlemmer = list(conn.entries[0].member.values) if conn.entries[0].member.values else []
    print(f"  GRP_IT_Admins har {len(medlemmer)} medlem(mer):\n")
    for dn in sorted(medlemmer):
        print(f"  · {kort_navn(dn)}")
        print(f"    {dn}")
        print()
else:
    print("  GRP_IT_Admins ikke fundet.")


# ============================================================
#  Del 3 - member med brugerinfo: GRP_Projekt_Alpha
# ============================================================

print("=" * 65)
print("  Del 3 · GRP_Projekt_Alpha - på tværs af afdelinger?")
print("=" * 65)
print()
print("  Her henter vi member-listen fra gruppen og slår")
print("  derefter HVER bruger op for at se deres afdeling.")
print()

conn.search(
    search_base   = GRUPPER_OU,
    search_filter = "(cn=GRP_Projekt_Alpha)",
    search_scope  = SUBTREE,
    attributes    = ["member"],
)

if conn.entries:
    projekt_dns = list(conn.entries[0].member.values) if conn.entries[0].member.values else []
    print(f"  {len(projekt_dns)} medlem(mer) i GRP_Projekt_Alpha:\n")
    print(f"  {'Logonnavn':<28} {'Afdeling'}")
    print(f"  {'─'*28} {'─'*20}")

    afdelinger = set()
    for dn in sorted(projekt_dns):
        conn.search(
            search_base   = AD_BASE_DN,
            search_filter = f"(distinguishedName={dn})",
            search_scope  = SUBTREE,
            attributes    = ["sAMAccountName", "department"],
        )
        if conn.entries:
            u   = conn.entries[0]
            afd = str(u.department) if str(u.department) != "[]" else "(ingen)"
            afdelinger.add(afd)
            print(f"  · {str(u.sAMAccountName):<28} {afd}")

    print()
    print(f"  Afdelinger repræsenteret: {', '.join(sorted(afdelinger))}")
else:
    print("  GRP_Projekt_Alpha ikke fundet.")


# ============================================================
#  Del 4 - GRP_Alle_Medarbejdere
# ============================================================

print()
print("=" * 65)
print("  Del 4 · GRP_Alle_Medarbejdere")
print("=" * 65)
print()

conn.search(
    search_base   = GRUPPER_OU,
    search_filter = "(cn=GRP_Alle_Medarbejdere)",
    search_scope  = SUBTREE,
    attributes    = ["member"],
)

if conn.entries:
    alle = list(conn.entries[0].member.values) if conn.entries[0].member.values else []
    print(f"  Gruppen har {len(alle)} direkte medlem(mer):\n")
    for dn in sorted(alle):
        print(f"  · {kort_navn(dn)}")
else:
    print("  GRP_Alle_Medarbejdere ikke fundet.")


# ============================================================
#  Del 5 - Sammenlign GRP_IT og DL_IT
# ============================================================

print()
print("=" * 65)
print("  Del 5 · Sikkerhedsgruppe vs. distributionsgruppe")
print("=" * 65)
print()
print("  GRP_IT = sikkerhedsgruppe (bruges til adgangsstyring)")
print("  DL_IT  = distributionsliste (bruges til e-mail)")
print()

for gruppenavn in ["GRP_IT", "DL_IT"]:
    conn.search(
        search_base   = GRUPPER_OU,
        search_filter = f"(cn={gruppenavn})",
        search_scope  = SUBTREE,
        attributes    = ["member", "groupType"],
    )
    if conn.entries:
        grp        = conn.entries[0]
        gt         = str(grp.groupType)
        type_label = "Sikkerhedsgruppe" if int(gt) < 0 else "Distribution"
        medl       = list(grp.member.values) if grp.member.values else []
        print(f"  {gruppenavn:<20} [{type_label}]  →  {len(medl)} medlem(mer)")
        for dn in sorted(medl):
            print(f"    · {kort_navn(dn)}")
        print()
    else:
        print(f"  {gruppenavn} ikke fundet\n")


# ============================================================
#  Del 6 - memberOf: hvilke grupper er thomas.bjerregaard i?
# ============================================================

print("=" * 65)
print("  Del 6 · memberOf - thomas.bjerregaards grupper")
print("=" * 65)
print()
print("  'memberOf' læses fra BRUGEREN og indeholder DN'erne")
print("  på alle de grupper brugeren er med i.")
print()

conn.search(
    search_base   = AD_BASE_DN,
    search_filter = "(sAMAccountName=thomas.bjerregaard)",
    search_scope  = SUBTREE,
    attributes    = ["memberOf", "cn", "department"],
)

if conn.entries:
    thomas  = conn.entries[0]
    grupper = list(thomas.memberOf.values) if thomas.memberOf.values else []
    print(f"  {str(thomas.cn)} ({str(thomas.department)})")
    print(f"  er med i {len(grupper)} gruppe(r):\n")
    for grp_dn in sorted(grupper):
        print(f"  · {kort_navn(grp_dn)}")
        print(f"    {grp_dn}")
else:
    print("  thomas.bjerregaard ikke fundet.")


# ============================================================
#  Del 7 - Sammenlign thomas og majas gruppemedlemskaber
# ============================================================

print()
print("=" * 65)
print("  Del 7 · Sammenlign thomas og majas gruppemedlemskaber")
print("=" * 65)
print()


def hent_grupper(logonnavn):
    """Returnerer et set af gruppe-CNer for en given bruger."""
    conn.search(
        search_base   = AD_BASE_DN,
        search_filter = f"(sAMAccountName={logonnavn})",
        search_scope  = SUBTREE,
        attributes    = ["memberOf"],
    )
    if conn.entries and conn.entries[0].memberOf.values:
        return set(kort_navn(dn) for dn in conn.entries[0].memberOf.values)
    return set()


thomas_grupper = hent_grupper("thomas.bjerregaard")
maja_grupper   = hent_grupper("maja.aggerholm")

kun_thomas = thomas_grupper - maja_grupper
kun_maja   = maja_grupper   - thomas_grupper
begge      = thomas_grupper & maja_grupper

print(f"  Thomas er med i {len(thomas_grupper)} gruppe(r)")
print(f"  Maja   er med i {len(maja_grupper)} gruppe(r)")
print()

if begge:
    print(f"  Grupper BEGGE er med i ({len(begge)}):")
    for g in sorted(begge):
        print(f"    · {g}")

if kun_thomas:
    print(f"\n  Grupper KUN Thomas er med i ({len(kun_thomas)}):")
    for g in sorted(kun_thomas):
        print(f"    · {g}")

if kun_maja:
    print(f"\n  Grupper KUN Maja er med i ({len(kun_maja)}):")
    for g in sorted(kun_maja):
        print(f"    · {g}")
else:
    print("\n  Maja er ikke i nogen grupper som Thomas ikke også er i.")


# ============================================================
#  Del 8 - Din tur: find nanna.vestergaards grupper
# ============================================================
#
#  Opgaven: udfyld de to linjer markeret med ← erstat
#  Sammenlign derefter Nannas grupper med Thomas og Majas.
#

print()
print("=" * 65)
print("  Del 8 · Din tur - find nanna.vestergaards grupper")
print("=" * 65)
print()

# Linje 1: Filteret der finder nanna.vestergaard
# Attributten for logonnavn hedder sAMAccountName
bruger_filter = "(sAMAccountName=nanna.vestergaard)"

# Linje 2: Den attribut der fortæller hvilke grupper brugeren er med i
bruger_attr = "memberOf"


# ── Resten kører automatisk når du har udfyldt de to linjer ──
if bruger_filter and bruger_attr:
    conn.search(
        search_base   = AD_BASE_DN,
        search_filter = bruger_filter,
        search_scope  = SUBTREE,
        attributes    = [bruger_attr],
    )

    if conn.entries:
        nanna_dns     = list(conn.entries[0].memberOf.values) if conn.entries[0].memberOf.values else []
        nanna_grupper = set(kort_navn(dn) for dn in nanna_dns)

        print(f"  nanna.vestergaard er med i {len(nanna_grupper)} gruppe(r):\n")
        for grp in sorted(nanna_grupper):
            print(f"  · {grp}")

        alle_tre  = nanna_grupper & thomas_grupper & maja_grupper
        kun_nanna = nanna_grupper - thomas_grupper - maja_grupper

        print()
        print("  Sammenligning med Thomas og Maja:")
        if alle_tre:
            print(f"  Alle tre er med i: {', '.join(sorted(alle_tre))}")
        if kun_nanna:
            print(f"  Kun Nanna er med i: {', '.join(sorted(kun_nanna))}")
        else:
            print("  Nanna har ingen grupper, som hverken Thomas eller Maja har.")
    else:
        print("  nanna.vestergaard ikke fundet.")
else:
    print("  Del 8: bruger_filter og/eller bruger_attr er ikke udfyldt.")


conn.unbind()


# ============================================================
#  Observationsopgaver
# ============================================================

print()
print("=" * 65)
print("  Observationsopgaver - sammenlign med ADUC")
print("=" * 65)
print()
print("Del 1 - Alle grupper:")
print("  A. Åbn ADUC → OU=Testdata → OU=Grupper.")
print("     Ser du det samme antal grupper?")
print("     Kan du se forskel på sikkerhedsgrupper og")
print("     distributionsgrupper på ikonerne i ADUC?")
print("  B. Hvad er groupType-talværdien for GRP_IT_Admins?")
print("     Hvad er den for DL_IT?")
print()
print("Del 2 - member (GRP_IT_Admins):")
print("  A. Åbn GRP_IT_Admins i ADUC → Members-fanen.")
print("     Stemmer listen præcis med Python-output?")
print("  B. Klik på én af administratorerne → Member Of-fanen.")
print("     Ser du GRP_IT_Admins der?")
print("     member og memberOf er to sider af samme medalje -")
print("     hvad viser det ene, som det andet ikke viser?")
print()
print("Del 3 - GRP_Projekt_Alpha:")
print("  A. Er gruppen sammensat på tværs af afdelinger?")
print("     Fra hvilke afdelinger kommer medlemmerne?")
print("  B. Klik én af projektmedlemmerne → Member Of.")
print("     Kan du finde GRP_Projekt_Alpha på listen?")
print()
print("Del 4 - GRP_Alle_Medarbejdere:")
print("  A. Tæl brugerne manuelt i ADUC.")
print("     Er det det samme antal som Python fandt?")
print("  B. Er deaktiverede konti med i gruppen?")
print()
print("Del 5 - GRP_IT vs DL_IT:")
print("  A. Har de de samme medlemmer?")
print("  B. Hvad kan GRP_IT bruges til, som DL_IT ikke kan?")
print()
print("Del 6+7 - memberOf og sammenligning:")
print("  A. Åbn thomas.bjerregaard i ADUC → Member Of.")
print("     Stemmer listen med Python-output?")
print("  B. Åbn maja.aggerholm → Member Of.")
print("     Hvad er forskellene på Thomas og Majas grupper?")
print("     Hvad fortæller det om deres roller?")
print()
print("Del 8 - Nanna:")
print("  A. Stemmer Python-output med ADUC → Member Of?")
print("  B. Er der grupper Nanna er i, som hverken Thomas")
print("     eller Maja er i? Hvad kan det betyde?")
print("  C. Prøv selv: ændr bruger_filter til en anden bruger")
print("     - fx rikke.svenningsen - og kør igen.")
print("     Hvem er med i flest grupper?")
print("=" * 65)
