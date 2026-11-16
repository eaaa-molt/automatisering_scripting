# ============================================================
#  MODUL 9 · Sprint 2 · Øvelse 2 · CSV-rapport
# ============================================================
#  En audit er først nyttig, når andre kan læse den. CSV er det format,
#  som Excel, Numbers og LibreOffice åbner direkte.
#  Scriptet LÆSER kun fra AD. Det skriver kun filer i din egen mappe.
#
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
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
# 1b. Hvorfor er conn.entries ikke klar til at blive skrevet direkte til en CSV-fil?

# ------------------------------------------------------------
# Trin 2 · Lav én dict pr. bruger
# ------------------------------------------------------------
overskrift("Trin 2 · Brugerne som en liste af dicts")
brugere = []
for e in conn.entries:
    afdeling = e.department.value
    if afdeling is None:                   # brugeren har ingen afdeling
        afdeling = ""
    status = "???"                         # TODO: "Deaktiveret" hvis flaget 2 er sat, ellers "Aktiv" (se Sprint 1)
    if status == "???":
        print("    Udfyld status i Trin 2.")
        exit()
    brugere.append({"logon": e.sAMAccountName.value,
                    "navn": e.cn.value,
                    "afdeling": afdeling,
                    "status": status})
print("    antal dicts :", len(brugere))
print("    første      :", brugere[0])
# 2a. Hvad ville der stå i afdeling, hvis vi fjernede if-sætningen? Hvorfor er det dårligt i en CSV?
# 2b. Hvorfor gemmer vi "Aktiv"/"Deaktiveret" i stedet for selve tallet 512/514?

# ------------------------------------------------------------
# Trin 3 · Skriv listen til brugere.csv
# ------------------------------------------------------------
overskrift("Trin 3 · Skriv brugere.csv")
fil = mappe / "brugere.csv"
with open(fil, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["logon", "navn", "afdeling", "status"])
    # TODO: skriv overskriftsrækken
    # TODO: skriv én række pr. dict i brugere med en for-løkke
print("    gemt        :", fil)
print("    størrelse   :", fil.stat().st_size, "bytes")
# 3a. Åbn brugere.csv i VS Code. Hvad står der i første linje? Hvor kommer det fra?
# 3b. Hvad sker der, hvis du glemmer writeheader()? Prøv det.
# 3c. Hvorfor bruger vi en DictWriter og ikke bare f.write() med kommaer imellem?

# ------------------------------------------------------------
# Trin 4 · Åbn filen i et regneark
# ------------------------------------------------------------
overskrift("Trin 4 · Åbn brugere.csv i Excel, Numbers eller LibreOffice")
print("    Find filen her:", fil)
# 4a. Vises æ, ø og å korrekt (fx i en afdeling som Økonomi eller i et navn)?
# 4b. Står alle værdier i én kolonne, eller er de fordelt i fire kolonner?
# 4c. Skift "utf-8-sig" til "utf-8" i Trin 3, kør igen og åbn filen i Excel. Hvad sker der?
# 4d. Hvor mange bytes blev filen større med utf-8-sig end med utf-8?

# ------------------------------------------------------------
# Trin 5 · Læs filen tilbage og tjek den
# ------------------------------------------------------------
overskrift("Trin 5 · Læs brugere.csv igen")
with open(fil, newline="", encoding="utf-8-sig") as f:
    raekker = list(csv.DictReader(f))
print("    rækker      :", len(raekker))
print("    første      :", raekker[0])
# TODO: tæl hvor mange rækker der har status "Deaktiveret", og skriv tallet ud
# TODO: skriv logon ud for hver deaktiveret bruger
# 5a. Er antallet af rækker det samme som i Trin 1? Hvorfor er det et godt tjek?
# 5b. Passer antallet af deaktiverede med Sprint 1, Trin 3?
# 5c. Hvilken datatype har r["status"]? Hvilken datatype ville et tal fra CSV-filen have?


# ============================================================
#  BONUS · Trin 6-10
#  Gå kun videre, når Trin 1-5 er svaret.
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Tilføj en kolonne med titel
# ------------------------------------------------------------
overskrift("Trin 6 · BONUS · Kolonnen titel")
# TODO: tilføj "titel" til hver dict i Trin 2 (samme mønster som afdeling)
# TODO: tilføj "titel" til fieldnames i Trin 3, og kør igen
print("    kolonner    :", list(brugere[0].keys()))
# 6a. Hvad sker der, hvis du tilføjer titel til dict'en, men glemmer den i fieldnames?
# 6b. Hvad sker der omvendt, hvis titel står i fieldnames, men mangler i en dict?

# ------------------------------------------------------------
# Trin 7 · BONUS · En version til dansk Excel
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · brugere_excel.csv med semikolon")
fil_excel = mappe / "brugere_excel.csv"
# TODO: skriv brugere til fil_excel som i Trin 3, men med semikolon som skilletegn
#       (Tip: DictWriter har en parameter, der hedder delimiter)
# TODO: brug de danske kolonnenavne "Logonnavn", "Navn", "Afdeling" og "Status" i overskriften
#       (Tip: writeheader() skriver nøglerne. Prøv i stedet writer.writerow() med en dict)
print("    gemt        :", fil_excel)
# 7a. Åbn begge filer i Excel. Hvilken ser rigtig ud nu?
# 7b. Hvorfor er det et problem for en rapport, der skal deles på tværs af lande?

# ------------------------------------------------------------
# Trin 8 · BONUS · Sortér rapporten
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · Sorteret efter afdeling og logon")
sorteret = "???"                          # TODO: brugere sorteret efter afdeling, og inden for afdeling efter logon
#       (Tip: sorted() med key=lambda, og en tuple som nøgle)
if sorteret == "???":
    print("    Udfyld sorteret i Trin 8.")
    exit()
for b in sorteret:
    print(f"    {b['afdeling']:<15} {b['logon']:<22} {b['status']}")
# 8a. Hvor havner brugerne uden afdeling? Hvorfor?
# 8b. Hvordan ville du få de deaktiverede brugere øverst i stedet?

# ------------------------------------------------------------
# Trin 9 · BONUS · En rapport kun med fund
# ------------------------------------------------------------
overskrift("Trin 9 · BONUS · mangler_afdeling.csv")
fund = "???"                              # TODO: kun de AKTIVE brugere uden afdeling (list comprehension eller for-løkke)
if fund == "???":
    print("    Udfyld fund i Trin 9.")
    exit()
fil_fund = mappe / "mangler_afdeling.csv"
with open(fil_fund, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(f, fieldnames=["logon", "navn", "afdeling", "status"])
    writer.writeheader()
    for b in fund:
        writer.writerow(b)
print("    fund        :", len(fund))
print("    gemt        :", fil_fund)
# 9a. Passer antallet med Sprint 1, Trin 6?
# 9b. Hvem ville du sende denne fil til i en virksomhed, og hvad skal de gøre med den?

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
# 10a. Hvad har DictWriter gjort ved "Hansen, Anne" i filen?
# 10b. Hvor mange felter giver split(",") for datalinjen, og hvor mange giver DictReader?

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
