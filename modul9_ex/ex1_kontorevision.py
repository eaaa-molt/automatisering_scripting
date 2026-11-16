# ============================================================
#  MODUL 9 · Sprint 1 · Øvelse 1 · Kontorevision
# ============================================================
#  En kontorevision (audit) er en systematisk gennemgang af konti:
#  hvilke er deaktiverede, hvilke har svage indstillinger, og hvad mangler?
#  Scriptet LÆSER kun fra AD. Det skriver aldrig noget.
#
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
#
#  Trin 1-5 er kernen. Trin 6-10 er BONUS, hvis du har tid tilbage.
# ============================================================
from ldap3 import SUBTREE
from ad_hjaelp import forbind, overskrift

conn = forbind()
ou = "OU=Testdata,DC=CSIK_DC_1,DC=local"

# ------------------------------------------------------------
# Trin 1 · Hvilke brugere er der, og hvad er deres userAccountControl?
# ------------------------------------------------------------
overskrift("Trin 1 · Brugere i OU=Testdata")
conn.search(ou, "(objectClass=user)", SUBTREE,
            attributes=["sAMAccountName", "userAccountControl"])
print("    antal       :", len(conn.entries))
for e in conn.entries:
    print(f"    {e.sAMAccountName.value:<22} {e.userAccountControl.value}")
# 1a. Hvilke forskellige tal ser du i userAccountControl?
# 1b. 512 betyder "normal konto". Hvad er de andre tal? Skriv dem som 512 + noget.
# 1c. Hvorfor gemmer AD mange indstillinger i ét tal i stedet for én attribut pr. indstilling?

# ------------------------------------------------------------
# Trin 2 · Regn selv på tallet: er flaget 2 sat?
# ------------------------------------------------------------
#  Hvert flag er én bit i tallet. "Flaget 2" er den bit, der har værdien 2.
#  & sammenligner to tal bit for bit (se slides).
overskrift("Trin 2 · Deaktiveret? Regnet i Python")
for e in conn.entries:
    uac = e.userAccountControl.value
    deaktiveret = "???"                    # TODO: True hvis flaget 2 er sat i uac, ellers False (brug &)
    if deaktiveret == "???":
        print("    Udfyld deaktiveret i Trin 2.")
        exit()
    print(f"    {e.sAMAccountName.value:<22} {uac:>6}  deaktiveret: {deaktiveret}")
#  Python-konsollen er Python, hvor du skriver én linje ad gangen og får svaret med det samme.
#  Åbn en terminal (Windows: PowerShell, macOS: Terminal, Linux: din terminal) og skriv:
#      Windows:        py           (virker det ikke, så prøv: python)
#      macOS / Linux:  python3
#  Når du ser >>>, skriver du fx 2 + 3 og trykker Enter. Luk igen med exit().
# 2a. Hvad giver 514 & 2, og hvad giver 512 & 2? Prøv det i Python-konsollen.
# 2b. Hvorfor kan man ikke bare skrive uac == 514 for at finde deaktiverede konti?

# ------------------------------------------------------------
# Trin 3 · Kun de deaktiverede konti
# ------------------------------------------------------------
overskrift("Trin 3 · Deaktiverede konti")
conn.search(ou, "(objectClass=user)", SUBTREE,
            attributes=["sAMAccountName", "userAccountControl", "department"])
antal = 0
for e in conn.entries:
    # TODO: skriv kun kontoen ud, hvis flaget 2 er sat, og læg 1 til antal
    #       Brug printet herunder, når betingelsen er på plads:
    #       print(f"    [DEAKTIVERET]  {e.sAMAccountName.value:<22} {e.department}")
    pass
print("    antal       :", antal)
# 3a. Giver Trin 2 og Trin 3 det samme antal deaktiverede konti? Bør de?
# 3b. Hvad står der i department-kolonnen, når en bruger ikke har en afdeling?
# 3c. Scriptet henter ALLE brugere fra AD og sorterer selv. Hvad betyder det, hvis AD har 10.000 brugere?

# ------------------------------------------------------------
# Trin 4 · Kodeord der aldrig udløber
# ------------------------------------------------------------
#  Flaget 65536 hedder DONT_EXPIRE_PASSWORD.
overskrift("Trin 4 · Kodeord udløber aldrig")
conn.search(ou, "(objectClass=user)", SUBTREE,
            attributes=["sAMAccountName", "userAccountControl"])
antal = 0
# TODO: løb conn.entries igennem, og skriv "[UDLØBER-ALDRIG]", sAMAccountName og
#       userAccountControl ud for hver konto, hvor flaget 65536 er sat
# TODO: tæl dem undervejs, og skriv antallet ud til sidst
# 4a. Hvorfor er en konto, hvis kodeord aldrig udløber, en risiko?
# 4b. Hvornår kan det alligevel være rimeligt? (Tip: tænk på servicekonti)
# 4c. En konto har userAccountControl 66050. Er den deaktiveret? Udløber koden? Regn det ud.

# ------------------------------------------------------------
# Trin 5 · Brugere uden afdeling (repetition fra Modul 7)
# ------------------------------------------------------------
overskrift("Trin 5 · Brugere uden afdeling")
# TODO: søg i ou efter brugere, der IKKE har attributten department sat
# TODO: skriv antallet ud og "[INGEN-AFD]" + sAMAccountName for hver bruger
# 5a. Hvilket filter brugte du? Hvad betyder =* alene, og hvad gør ! foran?
# 5b. Hvorfor er det et problem for en audit, at brugere mangler afdeling?
# 5c. Sammenlign med Trin 3: er der brugere, der både er deaktiverede OG mangler afdeling?


# ============================================================
#  BONUS · Trin 6-10
#  Gå kun videre, når Trin 1-5 er svaret.
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Aktive brugere uden afdeling
# ------------------------------------------------------------
overskrift("Trin 6 · BONUS · Aktive brugere uden afdeling")
conn.search(ou, "(&(objectClass=user)(!(department=*)))", SUBTREE,
            attributes=["sAMAccountName", "userAccountControl"])
antal = 0
# TODO: skriv kun de brugere ud, der IKKE er deaktiverede, og tæl dem
print("    antal       :", antal)
# 6a. Hvorfor er aktive konti uden afdeling mere interessante end deaktiverede?
# 6b. Antal i Trin 5 minus antal her. Hvad fortæller det tal?

# ------------------------------------------------------------
# Trin 7 · BONUS · Saml alle fund i én liste
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · Fundliste")
fund = []
conn.search(ou, "(objectClass=user)", SUBTREE,
            attributes=["sAMAccountName", "userAccountControl", "department"])
for e in conn.entries:
    logon = e.sAMAccountName.value
    uac = e.userAccountControl.value
    if (uac & 2) != 0:
        fund.append({"kategori": "DEAKTIVERET", "logon": logon})
    # TODO: tilføj et fund med kategori "UDLØBER-ALDRIG", hvis flaget 65536 er sat
    # TODO: tilføj et fund med kategori "INGEN-AFD", hvis department mangler (Tip: e.department.value is None)

for f in fund:
    print(f"    [{f['kategori']:<15}] {f['logon']}")
print("    fund i alt  :", len(fund))
# 7a. Hvorfor gemmer vi hvert fund som en dict i stedet for en tekststreng?
# 7b. Kan samme konto stå flere gange i listen? Er det en fejl?
# 7c. Hvorfor står der tre if'er og ikke if, elif, elif?

# ------------------------------------------------------------
# Trin 8 · BONUS · Tæl fund pr. kategori
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · Fund pr. kategori")
taeller = {}
# TODO: løb fund igennem, og tæl hvor mange der er i hver kategori
#       (Tip: dict.get(noegle, 0) fra slides)
print("   ", taeller)
# 8a. Passer tallene med Trin 3, 4 og 5?

# ------------------------------------------------------------
# Trin 9 · BONUS · Lad AD filtrere: bitwise LDAP-filter (se slides)
# ------------------------------------------------------------
#  Indtil nu har scriptet hentet ALLE brugere og testet flaget i Python.
#  Med et bitwise LDAP-filter tester AD selv flaget, og kun fundene sendes til scriptet.
overskrift("Trin 9 · BONUS · Deaktiverede konti fundet med LDAP-filter")
filter_deakt = "???"                       # TODO: et bitwise filter, der finder konti hvor flaget 2 er sat
if filter_deakt == "???":
    print("    Udfyld filter_deakt i Trin 9.")
    exit()
conn.search(ou, filter_deakt, SUBTREE, attributes=["sAMAccountName"])
print("    antal       :", len(conn.entries))
for e in conn.entries:
    print(f"    [DEAKTIVERET]  {e.sAMAccountName.value}")
# 9a. Giver det samme antal som Trin 3? Bør det?
# 9b. Hvad er fordelen ved at lade AD filtrere, når AD har 10.000 brugere?
# 9c. Hvad skal du ændre i filtret for at finde kodeord, der aldrig udløber (Trin 4)?

# ------------------------------------------------------------
# Trin 10 · BONUS · Hele domænet, ikke kun Testdata
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · Hele domænet")
domaene = "DC=CSIK_DC_1,DC=local"
conn.search(domaene, filter_deakt, SUBTREE, attributes=["sAMAccountName", "objectClass"])
print("    deaktiverede:", len(conn.entries))
for e in conn.entries:
    print(f"    {e.sAMAccountName.value:<22} {e.objectClass.values[-1]}")
# 10a. Find to konti, du ikke selv har lavet. Hvorfor er krbtgt og Guest deaktiverede?
# 10b. Er der computere med i listen? Hvorfor kan et filter på userAccountControl også ramme computere?
#  Flaget 32 hedder PASSWD_NOTREQD. I Modul 8 oprettede I brugere med 544 = 512 + 32.
# TODO: find alle konti i hele domænet, hvor flaget 32 er sat, med et bitwise filter, og skriv dem ud
# 10c. Hvorfor er flaget 32 en af de første ting, en angriber leder efter?
# 10d. Hvilke tre audit-tjek fra i dag ville du køre hver uge i en rigtig virksomhed?

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
