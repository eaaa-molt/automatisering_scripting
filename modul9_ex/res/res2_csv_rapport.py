# ============================================================
#  MODUL 9 · Sprint 2 · Løsning 2 · CSV-rapport
# ============================================================
#  Løsningsforslag. Hver opgave (TODO) og hvert spørgsmål står som i
#  øvelsen, med løsningen eller svaret lige under.
#  Tal i svarene afhænger af, hvad der ligger i AD på dagen.
#
#  Trin 1-5 er kernen. Trin 6-10 er BONUS, hvis du har tid tilbage.
# ============================================================
import csv
from pathlib import Path
from ldap3 import SUBTREE
from ad_hjaelp import forbind, overskrift

conn = forbind()
ou = "OU=Testdata,DC=CSIK_DC_1,DC=local"
mappe = Path(__file__).parent              # CSV-filerne lægges ved siden af scriptet

# ------------------------------------------------------------
# Trin 1 · Hent brugerne (repetition fra Sprint 1)
# ------------------------------------------------------------
overskrift("Trin 1 · Brugere i OU=Testdata")
conn.search(ou, "(objectClass=user)", SUBTREE,
            attributes=["sAMAccountName", "cn", "department", "title", "userAccountControl"])
print("    antal       :", len(conn.entries))
print(conn.entries[0])
# 1a. Hvilke af de fem attributter har den første bruger? Hvilke mangler?
#     Svar: Afhænger af brugeren. sAMAccountName, cn og userAccountControl har alle
#           brugere. department og title mangler ofte, og så står de slet ikke i udskriften.
# 1b. Hvorfor er conn.entries ikke klar til at blive skrevet direkte til en CSV-fil?
#     Svar: Hver entry er et ldap3-objekt med attributobjekter, ikke almindelig tekst.
#           CSV skal bruge rækker af simple værdier (tekst og tal). Vi skal selv vælge
#           kolonnerne og oversætte fx userAccountControl til noget læsbart.

# ------------------------------------------------------------
# Trin 2 · Lav én dict pr. bruger
# ------------------------------------------------------------
overskrift("Trin 2 · Brugerne som en liste af dicts")
brugere = []
for e in conn.entries:
    afdeling = e.department.value
    if afdeling is None:                   # brugeren har ingen afdeling
        afdeling = ""
    # TODO: "Deaktiveret" hvis flaget 2 er sat, ellers "Aktiv" (se Sprint 1)
    if e.userAccountControl.value & 2 != 0:
        status = "Deaktiveret"
    else:
        status = "Aktiv"
    brugere.append({"logon": e.sAMAccountName.value,
                    "navn": e.cn.value,
                    "afdeling": afdeling,
                    "status": status})
print("    antal dicts :", len(brugere))
print("    første      :", brugere[0])
# 2a. Hvad ville der stå i afdeling, hvis vi fjernede if-sætningen? Hvorfor er det dårligt i en CSV?
#     Svar: None. I CSV-filen ville der stå teksten "None", som ligner en afdeling, der
#           hedder None. En tom celle viser tydeligt, at værdien mangler.
# 2b. Hvorfor gemmer vi "Aktiv"/"Deaktiveret" i stedet for selve tallet 512/514?
#     Svar: Den, der læser rapporten, skal ikke kende userAccountControl-flagene. En rapport
#           skal kunne læses af en leder eller revisor uden teknisk viden.

# ------------------------------------------------------------
# Trin 3 · Skriv listen til brugere.csv
# ------------------------------------------------------------
overskrift("Trin 3 · Skriv brugere.csv")
fil = mappe / "brugere.csv"
with open(fil, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["logon", "navn", "afdeling", "status"])
    # TODO: skriv overskriftsrækken
    writer.writeheader()
    # TODO: skriv én række pr. dict i brugere med en for-løkke
    for b in brugere:
        writer.writerow(b)
print("    gemt        :", fil)
print("    størrelse   :", fil.stat().st_size, "bytes")
# 3a. Åbn brugere.csv i VS Code. Hvad står der i første linje? Hvor kommer det fra?
#     Svar: logon,navn,afdeling,status. Det er fieldnames, som writeheader() skriver.
# 3b. Hvad sker der, hvis du glemmer writeheader()? Prøv det.
#     Svar: Filen starter direkte med data. Ingen ved, hvad kolonnerne betyder, og
#           DictReader i Trin 5 vil bruge første bruger som kolonnenavne.
# 3c. Hvorfor bruger vi en DictWriter og ikke bare f.write() med kommaer imellem?
#     Svar: DictWriter sørger for kolonnernes rækkefølge og sætter anførselstegn om
#           værdier, der selv indeholder komma eller linjeskift. Med f.write() skal man
#           selv huske det hele (se Trin 10).

# ------------------------------------------------------------
# Trin 4 · Åbn filen i et regneark
# ------------------------------------------------------------
overskrift("Trin 4 · Åbn brugere.csv i Excel, Numbers eller LibreOffice")
print("    Find filen her:", fil)
# 4a. Vises æ, ø og å korrekt (fx i en afdeling som Økonomi eller i et navn)?
#     Svar: Ja, fordi filen er skrevet med utf-8-sig. Det kan afhænge af programmet.
# 4b. Står alle værdier i én kolonne, eller er de fordelt i fire kolonner?
#     Svar: Med dansk Excel står alt ofte i én kolonne. Dansk Excel forventer semikolon som
#           skilletegn, fordi komma er decimaltegn på dansk. Numbers og LibreOffice
#           spørger eller gætter rigtigt. Se BONUS Trin 7.
# 4c. Skift "utf-8-sig" til "utf-8" i Trin 3, kør igen og åbn filen i Excel. Hvad sker der?
#     Svar: Excel tror, filen er i en gammel tegnsæt-standard, og æøå bliver til mærkelige
#           tegn (fx Ã¸). utf-8-sig skriver tre usynlige bytes (BOM) først i filen, som
#           fortæller Excel, at det er UTF-8. Husk at skifte tilbage.
# 4d. Hvor mange bytes blev filen større med utf-8-sig end med utf-8?
#     Svar: 3 bytes. Det er BOM'en (EF BB BF).

# ------------------------------------------------------------
# Trin 5 · Læs filen tilbage og tjek den
# ------------------------------------------------------------
overskrift("Trin 5 · Læs brugere.csv igen")
with open(fil, newline="", encoding="utf-8-sig") as f:
    raekker = list(csv.DictReader(f))
print("    rækker      :", len(raekker))
print("    første      :", raekker[0])
# TODO: tæl hvor mange rækker der har status "Deaktiveret", og skriv tallet ud
antal_deakt = 0
for r in raekker:
    if r["status"] == "Deaktiveret":
        antal_deakt += 1
print("    deaktiverede:", antal_deakt)
# TODO: skriv logon ud for hver deaktiveret bruger
for r in raekker:
    if r["status"] == "Deaktiveret":
        print("   ", r["logon"])
# 5a. Er antallet af rækker det samme som i Trin 1? Hvorfor er det et godt tjek?
#     Svar: Ja, det skal det være. Så ved man, at ingen brugere er gået tabt på vejen
#           fra AD til fil. Et script, der tjekker sit eget output, er mere troværdigt.
# 5b. Passer antallet af deaktiverede med Sprint 1, Trin 3?
#     Svar: Ja, hvis ingen har ændret noget i AD imellem. Begge bygger på flaget 2.
# 5c. Hvilken datatype har r["status"]? Hvilken datatype ville et tal fra CSV-filen have?
#     Svar: str. Alt, hvad der læses fra en CSV-fil, er tekst. Et tal skal laves om med
#           int(), før man kan regne med det. CSV gemmer ikke datatyper (det gør JSON).


# ============================================================
#  BONUS · Trin 6-10
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Tilføj en kolonne med titel
# ------------------------------------------------------------
overskrift("Trin 6 · BONUS · Kolonnen titel")
# TODO: tilføj "titel" til hver dict i Trin 2 (samme mønster som afdeling)
# TODO: tilføj "titel" til fieldnames i Trin 3, og kør igen
#   Løsning: i Trin 2:   titel = e.title.value
#                        if titel is None:
#                            titel = ""
#            og          "titel": titel   i dict'en
#            i Trin 3:   fieldnames=["logon", "navn", "afdeling", "titel", "status"]
print("    kolonner    :", list(brugere[0].keys()))
# 6a. Hvad sker der, hvis du tilføjer titel til dict'en, men glemmer den i fieldnames?
#     Svar: DictWriter giver en ValueError: "dict contains fields not in fieldnames".
#           Det er en fordel, for så opdager man fejlen i stedet for at miste data.
# 6b. Hvad sker der omvendt, hvis titel står i fieldnames, men mangler i en dict?
#     Svar: Cellen bliver bare tom. DictWriter udfylder manglende felter med "".

# ------------------------------------------------------------
# Trin 7 · BONUS · En version til dansk Excel
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · brugere_excel.csv med semikolon")
fil_excel = mappe / "brugere_excel.csv"
# TODO: skriv brugere til fil_excel som i Trin 3, men med semikolon som skilletegn
#       (Tip: DictWriter har en parameter, der hedder delimiter)
# TODO: brug de danske kolonnenavne "Logonnavn", "Navn", "Afdeling" og "Status" i overskriften
#       (Tip: writeheader() skriver nøglerne. Prøv i stedet writer.writerow() med en dict)
with open(fil_excel, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["logon", "navn", "afdeling", "status"], delimiter=";")
    writer.writerow({"logon": "Logonnavn", "navn": "Navn", "afdeling": "Afdeling", "status": "Status"})
    for b in brugere:
        writer.writerow(b)
print("    gemt        :", fil_excel)
# 7a. Åbn begge filer i Excel. Hvilken ser rigtig ud nu?
#     Svar: På en dansk Excel ser brugere_excel.csv rigtig ud (fire kolonner). På en engelsk
#           Excel er det omvendt. Skilletegnet afhænger af computerens sprogindstilling.
# 7b. Hvorfor er det et problem for en rapport, der skal deles på tværs af lande?
#     Svar: Den samme fil ser forskellig ud hos modtagerne. Derfor bruger man ofte
#           JSON eller xlsx til maskiner og aftaler skilletegn, når der bruges CSV.

# ------------------------------------------------------------
# Trin 8 · BONUS · Sortér rapporten
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · Sorteret efter afdeling og logon")
# TODO: brugere sorteret efter afdeling, og inden for afdeling efter logon
#       (Tip: sorted() med key=lambda, og en tuple som nøgle)
sorteret = sorted(brugere, key=lambda b: (b["afdeling"], b["logon"]))
for b in sorteret:
    print(f"    {b['afdeling']:<15} {b['logon']:<22} {b['status']}")
# 8a. Hvor havner brugerne uden afdeling? Hvorfor?
#     Svar: Øverst, fordi den tomme tekst "" sorteres før alle andre tekster.
# 8b. Hvordan ville du få de deaktiverede brugere øverst i stedet?
#     Svar: Sortér på status først, fx key=lambda b: (b["status"], b["logon"]).
#           "Aktiv" kommer før "Deaktiveret", så tilføj reverse=True eller byt rækkefølgen.

# ------------------------------------------------------------
# Trin 9 · BONUS · En rapport kun med fund
# ------------------------------------------------------------
overskrift("Trin 9 · BONUS · mangler_afdeling.csv")
# TODO: kun de AKTIVE brugere uden afdeling (list comprehension eller for-løkke)
fund = [b for b in brugere if b["afdeling"] == "" and b["status"] == "Aktiv"]
fil_fund = mappe / "mangler_afdeling.csv"
with open(fil_fund, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["logon", "navn", "afdeling", "status"])
    writer.writeheader()
    for b in fund:
        writer.writerow(b)
print("    fund        :", len(fund))
print("    gemt        :", fil_fund)
# 9a. Passer antallet med Sprint 1, Trin 6?
#     Svar: Ja. Det er den samme regel, bare regnet i Python i stedet for i et LDAP-filter.
# 9b. Hvem ville du sende denne fil til i en virksomhed, og hvad skal de gøre med den?
#     Svar: Fx HR eller lederne, som skal udfylde afdeling eller bekræfte, at kontoen
#           stadig skal bruges. En fundliste er en arbejdsopgave, ikke kun en oversigt.

# ------------------------------------------------------------
# Trin 10 · BONUS · Når en værdi selv indeholder et komma
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · Komma i en værdi")
test = mappe / "komma_test.csv"
with open(test, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["logon", "navn"])
    writer.writeheader()
    writer.writerow({"logon": "test01", "navn": "Hansen, Anne"})
print(test.read_text(encoding="utf-8-sig"))
with open(test, encoding="utf-8-sig") as f:
    for linje in f:
        print("    split(',')  :", linje.strip().split(","))
# TODO: læs komma_test.csv igen med csv.DictReader, og skriv hver række ud
with open(test, newline="", encoding="utf-8-sig") as f:
    for r in csv.DictReader(f):
        print("    DictReader  :", r)
# 10a. Hvad har DictWriter gjort ved "Hansen, Anne" i filen?
#      Svar: Sat anførselstegn om værdien: "Hansen, Anne". Så ved læseren, at kommaet
#            er en del af værdien og ikke et skilletegn.
# 10b. Hvor mange felter giver split(",") for datalinjen, og hvor mange giver DictReader?
#      Svar: split giver 3 felter og ødelægger navnet. DictReader giver 2 felter og læser
#            navnet korrekt. Brug altid csv-modulet til CSV, aldrig split.

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
