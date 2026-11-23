# ============================================================
#  MODUL 10 · Sprint 3 · Øvelse 3 · Active Directory (kun læsning)
#  Repeterer: Modul 6 (ADUC), Modul 7 (forbind, søg, filtre)
#             og Modul 9 (flag og audit)
# ============================================================
#  Før vi opretter brugerne fra nye_brugere.csv, skal vi kunne spørge AD:
#  findes logon allerede? Hvordan ser de eksisterende konti ud?
#  Værktøjet ligger færdigt i ad_vaerktoej.py. Hav filen åben ved siden af.
#  Scriptet LÆSER kun fra AD. Det skriver aldrig noget.
#
#  Kræver config_ad.json i samme mappe (som i Modul 7-9).
#  Du skal IKKE ændre i modulerne. Alt, du skriver, skriver du i denne fil.
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
#
#  Trin 1-5 er kernen. Trin 6-10 er BONUS, hvis du har tid tilbage.
# ============================================================
from tekst_vaerktoej import overskrift, ad_dato
from csv_vaerktoej import mappe, indlaes_csv, gem_json, valider_raekke, Bruger
from ad_vaerktoej import forbind, mit_logon, soeg, findes_i_ad, har_flag, gruppe_medlemmer

domaene = "DC=CSIK_DC_1,DC=local"
testdata = "OU=Testdata,DC=CSIK_DC_1,DC=local"

# ------------------------------------------------------------
# Trin 1 · Forbind til AD (Modul 7)
# ------------------------------------------------------------
overskrift("Trin 1 · Forbind")
conn = forbind()
print("    forbundet    :", conn.bound)
# TODO: skriv det logonnavn ud, du er logget ind med (brug en funktion fra ad_vaerktoej)
# 1a. Find forbind() i ad_vaerktoej.py. Hvor kommer server, bruger og adgangskode fra?
# 1b. Hvorfor står adgangskoden i en fil og ikke i koden? Hvorfor må config_ad.json ikke på GitHub?
# 1c. Hvad gør forbind(), hvis adgangskoden er forkert? Prøv evt. med en kopi af filen.

# ------------------------------------------------------------
# Trin 2 · Søg efter brugere (Modul 7)
# ------------------------------------------------------------
overskrift("Trin 2 · Brugere i OU=Testdata")
entries = soeg(conn, testdata, "(objectClass=user)", ["sAMAccountName", "department"])
print("    antal        :", len(entries))
# TODO: skriv sAMAccountName og department ud for hver bruger
# 2a. soeg søger med SUBTREE. Hvad betyder det, og hvad ville BASE og LEVEL give? (Modul 7)
# 2b. Åbn ADUC (Modul 6) og find OU=Testdata. Passer antallet med det, scriptet finder?
# 2c. Hvad skrives der for en bruger uden department? Hvorfor ikke en fejl?

# ------------------------------------------------------------
# Trin 3 · Filtre (Modul 7)
# ------------------------------------------------------------
overskrift("Trin 3 · Filtre")
it_filter = "???"         # TODO: filter der finder brugere i afdelingen IT
it_eller_hr = "???"       # TODO: filter der finder brugere i IT ELLER HR
if it_filter == "???" or it_eller_hr == "???":
    print("    Udfyld filtrene i Trin 3.")
    exit()
print("    IT           :", len(soeg(conn, testdata, it_filter, ["sAMAccountName"])))
print("    IT eller HR  :", len(soeg(conn, testdata, it_eller_hr, ["sAMAccountName"])))
# 3a. Hvilke filtre skrev du? Hvad betyder & og | foran parenteserne?
# 3b. Hvorfor er (objectClass=user) med i filteret?
# 3c. Er antallet for "IT eller HR" lig IT plus HR? Hvorfor eller hvorfor ikke?

# ------------------------------------------------------------
# Trin 4 · Findes logon allerede?
# ------------------------------------------------------------
overskrift("Trin 4 · Findes logon i AD?")
for logon in ["ahansen", "administrator", mit_logon(conn)]:
    print(f"    {logon:<22} {findes_i_ad(conn, domaene, logon)}")
raekker = indlaes_csv(mappe / "nye_brugere.csv")
# TODO: lav et Bruger-objekt for hver gyldig række i raekker (afdelinger IT, HR, Salg, Support),
#       og skriv logon ud med "[FINDES]" eller "[LEDIG]" foran
# 4a. Hvorfor søger findes_i_ad i hele domænet og ikke kun i OU=Testdata?
# 4b. "administrator" findes, selvom kontoen hedder "Administrator". Hvad siger det om LDAP-filtre?
# 4c. Hvilke moduler har du brugt i dette trin? Hvad kommer fra hvilket?

# ------------------------------------------------------------
# Trin 5 · Flag i userAccountControl (Modul 9)
# ------------------------------------------------------------
overskrift("Trin 5 · Deaktiverede konti og kodeord, der aldrig udløber")
entries = soeg(conn, testdata, "(objectClass=user)", ["sAMAccountName", "userAccountControl"])
deaktiverede = 0
udloeber_aldrig = 0
for e in entries:
    uac = e.userAccountControl.value
    if har_flag(uac, 2):
        deaktiverede += 1
    # TODO: tæl udloeber_aldrig op, når flaget 65536 er sat
print("    deaktiverede     :", deaktiverede)
print("    udløber aldrig   :", udloeber_aldrig)
# 5a. Find har_flag i ad_vaerktoej.py. Hvad gør &, og hvorfor står der != 0?
# 5b. Regn selv i Python-konsollen: er konto 66050 deaktiveret? Udløber koden aldrig?
# 5c. Hvorfor er en aktiv konto, hvis kodeord aldrig udløber, et fund i en audit?


# ============================================================
#  BONUS · Trin 6-10
#  Gå kun videre, når Trin 1-5 er svaret.
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Medlemmer af en gruppe (Modul 7)
# ------------------------------------------------------------
overskrift("Trin 6 · BONUS · Medlemmer af GRP_IT")
medlemmer = gruppe_medlemmer(conn, testdata, "GRP_IT")
print("    antal        :", len(medlemmer))
# TODO: skriv hvert medlem ud på sin egen linje
# 6a. Find gruppe_medlemmer. Hvad står der i member, før funktionen laver det om?
# 6b. Hvad returnerer funktionen, hvis gruppen ikke findes? Prøv med "GRP_FindesIkke".

# ------------------------------------------------------------
# Trin 7 · BONUS · En bruger i detaljer (Modul 6 og 7)
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · Én bruger med flere attributter")
logon = "???"           # TODO: skriv sAMAccountName på en bruger fra Trin 2
if logon == "???":
    print("    Udfyld logon i Trin 7.")
    exit()
entries = soeg(conn, testdata, "(sAMAccountName=" + logon + ")",
               ["displayName", "department", "title", "whenCreated", "userAccountControl"])
for e in entries:
    print("    displayName  :", e.displayName.value)
    print("    department   :", e.department.value)
    print("    title        :", e.title.value)
    print("    oprettet     :", ad_dato(e.whenCreated.value))
    print("    deaktiveret  :", har_flag(e.userAccountControl.value, 2))
# 7a. Find samme bruger i ADUC, og åbn Properties. På hvilke faner står department og title?
# 7b. ad_dato kommer fra Sprint 1. Hvad får den her: tekst eller datetime?

# ------------------------------------------------------------
# Trin 8 · BONUS · Gruppestatistik (Modul 7 og 9)
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · Medlemmer pr. gruppe")
grupper = soeg(conn, testdata, "(objectClass=group)", ["cn", "member"])
statistik = {}
# TODO: gem antal medlemmer for hver gruppe i statistik (gruppens cn som nøgle)
for navn in sorted(statistik, key=lambda n: statistik[n], reverse=True):
    print(f"    {navn:<28} {statistik[navn]}")
# 8a. Hvilken gruppe har flest medlemmer? Er der tomme grupper?
# 8b. Hvorfor bruger vi g.member.values og ikke g.member.value?

# ------------------------------------------------------------
# Trin 9 · BONUS · Findes afdelingernes grupper?
# ------------------------------------------------------------
overskrift("Trin 9 · BONUS · En gruppe pr. afdeling?")
for afd in ["IT", "HR", "Salg", "Support"]:
    gruppe = "GRP_" + afd
    # TODO: skriv "[FINDES]" eller "[MANGLER]" og gruppens navn ud
# 9a. Hvilke afdelinger mangler en gruppe? Hvad betyder det for nye brugere i Sprint 4?
# 9b. Kunne findes_i_ad bruges her? Hvorfor ikke?

# ------------------------------------------------------------
# Trin 10 · BONUS · Mini-audit som JSON (Modul 9)
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · audit.json")
audit = {"deaktiverede": deaktiverede, "udloeber_aldrig": udloeber_aldrig}
# TODO: tilføj "uden_afdeling" (antal brugere i Testdata uden department) til audit,
#       og gem audit i mappe / "audit.json" med gem_json
print("    audit        :", audit)
# 10a. Hvordan fandt du brugerne uden department?
# 10b. Kør scriptet igen i næste uge og gem en ny fil. Hvordan kunne du se, hvad der har ændret sig?

conn.unbind()
