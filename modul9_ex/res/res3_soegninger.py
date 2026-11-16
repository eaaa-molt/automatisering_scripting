# ============================================================
#  MODUL 9 · Sprint 3 · Løsning 3 · Målrettede søgninger
# ============================================================
#  Løsningsforslag. Hver opgave (TODO) og hvert spørgsmål står som i
#  øvelsen, med løsningen eller svaret lige under.
#  Tal i svarene afhænger af, hvad der ligger i AD på dagen.
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
    taeller[afd] = taeller.get(afd, 0) + 1
print("   ", taeller)
# 1a. Hvad sker der første gang en afdeling dukker op i løkken? Hvad gør .get(afd, 0)?
#     Svar: Afdelingen findes ikke som nøgle endnu. get giver så 0 i stedet for en
#           KeyError, og 0 + 1 = 1 bliver gemt. Næste gang findes nøglen og tælles op.
# 1b. Hvad ville taeller[afd] += 1 gøre første gang? Prøv det.
#     Svar: KeyError, fordi nøglen ikke findes endnu. Man kan ikke lægge til noget,
#           der ikke er der.
# 1c. Summen af alle tallene. Passer den med antallet af brugere fra Sprint 1, Trin 1?
#     Svar: Ja. Hver bruger tælles præcis én gang, også dem uden afdeling, fordi de
#           får "(ingen)".

# ------------------------------------------------------------
# Trin 2 · Sortér, så den største afdeling står øverst
# ------------------------------------------------------------
overskrift("Trin 2 · Afdelinger, største først")
# TODO: taeller.items() sorteret efter antal, største først
sorteret = sorted(taeller.items(), key=lambda x: x[1], reverse=True)
for afd, antal in sorteret:
    print(f"    {afd:<20} {antal:>3}")
# 2a. Hvad er x i lambda x: x[1]? Hvad er x[0]?
#     Svar: x er ét par (afdeling, antal) fra taeller.items(). x[0] er afdelingen,
#           x[1] er antallet. Vi sorterer altså på antallet.
# 2b. Hvad sker der, hvis du fjerner reverse=True?
#     Svar: Den mindste afdeling kommer øverst (stigende rækkefølge).
# 2c. Hvordan ville du i stedet sortere alfabetisk efter afdeling?
#     Svar: key=lambda x: x[0], eller bare sorted(taeller.items()), som sorterer på
#           første element som standard.

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
for dn in medlemmer:
    navn = dn.split(",")[0].replace("CN=", "")
    print("    admin       :", navn)
# 3a. Hvor mange er Domain Admins? Ville du som revisor synes, det er mange eller få?
#     Svar: Afhænger af data. Domain Admins skal være så få som muligt (typisk 2-5 navngivne
#           personer plus en nødkonto). Hver admin-konto er et mål for en angriber.
# 3b. Hvorfor søger vi i hele domænet og ikke kun i OU=Testdata?
#     Svar: Domain Admins ligger i containeren CN=Users, ikke i Testdata. Admin-grupper
#           og admin-konti kan ligge alle steder, så en audit skal se hele domænet.
# 3c. Hvad sker der med dit split, hvis et navn selv indeholder et komma?
#     Svar: Navnet bliver skåret over. I DN'et står kommaet escaped som \, og et simpelt
#           split tager ikke hensyn til det. Til en rapport er det godt nok, men ikke helt
#           sikkert.

# ------------------------------------------------------------
# Trin 4 · adminCount: konti der er eller har været beskyttede
# ------------------------------------------------------------
#  AD sætter adminCount=1 på konti, der kommer i en beskyttet gruppe (fx Domain Admins).
#  Værdien bliver IKKE fjernet igen, når kontoen tages ud af gruppen.
overskrift("Trin 4 · Konti med adminCount=1")
# TODO: søg i hele domænet efter brugere med adminCount=1, og hent sAMAccountName
conn.search(domaene, "(&(objectClass=user)(adminCount=1))", SUBTREE,
            attributes=["sAMAccountName"])
# TODO: skriv antallet ud, og sAMAccountName for hver konto
print("    antal       :", len(conn.entries))
for e in conn.entries:
    print("   ", e.sAMAccountName)
# 4a. Er der flere konti her end i Trin 3? Hvem er de ekstra?
#     Svar: Typisk ja. De ekstra er konti, der er medlem af andre beskyttede grupper
#           (fx Administrators, Account Operators), eller som tidligere har været det.
#           krbtgt har også adminCount=1.
# 4b. Hvorfor er en konto med adminCount=1, som ikke længere er admin, interessant i en audit?
#     Svar: Den har været admin og kan stadig have rettigheder eller ACL'er tilbage.
#           Ofte er det en glemt oprydning efter en medarbejder, der skiftede rolle.

# ------------------------------------------------------------
# Trin 5 · Hvem har ikke logget ind i 90 dage?
# ------------------------------------------------------------
#  lastLogonTimestamp er seneste login. ldap3 laver det om til et datetime-objekt.
#  Har kontoen aldrig logget ind, findes attributten ikke, og .value er None.
overskrift("Trin 5 · Ingen login i 90 dage")
nu = datetime.now(timezone.utc)
# TODO: tidspunktet for 90 dage siden (Tip: timedelta)
graense = nu - timedelta(days=90)
print("    grænse      :", graense.date())
conn.search(ou, "(objectClass=user)", SUBTREE,
            attributes=["sAMAccountName", "lastLogonTimestamp"])
for e in conn.entries:
    sidst = e.lastLogonTimestamp.value
    if sidst is None:
        print(f"    [ALDRIG]       {e.sAMAccountName.value}")
    # TODO: skriv [INAKTIV], sAMAccountName og datoen ud, hvis sidst er ældre end graense
    elif sidst < graense:
        print(f"    [INAKTIV]      {e.sAMAccountName.value:<22} {sidst.date()}")
# 5a. Hvorfor bruger vi timezone.utc og ikke bare datetime.now()?
#     Svar: AD gemmer tider i UTC, og ldap3 giver et datetime med tidszone. Python vil
#           ikke sammenligne et datetime med tidszone og et uden (TypeError). Prøv det.
# 5b. Hvad er forskellen på [ALDRIG] og [INAKTIV]? Hvilken er mest bekymrende?
#     Svar: ALDRIG er oprettet, men aldrig brugt. INAKTIV har været i brug, men ikke for
#           nylig. Begge er kandidater til at blive deaktiveret. En gammel aktiv konto,
#           som ingen bruger, er det klassiske mål, fordi ingen opdager misbrug.
# 5c. Microsoft opdaterer kun lastLogonTimestamp hver 9-14 dage. Er det et problem for en 90-dages audit?
#     Svar: Nej. Unøjagtigheden er højst 14 dage, og det er lille i forhold til 90.
#           Til en præcis "sidst logget ind i går" skal man bruge lastLogon på hver DC.


# ============================================================
#  BONUS · Trin 6-10
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Lad AD finde de inaktive (LDAP-filter med tid)
# ------------------------------------------------------------
#  I AD er lastLogonTimestamp et stort heltal: antal 100-nanosekunder siden 1. januar 1601.
overskrift("Trin 6 · BONUS · Inaktive med LDAP-filter")
ad_tid = int((graense.timestamp() + 11644473600) * 10_000_000)
print("    ad_tid      :", ad_tid)
# TODO: brugere hvor lastLogonTimestamp er mindre end eller lig ad_tid
filter_inaktiv = "(&(objectClass=user)(lastLogonTimestamp<=" + str(ad_tid) + "))"
conn.search(ou, filter_inaktiv, SUBTREE, attributes=["sAMAccountName"])
print("    antal       :", len(conn.entries))
for e in conn.entries:
    print("   ", e.sAMAccountName)
# 6a. Hvad er 11644473600? (Tip: regn det om til år)
#     Svar: Antal sekunder fra 1. januar 1601 til 1. januar 1970 (ca. 369 år).
#           Python regner fra 1970 (Unix-tid), Windows fra 1601.
# 6b. Kommer brugerne fra [ALDRIG] i Trin 5 med her? Hvorfor ikke?
#     Svar: Nej. De har ingen lastLogonTimestamp, og et filter kan ikke sammenligne en
#           værdi, der ikke findes. De skal findes med (!(lastLogonTimestamp=*)).

# ------------------------------------------------------------
# Trin 7 · BONUS · Kodeord der ikke er skiftet i 90 dage
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · pwdLastSet ældre end 90 dage")
# TODO: lav det samme som Trin 5, men med attributten pwdLastSet og mærket [GAMMEL-KODE]
conn.search(ou, "(objectClass=user)", SUBTREE, attributes=["sAMAccountName", "pwdLastSet"])
for e in conn.entries:
    sat = e.pwdLastSet.value
    if sat is not None and sat < graense:
        print(f"    [GAMMEL-KODE]  {e.sAMAccountName.value:<22} {sat.date()}")
# 7a. Nogle konti viser datoen 1601-01-01. Hvad betyder det?
#     Svar: pwdLastSet er 0. Det betyder "skal skifte kodeord ved næste login" (fx en ny
#           konto eller en nulstillet kode). ldap3 viser 0 som 1601-01-01.
# 7b. Sammenlign med Sprint 1, Trin 4. Hvilke konti er særligt udsatte?
#     Svar: Konti hvor koden aldrig udløber OG ikke er skiftet længe. Den kode har været
#           i brug længe og bliver aldrig tvunget skiftet.

# ------------------------------------------------------------
# Trin 8 · BONUS · Flere beskyttede grupper
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · Beskyttede grupper")
grupper = ["Domain Admins", "Enterprise Admins", "Schema Admins", "Administrators", "Account Operators"]
# TODO: lav en for-løkke over grupper, søg hver gruppe (som i Trin 3), og skriv navn og antal medlemmer ud
for g in grupper:
    conn.search(domaene, "(cn=" + g + ")", SUBTREE, attributes=["member"])
    print(f"    {g:<20} {len(conn.entries[0].member.values):>3}")
# 8a. Hvilken gruppe har flest medlemmer? Er det et problem?
#     Svar: Afhænger af data. Account Operators kan oprette og ændre de fleste brugere og
#           grupper. Mange medlemmer her er en reel risiko og bør ryddes op.
# 8b. Hvad sker der, hvis du staver et gruppenavn forkert? Hvordan kan scriptet tåle det?
#     Svar: conn.entries er tom, og conn.entries[0] giver IndexError. Tjek med
#           if not conn.entries: før man bruger [0], og skriv fx "findes ikke".

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
#     Svar: Hvis en gruppe er medlem af Domain Admins, er dens medlemmer også admins.
#           Trin 3 viser kun de direkte medlemmer. Filtret her viser alle, også gennem
#           undergrupper.
# 9b. Hvorfor er skjulte admins via undergrupper et klassisk auditfund?
#     Svar: De ses ikke, når man kigger på gruppen i ADUC. Man kan tro, der er 3 admins,
#           men der er 30. Angribere leder netop efter sådanne veje (fx med BloodHound).

# ------------------------------------------------------------
# Trin 10 · BONUS · Aktive og deaktiverede pr. afdeling
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · Status pr. afdeling")
conn.search(ou, "(objectClass=user)", SUBTREE, attributes=["department", "userAccountControl"])
rapport = {}
# TODO: byg en dict af dicts, fx {"IT": {"aktiv": 3, "deaktiveret": 1}, ...}
#       og skriv en linje ud pr. afdeling
for e in conn.entries:
    afd = e.department.value
    if afd is None:
        afd = "(ingen)"
    if afd not in rapport:
        rapport[afd] = {"aktiv": 0, "deaktiveret": 0}
    if e.userAccountControl.value & 2 != 0:
        rapport[afd]["deaktiveret"] += 1
    else:
        rapport[afd]["aktiv"] += 1
for afd, tal in rapport.items():
    print(f"    {afd:<20} aktiv {tal['aktiv']:>3}   deaktiveret {tal['deaktiveret']:>3}")
# 10a. Hvorfor skal den indre dict oprettes, før man kan tælle op i den?
#      Svar: rapport[afd]["aktiv"] += 1 kræver, at rapport[afd] allerede er en dict med
#            nøglen "aktiv". Ellers giver det KeyError, ligesom i 1b.
# 10b. Denne struktur er klar til JSON i Sprint 4. Hvorfor ville den være besværlig i CSV?
#      Svar: CSV er en flad tabel med én værdi pr. celle. En dict i en dict skal laves om til
#            kolonner (afdeling, aktiv, deaktiveret). JSON kan gemme strukturen direkte.

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
