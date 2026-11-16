# ============================================================
#  MODUL 9 · Sprint 3 · Øvelse 3 · Målrettede søgninger
# ============================================================
#  Tre typiske auditspørgsmål: Hvordan fordeler brugerne sig? Hvem er
#  administratorer? Hvem har ikke logget ind i 90 dage?
#  Scriptet LÆSER kun fra AD. Det skriver aldrig noget.
#
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
#
#  Trin 1-5 er kernen. Trin 6-10 er BONUS, hvis du har tid tilbage.
# ============================================================
from datetime import datetime, timedelta, timezone
from ldap3 import SUBTREE
from ad_hjaelp import forbind, overskrift

conn = forbind()
ou = "OU=Testdata,DC=CSIK_DC_1,DC=local"
domaene = "DC=CSIK_DC_1,DC=local"

# ------------------------------------------------------------
# Trin 1 · Tæl brugere pr. afdeling
# ------------------------------------------------------------
overskrift("Trin 1 · Brugere pr. afdeling")
conn.search(ou, "(objectClass=user)", SUBTREE, attributes=["department"])
taeller = {}
for e in conn.entries:
    afd = e.department.value
    if afd is None:
        afd = "(ingen)"
    # TODO: læg 1 til tallet for afd i taeller (Tip: dict.get fra slides)
print("   ", taeller)
# 1a. Hvad sker der første gang en afdeling dukker op i løkken? Hvad gør .get(afd, 0)?
# 1b. Hvad ville taeller[afd] += 1 gøre første gang? Prøv det.
# 1c. Summen af alle tallene. Passer den med antallet af brugere fra Sprint 1, Trin 1?

# ------------------------------------------------------------
# Trin 2 · Sortér, så den største afdeling står øverst
# ------------------------------------------------------------
overskrift("Trin 2 · Afdelinger, største først")
sorteret = "???"                          # TODO: taeller.items() sorteret efter antal, største først
if sorteret == "???":
    print("    Udfyld sorteret i Trin 2.")
    exit()
for afd, antal in sorteret:
    print(f"    {afd:<20} {antal:>3}")
# 2a. Hvad er x i lambda x: x[1]? Hvad er x[0]?
# 2b. Hvad sker der, hvis du fjerner reverse=True?
# 2c. Hvordan ville du i stedet sortere alfabetisk efter afdeling?

# ------------------------------------------------------------
# Trin 3 · Hvem er Domain Admins?
# ------------------------------------------------------------
overskrift("Trin 3 · Medlemmer af Domain Admins")
conn.search(domaene, "(cn=Domain Admins)", SUBTREE, attributes=["member"])
medlemmer = conn.entries[0].member.values
print("    antal       :", len(medlemmer))
for dn in medlemmer:
    print("   ", dn)
# TODO: skriv kun navnet (CN-delen) ud for hvert medlem i stedet for hele DN'et
#       (Tip: et DN er tekst. Hvad står før det første komma?)
# 3a. Hvor mange er Domain Admins? Ville du som revisor synes, det er mange eller få?
# 3b. Hvorfor søger vi i hele domænet og ikke kun i OU=Testdata?
# 3c. Hvad sker der med dit split, hvis et navn selv indeholder et komma?

# ------------------------------------------------------------
# Trin 4 · adminCount: konti der er eller har været beskyttede
# ------------------------------------------------------------
#  AD sætter adminCount=1 på konti, der kommer i en beskyttet gruppe (fx Domain Admins).
#  Værdien bliver IKKE fjernet igen, når kontoen tages ud af gruppen.
overskrift("Trin 4 · Konti med adminCount=1")
# TODO: søg i hele domænet efter brugere med adminCount=1, og hent sAMAccountName
# TODO: skriv antallet ud, og sAMAccountName for hver konto
# 4a. Er der flere konti her end i Trin 3? Hvem er de ekstra?
# 4b. Hvorfor er en konto med adminCount=1, som ikke længere er admin, interessant i en audit?

# ------------------------------------------------------------
# Trin 5 · Hvem har ikke logget ind i 90 dage?
# ------------------------------------------------------------
#  lastLogonTimestamp er seneste login. ldap3 laver det om til et datetime-objekt.
#  Har kontoen aldrig logget ind, findes attributten ikke, og .value er None.
overskrift("Trin 5 · Ingen login i 90 dage")
nu = datetime.now(timezone.utc)
graense = "???"                           # TODO: tidspunktet for 90 dage siden (Tip: timedelta)
if graense == "???":
    print("    Udfyld graense i Trin 5.")
    exit()
print("    grænse      :", graense.date())
conn.search(ou, "(objectClass=user)", SUBTREE,
            attributes=["sAMAccountName", "lastLogonTimestamp"])
for e in conn.entries:
    sidst = e.lastLogonTimestamp.value
    if sidst is None:
        print(f"    [ALDRIG]       {e.sAMAccountName.value}")
    # TODO: skriv [INAKTIV], sAMAccountName og datoen ud, hvis sidst er ældre end graense
# 5a. Hvorfor bruger vi timezone.utc og ikke bare datetime.now()?
# 5b. Hvad er forskellen på [ALDRIG] og [INAKTIV]? Hvilken er mest bekymrende?
# 5c. Microsoft opdaterer kun lastLogonTimestamp hver 9-14 dage. Er det et problem for en 90-dages audit?


# ============================================================
#  BONUS · Trin 6-10
#  Gå kun videre, når Trin 1-5 er svaret.
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Lad AD finde de inaktive (LDAP-filter med tid)
# ------------------------------------------------------------
#  I AD er lastLogonTimestamp et stort heltal: antal 100-nanosekunder siden 1. januar 1601.
overskrift("Trin 6 · BONUS · Inaktive med LDAP-filter")
ad_tid = int((graense.timestamp() + 11644473600) * 10_000_000)
print("    ad_tid      :", ad_tid)
filter_inaktiv = "???"                    # TODO: brugere hvor lastLogonTimestamp er mindre end eller lig ad_tid
if filter_inaktiv == "???":
    print("    Udfyld filter_inaktiv i Trin 6.")
    exit()
conn.search(ou, filter_inaktiv, SUBTREE, attributes=["sAMAccountName"])
print("    antal       :", len(conn.entries))
for e in conn.entries:
    print("   ", e.sAMAccountName)
# 6a. Hvad er 11644473600? (Tip: regn det om til år)
# 6b. Kommer brugerne fra [ALDRIG] i Trin 5 med her? Hvorfor ikke?

# ------------------------------------------------------------
# Trin 7 · BONUS · Kodeord der ikke er skiftet i 90 dage
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · pwdLastSet ældre end 90 dage")
# TODO: lav det samme som Trin 5, men med attributten pwdLastSet og mærket [GAMMEL-KODE]
# 7a. Nogle konti viser datoen 1601-01-01. Hvad betyder det?
# 7b. Sammenlign med Sprint 1, Trin 4. Hvilke konti er særligt udsatte?

# ------------------------------------------------------------
# Trin 8 · BONUS · Flere beskyttede grupper
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · Beskyttede grupper")
grupper = ["Domain Admins", "Enterprise Admins", "Schema Admins", "Administrators", "Account Operators"]
# TODO: lav en for-løkke over grupper, søg hver gruppe (som i Trin 3), og skriv navn og antal medlemmer ud
# 8a. Hvilken gruppe har flest medlemmer? Er det et problem?
# 8b. Hvad sker der, hvis du staver et gruppenavn forkert? Hvordan kan scriptet tåle det?

# ------------------------------------------------------------
# Trin 9 · BONUS · Grupper i grupper (nested)
# ------------------------------------------------------------
#  1.2.840.113556.1.4.1941 er en matching rule, der følger medlemskaber hele vejen ned.
overskrift("Trin 9 · BONUS · Alle admins, også via undergrupper")
admin_dn = "CN=Domain Admins,CN=Users,DC=CSIK_DC_1,DC=local"
filter_kaede = "(memberOf:1.2.840.113556.1.4.1941:=" + admin_dn + ")"
conn.search(domaene, filter_kaede, SUBTREE, attributes=["sAMAccountName", "objectClass"])
print("    antal       :", len(conn.entries))
for e in conn.entries:
    print(f"    {e.sAMAccountName.value:<22} {e.objectClass.values[-1]}")
# 9a. Giver det samme antal som Trin 3? Hvorfor kan det være forskelligt?
# 9b. Hvorfor er skjulte admins via undergrupper et klassisk auditfund?

# ------------------------------------------------------------
# Trin 10 · BONUS · Aktive og deaktiverede pr. afdeling
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · Status pr. afdeling")
conn.search(ou, "(objectClass=user)", SUBTREE, attributes=["department", "userAccountControl"])
rapport = {}
# TODO: byg en dict af dicts, fx {"IT": {"aktiv": 3, "deaktiveret": 1}, ...}
#       og skriv en linje ud pr. afdeling
# 10a. Hvorfor skal den indre dict oprettes, før man kan tælle op i den?
# 10b. Denne struktur er klar til JSON i Sprint 4. Hvorfor ville den være besværlig i CSV?

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
