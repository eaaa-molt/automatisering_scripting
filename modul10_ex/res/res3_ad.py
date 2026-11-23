# ============================================================
#  MODUL 10 · Sprint 3 · Løsning 3 · Active Directory (kun læsning)
#  Repeterer: Modul 6 (ADUC), Modul 7 (forbind, søg, filtre)
#             og Modul 9 (flag og audit)
# ============================================================
#  Løsningsforslag. Hver opgave (TODO) og hvert spørgsmål står som i
#  øvelsen, med løsningen eller svaret lige under.
#  Tal i svarene afhænger af, hvad der ligger i AD på dagen.
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
print("    logget ind   :", mit_logon(conn))
# 1a. Find forbind() i ad_vaerktoej.py. Hvor kommer server, bruger og adgangskode fra?
#     Svar: Fra config_ad.json i samme mappe som modulet. Filen læses med json (Modul 4).
# 1b. Hvorfor står adgangskoden i en fil og ikke i koden? Hvorfor må config_ad.json ikke på GitHub?
#     Svar: Så koden kan deles uden hemmeligheder, og hver person bruger sin egen konto.
#           Kommer filen på GitHub, kan alle læse adgangskoden. Derfor står den i .gitignore.
# 1c. Hvad gør forbind(), hvis adgangskoden er forkert? Prøv evt. med en kopi af filen.
#     Svar: auto_bind fejler, except fanger fejlen, skriver "Forbindelsesfejl" og stopper
#           med SystemExit. Scriptet går altså ikke videre uden forbindelse.

# ------------------------------------------------------------
# Trin 2 · Søg efter brugere (Modul 7)
# ------------------------------------------------------------
overskrift("Trin 2 · Brugere i OU=Testdata")
entries = soeg(conn, testdata, "(objectClass=user)", ["sAMAccountName", "department"])
print("    antal        :", len(entries))
# TODO: skriv sAMAccountName og department ud for hver bruger
for e in entries:
    print(f"    {e.sAMAccountName.value:<22} {e.department.value}")
# 2a. soeg søger med SUBTREE. Hvad betyder det, og hvad ville BASE og LEVEL give? (Modul 7)
#     Svar: SUBTREE søger i base og alle OU'er under den. BASE ser kun på selve base-objektet,
#           LEVEL kun på det, der ligger direkte under base.
# 2b. Åbn ADUC (Modul 6) og find OU=Testdata. Passer antallet med det, scriptet finder?
#     Svar: Det bør passe, når man tæller brugere i alle under-OU'er. ADUC viser kun én OU
#           ad gangen, mens SUBTREE tager dem alle.
# 2c. Hvad skrives der for en bruger uden department? Hvorfor ikke en fejl?
#     Svar: None. Attributten findes ikke på brugeren, og ldap3 giver .value = None.

# ------------------------------------------------------------
# Trin 3 · Filtre (Modul 7)
# ------------------------------------------------------------
overskrift("Trin 3 · Filtre")
# TODO: filter der finder brugere i afdelingen IT
it_filter = "(&(objectClass=user)(department=IT))"
# TODO: filter der finder brugere i IT ELLER HR
it_eller_hr = "(&(objectClass=user)(|(department=IT)(department=HR)))"
print("    IT           :", len(soeg(conn, testdata, it_filter, ["sAMAccountName"])))
print("    IT eller HR  :", len(soeg(conn, testdata, it_eller_hr, ["sAMAccountName"])))
# 3a. Hvilke filtre skrev du? Hvad betyder & og | foran parenteserne?
#     Svar: & betyder at alle betingelser skal passe (AND), | at mindst én skal (OR).
# 3b. Hvorfor er (objectClass=user) med i filteret?
#     Svar: Ellers kan andre objekter med department (fx kontakter) også komme med.
#           Computerkonti har også objectClass=user, så man kan tilføje (objectCategory=person).
# 3c. Er antallet for "IT eller HR" lig IT plus HR? Hvorfor eller hvorfor ikke?
#     Svar: Ja, fordi en bruger kun har én department. Havde vi talt grupper, kunne en
#           bruger tælle med to gange.

# ------------------------------------------------------------
# Trin 4 · Findes logon allerede?
# ------------------------------------------------------------
overskrift("Trin 4 · Findes logon i AD?")
for logon in ["ahansen", "administrator", mit_logon(conn)]:
    print(f"    {logon:<22} {findes_i_ad(conn, domaene, logon)}")
raekker = indlaes_csv(mappe / "nye_brugere.csv")
# TODO: lav et Bruger-objekt for hver gyldig række i raekker (afdelinger IT, HR, Salg, Support),
#       og skriv logon ud med "[FINDES]" eller "[LEDIG]" foran
for r in raekker:
    if len(valider_raekke(r, ["IT", "HR", "Salg", "Support"])) == 0:
        b = Bruger(r["fornavn"], r["efternavn"], r["afdeling"], r["titel"])
        if findes_i_ad(conn, domaene, b.logon):
            print(f"    [FINDES] {b.logon}")
        else:
            print(f"    [LEDIG]  {b.logon}")
# 4a. Hvorfor søger findes_i_ad i hele domænet og ikke kun i OU=Testdata?
#     Svar: sAMAccountName skal være unik i hele domænet. En konto i en anden OU blokerer
#           også for logon.
# 4b. "administrator" findes, selvom kontoen hedder "Administrator". Hvad siger det om LDAP-filtre?
#     Svar: Sammenligningen i AD skelner ikke mellem store og små bogstaver for sAMAccountName.
# 4c. Hvilke moduler har du brugt i dette trin? Hvad kommer fra hvilket?
#     Svar: csv_vaerktoej (indlaes_csv, valider_raekke, Bruger), tekst_vaerktoej (lav_logon,
#           inde i Bruger) og ad_vaerktoej (findes_i_ad). Det er netop sådan, Sprint 4 arbejder.

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
    if har_flag(uac, 65536):
        udloeber_aldrig += 1
print("    deaktiverede     :", deaktiverede)
print("    udløber aldrig   :", udloeber_aldrig)
# 5a. Find har_flag i ad_vaerktoej.py. Hvad gør &, og hvorfor står der != 0?
#     Svar: & sammenligner bit for bit og giver et tal, hvor kun de fælles bits er sat.
#           Er flaget sat, giver det flagets værdi, ellers 0. != 0 gør det til True/False.
# 5b. Regn selv i Python-konsollen: er konto 66050 deaktiveret? Udløber koden aldrig?
#     Svar: 66050 = 65536 + 512 + 2. 66050 & 2 = 2 (deaktiveret), 66050 & 65536 = 65536
#           (udløber aldrig). Begge er sat.
# 5c. Hvorfor er en aktiv konto, hvis kodeord aldrig udløber, et fund i en audit?
#     Svar: Koden kan være gammel og lækket uden at blive skiftet. Den bør kun findes på
#           servicekonti med lange, stærke koder.


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
for navn in medlemmer:
    print("   ", navn)
# 6a. Find gruppe_medlemmer. Hvad står der i member, før funktionen laver det om?
#     Svar: Fulde DN'er, fx CN=Lars Jensen,OU=Brugere,OU=Testdata,DC=... Funktionen tager
#           den første del og fjerner "CN=".
# 6b. Hvad returnerer funktionen, hvis gruppen ikke findes? Prøv med "GRP_FindesIkke".
#     Svar: En tom liste. Den tjekker len(conn.entries) == 0 før conn.entries[0], så der
#           ikke kommer IndexError.

# ------------------------------------------------------------
# Trin 7 · BONUS · En bruger i detaljer (Modul 6 og 7)
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · Én bruger med flere attributter")
# TODO: skriv sAMAccountName på en bruger fra Trin 2
logon = entries[0].sAMAccountName.value
entries = soeg(conn, testdata, "(sAMAccountName=" + logon + ")",
               ["displayName", "department", "title", "whenCreated", "userAccountControl"])
for e in entries:
    print("    displayName  :", e.displayName.value)
    print("    department   :", e.department.value)
    print("    title        :", e.title.value)
    print("    oprettet     :", ad_dato(e.whenCreated.value))
    print("    deaktiveret  :", har_flag(e.userAccountControl.value, 2))
# 7a. Find samme bruger i ADUC, og åbn Properties. På hvilke faner står department og title?
#     Svar: Under fanen Organization (Department og Job Title). whenCreated ses på fanen
#           Object, eller i Attribute Editor med Advanced Features slået til.
# 7b. ad_dato kommer fra Sprint 1. Hvad får den her: tekst eller datetime?
#     Svar: ldap3 giver whenCreated som datetime, så ad_dato springer strptime over og
#           bruger strftime direkte. Derfor kan funktionen begge dele.

# ------------------------------------------------------------
# Trin 8 · BONUS · Gruppestatistik (Modul 7 og 9)
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · Medlemmer pr. gruppe")
grupper = soeg(conn, testdata, "(objectClass=group)", ["cn", "member"])
statistik = {}
# TODO: gem antal medlemmer for hver gruppe i statistik (gruppens cn som nøgle)
for g in grupper:
    statistik[g.cn.value] = len(g.member.values)
for navn in sorted(statistik, key=lambda n: statistik[n], reverse=True):
    print(f"    {navn:<28} {statistik[navn]}")
# 8a. Hvilken gruppe har flest medlemmer? Er der tomme grupper?
#     Svar: Afhænger af AD. Tomme grupper er ofte rester, der bør ryddes op.
# 8b. Hvorfor bruger vi g.member.values og ikke g.member.value?
#     Svar: member har mange værdier. .values giver altid en liste (også tom), mens .value
#           giver en enkelt værdi, en liste eller None afhængigt af antallet.

# ------------------------------------------------------------
# Trin 9 · BONUS · Findes afdelingernes grupper?
# ------------------------------------------------------------
overskrift("Trin 9 · BONUS · En gruppe pr. afdeling?")
for afd in ["IT", "HR", "Salg", "Support"]:
    gruppe = "GRP_" + afd
    # TODO: skriv "[FINDES]" eller "[MANGLER]" og gruppens navn ud
    if len(soeg(conn, testdata, "(&(objectClass=group)(cn=" + gruppe + "))", ["cn"])) > 0:
        print(f"    [FINDES]  {gruppe}")
    else:
        print(f"    [MANGLER] {gruppe}")
# 9a. Hvilke afdelinger mangler en gruppe? Hvad betyder det for nye brugere i Sprint 4?
#     Svar: Afhænger af AD. Nye brugere i en afdeling uden gruppe kan ikke meldes ind
#           automatisk. Gruppen skal oprettes først, eller afdelingen springes over.
# 9b. Kunne findes_i_ad bruges her? Hvorfor ikke?
#     Svar: Nej. findes_i_ad søger på sAMAccountName. Grupper har også sAMAccountName, men
#           det behøver ikke være lig cn. Her søger vi derfor på cn og objectClass=group.

# ------------------------------------------------------------
# Trin 10 · BONUS · Mini-audit som JSON (Modul 9)
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · audit.json")
audit = {"deaktiverede": deaktiverede, "udloeber_aldrig": udloeber_aldrig}
# TODO: tilføj "uden_afdeling" (antal brugere i Testdata uden department) til audit,
#       og gem audit i mappe / "audit.json" med gem_json
audit["uden_afdeling"] = len(soeg(conn, testdata, "(&(objectClass=user)(!(department=*)))", ["sAMAccountName"]))
gem_json(audit, mappe / "audit.json")
print("    audit        :", audit)
# 10a. Hvordan fandt du brugerne uden department?
#     Svar: Med filteret (!(department=*)). =* betyder "har en værdi", og ! vender det om.
# 10b. Kør scriptet igen i næste uge og gem en ny fil. Hvordan kunne du se, hvad der har ændret sig?
#     Svar: Gem med dato i filnavnet, indlæs begge med indlaes_json, og sammenlign tallene
#           (som diff med audit_forrige.json i Modul 9).

conn.unbind()
