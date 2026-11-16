# ============================================================
#  MODUL 9 · Sprint 1 · Løsning 1 · Kontorevision
# ============================================================
#  Løsningsforslag. Hver opgave (TODO) og hvert spørgsmål står som i
#  øvelsen, med løsningen eller svaret lige under.
#  Tal i svarene afhænger af, hvad der ligger i AD på dagen.
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
#     Svar: Typisk 512 og 514, måske også 66048, 66050 eller 544.
#
# 1b. 512 betyder "normal konto". Hvad er de andre tal? Skriv dem som 512 + noget.
#     Svar: 514 = 512 + 2 (deaktiveret)
#           544 = 512 + 32 (kodeord ikke påkrævet)
#           66048 = 512 + 65536 (kodeord udløber aldrig)
#           66050 = 512 + 65536 + 2 (udløber aldrig og deaktiveret)
#
# 1c. Hvorfor gemmer AD mange indstillinger i ét tal i stedet for én attribut pr. indstilling?
#     Svar: Hvert flag er én bit, så mange ja/nej-indstillinger fylder ét tal og kan
#           kombineres frit. Det er kompakt og stammer fra den gamle NT-kontodatabase.
#           Prisen er, at man skal bruge bitoperationer for at læse det.

# ------------------------------------------------------------
# Trin 2 · Regn selv på tallet: er flaget 2 sat?
# ------------------------------------------------------------
#  Hvert flag er én bit i tallet. "Flaget 2" er den bit, der har værdien 2.
#  & sammenligner to tal bit for bit (se slides).
overskrift("Trin 2 · Deaktiveret? Regnet i Python")
for e in conn.entries:
    uac = e.userAccountControl.value
    # TODO: True hvis flaget 2 er sat i uac, ellers False (brug &)
    deaktiveret = (uac & 2) != 0
    print(f"    {e.sAMAccountName.value:<22} {uac:>6}  deaktiveret: {deaktiveret}")
#  Python-konsollen er Python, hvor du skriver én linje ad gangen og får svaret med det samme.
#  Åbn en terminal (Windows: PowerShell, macOS: Terminal, Linux: din terminal) og skriv:
#      Windows:        py           (virker det ikke, så prøv: python)
#      macOS / Linux:  python3
#  Når du ser >>>, skriver du fx 2 + 3 og trykker Enter. Luk igen med exit().
# 2a. Hvad giver 514 & 2, og hvad giver 512 & 2? Prøv det i Python-konsollen.
#     Svar: 514 & 2 = 2 og 512 & 2 = 0. Binært er 514 = 1000000010 og 512 = 1000000000,
#           så kun 514 har flaget 2 sat. Alt andet end 0 betyder "sat".
#
# 2b. Hvorfor kan man ikke bare skrive uac == 514 for at finde deaktiverede konti?
#     Svar: Andre bit kan også være sat. 66050 er deaktiveret, men er ikke lig 514.
#           Man skal teste den ene bit, ikke hele tallet.

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
    if (e.userAccountControl.value & 2) != 0:
        print(f"    [DEAKTIVERET]  {e.sAMAccountName.value:<22} {e.department}")
        antal = antal + 1
print("    antal       :", antal)
# 3a. Giver Trin 2 og Trin 3 det samme antal deaktiverede konti? Bør de?
#     Svar: Ja. Begge tester flaget 2 med &. Trin 3 skriver bare kun fundene ud.
#           Er tallene forskellige, er der en fejl i betingelsen.
#
# 3b. Hvad står der i department-kolonnen, når en bruger ikke har en afdeling?
#     Svar: [] (en tom liste). Attributten findes ikke på objektet, og ldap3 viser den som tom.
#
# 3c. Scriptet henter ALLE brugere fra AD og sorterer selv. Hvad betyder det, hvis AD har 10.000 brugere?
#     Svar: Alle 10.000 konti sendes over netværket, selvom vi kun skal bruge få af dem.
#           AD sender desuden højst 1000 objekter pr. søgning som standard, så scriptet
#           ville få et forkert resultat uden at sige det. BONUS Trin 9 viser, hvordan AD
#           selv kan filtrere.

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
for e in conn.entries:
    uac = e.userAccountControl.value
    if (uac & 65536) != 0:
        print(f"    [UDLØBER-ALDRIG]  {e.sAMAccountName.value:<22} {uac}")
        antal = antal + 1
# TODO: tæl dem undervejs, og skriv antallet ud til sidst
print("    antal       :", antal)
# 4a. Hvorfor er en konto, hvis kodeord aldrig udløber, en risiko?
#     Svar: Et lækket eller gættet kodeord virker for altid. Kontoen bliver aldrig tvunget
#           til et nyt kodeord, så et brud kan vare i årevis uden at blive opdaget.
#
# 4b. Hvornår kan det alligevel være rimeligt? (Tip: tænk på servicekonti)
#     Svar: Servicekonti, hvor et udløbet kodeord ville stoppe en tjeneste. Så skal kodeordet
#           være langt og tilfældigt og dokumenteret. Endnu bedre er en gMSA, hvor AD selv
#           skifter kodeordet automatisk.
#
# 4c. En konto har userAccountControl 66050. Er den deaktiveret? Udløber koden? Regn det ud.
#     Svar: 66050 = 65536 + 512 + 2. Den er deaktiveret (flaget 2), og koden udløber aldrig
#           (flaget 65536). 66050 & 2 = 2 og 66050 & 65536 = 65536.

# ------------------------------------------------------------
# Trin 5 · Brugere uden afdeling (repetition fra Modul 7)
# ------------------------------------------------------------
overskrift("Trin 5 · Brugere uden afdeling")
# TODO: søg i ou efter brugere, der IKKE har attributten department sat
filter_ingen_afd = "(&(objectClass=user)(!(department=*)))"
conn.search(ou, filter_ingen_afd, SUBTREE, attributes=["sAMAccountName"])
# TODO: skriv antallet ud og "[INGEN-AFD]" + sAMAccountName for hver bruger
print("    antal       :", len(conn.entries))
for e in conn.entries:
    print(f"    [INGEN-AFD]    {e.sAMAccountName.value}")
# 5a. Hvilket filter brugte du? Hvad betyder =* alene, og hvad gør ! foran?
#     Svar: (&(objectClass=user)(!(department=*))). (department=*) betyder "department har
#           en værdi". ! vender det om til "department har ingen værdi".
#
# 5b. Hvorfor er det et problem for en audit, at brugere mangler afdeling?
#     Svar: Man kan ikke se, hvem kontoen hører til, eller hvem der skal godkende dens
#           rettigheder. Det kan være en ejerløs konto, som ingen opdager, når den ikke
#           længere bruges. Det tyder også på, at oprettelsesprocessen ikke bliver fulgt.
#
# 5c. Sammenlign med Trin 3: er der brugere, der både er deaktiverede OG mangler afdeling?
#     Svar: Afhænger af data. Se efter logonnavne, der står i begge lister.


# ============================================================
#  BONUS · Trin 6-10
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Aktive brugere uden afdeling
# ------------------------------------------------------------
overskrift("Trin 6 · BONUS · Aktive brugere uden afdeling")
conn.search(ou, "(&(objectClass=user)(!(department=*)))", SUBTREE,
            attributes=["sAMAccountName", "userAccountControl"])
antal = 0
# TODO: skriv kun de brugere ud, der IKKE er deaktiverede, og tæl dem
for e in conn.entries:
    if (e.userAccountControl.value & 2) == 0:
        print("   ", e.sAMAccountName)
        antal = antal + 1
print("    antal       :", antal)
# 6a. Hvorfor er aktive konti uden afdeling mere interessante end deaktiverede?
#     Svar: En aktiv konto kan logge ind lige nu. Er den ejerløs, er den en angrebsflade,
#           som ingen holder øje med. En deaktiveret konto kan ikke bruges, før nogen
#           aktiverer den igen.
#
# 6b. Antal i Trin 5 minus antal her. Hvad fortæller det tal?
#     Svar: Antallet af deaktiverede brugere uden afdeling (svaret på 5c som tal).

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
    if (uac & 65536) != 0:
        fund.append({"kategori": "UDLØBER-ALDRIG", "logon": logon})
    # TODO: tilføj et fund med kategori "INGEN-AFD", hvis department mangler (Tip: e.department.value is None)
    if e.department.value is None:
        fund.append({"kategori": "INGEN-AFD", "logon": logon})

for f in fund:
    print(f"    [{f['kategori']:<15}] {f['logon']}")
print("    fund i alt  :", len(fund))
# 7a. Hvorfor gemmer vi hvert fund som en dict i stedet for en tekststreng?
#     Svar: Så kategori og logon er adskilte felter. Man kan tælle, filtrere og sortere på
#           kategori uden at skille tekst ad. Listen kan også gemmes direkte som JSON eller
#           CSV (Sprint 2 og 4).
#
# 7b. Kan samme konto stå flere gange i listen? Er det en fejl?
#     Svar: Ja, fx både DEAKTIVERET og INGEN-AFD. Det er ikke en fejl, for hvert fund er en
#           selvstændig observation. Vil man tælle antal konti, skal man tælle unikke
#           logonnavne, fx med et set.
#
# 7c. Hvorfor står der tre if'er og ikke if, elif, elif?
#     Svar: Med elif stopper Python ved det første fund. En konto kan være både deaktiveret
#           og mangle afdeling, så alle tre tjek skal køre hver gang.

# ------------------------------------------------------------
# Trin 8 · BONUS · Tæl fund pr. kategori
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · Fund pr. kategori")
taeller = {}
# TODO: løb fund igennem, og tæl hvor mange der er i hver kategori
#       (Tip: dict.get(noegle, 0) fra slides)
for f in fund:
    taeller[f["kategori"]] = taeller.get(f["kategori"], 0) + 1
print("   ", taeller)
# 8a. Passer tallene med Trin 3, 4 og 5?
#     Svar: Ja. DEAKTIVERET = antal i Trin 3, UDLØBER-ALDRIG = Trin 4, INGEN-AFD = Trin 5.

# ------------------------------------------------------------
# Trin 9 · BONUS · Lad AD filtrere: bitwise LDAP-filter (se slides)
# ------------------------------------------------------------
#  Indtil nu har scriptet hentet ALLE brugere og testet flaget i Python.
#  Med et bitwise LDAP-filter tester AD selv flaget, og kun fundene sendes til scriptet.
overskrift("Trin 9 · BONUS · Deaktiverede konti fundet med LDAP-filter")
# TODO: et bitwise filter, der finder konti hvor flaget 2 er sat
filter_deakt = "(userAccountControl:1.2.840.113556.1.4.803:=2)"
conn.search(ou, filter_deakt, SUBTREE, attributes=["sAMAccountName"])
print("    antal       :", len(conn.entries))
for e in conn.entries:
    print(f"    [DEAKTIVERET]  {e.sAMAccountName.value}")
# 9a. Giver det samme antal som Trin 3? Bør det?
#     Svar: Ja. Begge tester flaget 2. Trin 3 gør det i Python, her gør AD det.
#
# 9b. Hvad er fordelen ved at lade AD filtrere, når AD har 10.000 brugere?
#     Svar: Kun de matchende konti sendes over netværket, så der er mindre trafik og
#           hukommelse i scriptet. Grænsen på 1000 objekter pr. søgning rammer også
#           sjældnere, fordi der kommer færre fund tilbage.
#
# 9c. Hvad skal du ændre i filtret for at finde kodeord, der aldrig udløber (Trin 4)?
#     Svar: Kun tallet til sidst: (userAccountControl:1.2.840.113556.1.4.803:=65536).

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
#      Svar: krbtgt er den konto, hvis nøgle domænecontrolleren bruger til at signere
#            Kerberos-tickets. Den skal aldrig logge ind og er deaktiveret fra start.
#            Guest er den indbyggede gæstekonto uden kodeord, så den er slået fra af
#            sikkerhedshensyn.
#
# 10b. Er der computere med i listen? Hvorfor kan et filter på userAccountControl også ramme computere?
#      Svar: Det afhænger af, om der er deaktiverede computerkonti. Computerkonti har også
#            userAccountControl, og i AD-skemaet er computer en underklasse af user.
#            Kombinér med (objectCategory=person) i et AND-filter for kun at få brugere.
#
#  Flaget 32 hedder PASSWD_NOTREQD. I Modul 8 oprettede I brugere med 544 = 512 + 32.
# TODO: find alle konti i hele domænet, hvor flaget 32 er sat, med et bitwise filter, og skriv dem ud
conn.search(domaene, "(userAccountControl:1.2.840.113556.1.4.803:=32)", SUBTREE,
            attributes=["sAMAccountName", "distinguishedName"])
print("    flaget 32   :", len(conn.entries))
for e in conn.entries:
    print(f"    {e.sAMAccountName.value:<22} {e.distinguishedName.value}")
# 10c. Hvorfor er flaget 32 en af de første ting, en angriber leder efter?
#      Svar: Kontoen må have et tomt kodeord, så man kan måske logge ind uden kode.
#            Det er nemt at finde med ét filter, og værktøjer som BloodHound og PingCastle
#            tjekker det som standard.
#
# 10d. Hvilke tre audit-tjek fra i dag ville du køre hver uge i en rigtig virksomhed?
#      Svar: Frit svar med en begrundelse. Fx aktive konti uden afdeling (ejerløse),
#            kodeord udløber aldrig (svage konti) og kodeord ikke påkrævet (tomme koder).
#            Deaktiverede konti er mest relevante til oprydning.

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
