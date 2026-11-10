# ============================================================
#  LØSNINGSFORSLAG · MODUL 8 · Sprint 1 · Øvelse 1 · Opret en bruger
# ============================================================
#  conn.add(dn, objectClass, attributter) opretter et nyt objekt i AD.
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
# ============================================================
from ldap3 import SUBTREE, BASE
from ad_hjaelp import forbind, overskrift, vis_resultat, vis_bruger

conn = forbind()

# ------------------------------------------------------------
# Trin 1 · Din testbruger hedder "test." + det logonnavn, du er logget ind med
# ------------------------------------------------------------
ou = "OU=Modul8,OU=Testdata,DC=CSIK_DC_1,DC=local"
logon = conn.user.split("\\")[-1]          # "CSIK_DC_1\\stud01" bliver til "stud01"
navn = ("test." + logon)[:20]              # sAMAccountName må højst være 20 tegn
dn = "CN=" + navn + "," + ou
overskrift("Trin 1 · Din testbruger")
print("    dn          :", dn)
# 1a. Hvilke tre dele består DN'et af? Hvad betyder CN, OU og DC?

# ------------------------------------------------------------
# Trin 2 · Hvem er testbrugeren? Udfyld alle tre linjer
# ------------------------------------------------------------
fornavn = "Test"
efternavn = "Bruger"
visningsnavn = fornavn + " " + efternavn

if fornavn == "???" or efternavn == "???" or visningsnavn == "???":
    overskrift("Trin 2 · Stop")
    print("    Udfyld fornavn, efternavn og visningsnavn i Trin 2. Intet er oprettet.")
    exit()

# ------------------------------------------------------------
# Trin 3 · Findes brugeren allerede? (samme søgning som i Modul 7)
# ------------------------------------------------------------
overskrift("Trin 3 · Findes " + navn + " allerede?")
conn.search(ou, "(sAMAccountName=" + navn + ")", SUBTREE)
print("    fundet      :", len(conn.entries))

# ------------------------------------------------------------
# Trin 4 · Opret brugeren
# ------------------------------------------------------------
overskrift("Trin 4 · Opret " + navn + " med conn.add()")
conn.add(dn,
         ["top", "person", "organizationalPerson", "user"],   # objectClass
         {"sAMAccountName": navn,                              # logonnavn (gammel stil)
          "userPrincipalName": navn + "@CSIK_DC_1.local",      # logonnavn (ny stil)
          "givenName": fornavn,
          "sn": efternavn,
          "displayName": visningsnavn,
          "userAccountControl": 514})                          # 512 + 2 = deaktiveret
vis_resultat(conn)
# 4a. Hvad betyder result 0?
# 4b. Kør scriptet igen. Hvad viser Trin 3 nu, og hvad svarer AD i Trin 4? Hvorfor?
# 4c. Hvorfor oprettes brugeren med 514 og ikke 512? Hvad ville AD sige til 512?

# ------------------------------------------------------------
# Trin 5 · Se brugeren i AD
# ------------------------------------------------------------
overskrift("Trin 5 · Sådan ser brugeren ud i AD")
vis_bruger(conn, dn)
# 5a. Find brugeren i ADUC under OU=Modul8 (F5). Hvorfor har ikonet en pil?
# 5b. Hvilket navn står i kolonnen Name, og hvilket i Display Name? Hvor kommer de fra i koden?
# 5c. Hvad er forskellen på sAMAccountName og userPrincipalName, når man logger ind?

# ------------------------------------------------------------
# Trin 6 · Hvem har ellers oprettet brugere? (repetition fra Modul 7)
# ------------------------------------------------------------
overskrift("Trin 6 · Alle brugere i OU=Modul8")
conn.search(ou, "(objectClass=user)", SUBTREE, attributes=["sAMAccountName", "displayName"])
print("    antal       :", len(conn.entries))
for e in conn.entries:
    print("   ", e.sAMAccountName, "·", e.displayName)
# 6a. Hvor mange testbrugere er der? Kan du se, hvem der har lavet dem?
# 6b. Kør Trin 6 igen om fem minutter. Er der kommet flere?

# ------------------------------------------------------------
# Trin 7 · Hvad satte AD selv?
# ------------------------------------------------------------
overskrift("Trin 7 · Alle attributter på " + navn)
conn.search(dn, "(objectClass=*)", BASE, attributes=["*"])
print(conn.entries[0])
# 7a. Find tre attributter, som du IKKE selv har sat i Trin 4. Hvem har sat dem?
# 7b. Hvad er whenCreated? Passer klokkeslættet med dit ur? (Tip: tidszone)
# 7c. primaryGroupID er 513. Hvilken gruppe er det? (Tip: søg på nettet efter "RID 513")
# 7d. Hvad er forskellen på objectGUID og objectSid?

# ------------------------------------------------------------
# Trin 8 · Opret en bruger mere, helt selv
# ------------------------------------------------------------
navn2 = ("test2." + logon)[:20]
dn2 = "CN=" + navn2 + "," + ou

if navn2 == "???" or dn2 == "???":
    overskrift("Trin 8 · Stop")
    print("    Udfyld navn2 og dn2 i Trin 8. Intet er oprettet.")
    exit()

overskrift("Trin 8 · Opret " + navn2)
conn.add(dn2,
         ["top", "person", "organizationalPerson", "user"],
         {"sAMAccountName": navn2,
          "userPrincipalName": navn2 + "@CSIK_DC_1.local",
          "givenName": "Anden",
          "sn": "Testbruger",
          "displayName": "Anden Testbruger",
          "department": "IT",
          "userAccountControl": 514})
vis_resultat(conn)
vis_bruger(conn, dn2)
# 8a. Hvilke linjer kunne du kopiere fra Trin 4, og hvilke skulle du ændre?
# 8b. department er sat her, men ikke i Trin 4. Kan man sætte alle attributter ved oprettelsen?

# ------------------------------------------------------------
# Trin 9 · Fejl med vilje: opret i en OU, der ikke findes
# ------------------------------------------------------------
forkert_dn = "CN=" + navn + ",OU=FindesIkke,OU=Testdata,DC=CSIK_DC_1,DC=local"

if forkert_dn == "???":
    overskrift("Trin 9 · Stop")
    print("    Udfyld forkert_dn i Trin 9.")
    exit()

overskrift("Trin 9 · Opret i en OU, der ikke findes")
conn.add(forkert_dn, ["top", "person", "organizationalPerson", "user"], {"sAMAccountName": navn})
vis_resultat(conn)
# 9a. Hvilken result-kode og description giver AD?
# 9b. Hvorfor er det IKKE 68 (entryAlreadyExists), selvom navn allerede findes i AD?
#     (Tip: kig på message. Hvad bliver tjekket først?)

# ------------------------------------------------------------
# Trin 10 · Find dine to brugere med ét OR-filter (repetition fra Modul 7)
# ------------------------------------------------------------
overskrift("Trin 10 · Dine to testbrugere")
filter_or = "(|(sAMAccountName=" + navn + ")(sAMAccountName=" + navn2 + "))"

if filter_or == "???":
    print("    Udfyld filter_or i Trin 10.")
    exit()

conn.search(ou, filter_or, SUBTREE, attributes=["sAMAccountName", "displayName", "department"])
for e in conn.entries:
    print("   ", e.sAMAccountName, "·", e.displayName, "·", e.department)
# 10a. Hvad viser department for den første bruger? Hvorfor?
# 10b. Skriv filteret om til et AND-filter. Hvor mange brugere finder du så? Hvorfor?

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
