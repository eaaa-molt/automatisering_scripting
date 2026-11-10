# ============================================================
#  LØSNINGSFORSLAG · MODUL 8 · Sprint 2 · Øvelse 2 · Ændr attributter
# ============================================================
#  conn.modify(dn, {"attribut": [(OPERATION, [værdier])]}) ændrer et objekt.
#    MODIFY_REPLACE  erstat værdien (eller sæt den, hvis den mangler)
#    MODIFY_ADD      tilføj en værdi
#    MODIFY_DELETE   fjern en bestemt værdi ([] = alle værdier)
#  Kræver at ex1_opret.py er kørt, så dine to testbrugere findes.
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
# ============================================================
from ldap3 import SUBTREE, MODIFY_REPLACE, MODIFY_ADD, MODIFY_DELETE
from ad_hjaelp import forbind, overskrift, vis_resultat, vis_bruger

conn = forbind()

# ------------------------------------------------------------
# Trin 1 · Dine testbrugere fra ex1. Findes de?
# ------------------------------------------------------------
ou = "OU=Modul8,OU=Testdata,DC=CSIK_DC_1,DC=local"
logon = conn.user.split("\\")[-1]
navn = ("test." + logon)[:20]
dn = "CN=" + navn + "," + ou
navn2 = ("test2." + logon)[:20]
dn2 = "CN=" + navn2 + "," + ou

conn.search(ou, "(sAMAccountName=" + navn + ")", SUBTREE)
if len(conn.entries) == 0:
    overskrift("Trin 1 · Stop")
    print("    " + navn + " findes ikke. Kør ex1_opret.py først.")
    exit()

overskrift("Trin 1 · " + navn + " før ændringerne")
vis_bruger(conn, dn)
# 1a. Hvilke attributter står med '-'? Hvad betyder det?

# ------------------------------------------------------------
# Trin 2 · MODIFY_REPLACE: sæt afdelingen
# ------------------------------------------------------------
overskrift("Trin 2 · MODIFY_REPLACE på department")
conn.modify(dn, {"department": [(MODIFY_REPLACE, ["IT"])]})
vis_resultat(conn)
vis_bruger(conn, dn)
# 2a. department havde ingen værdi før. Virkede REPLACE alligevel?
# 2b. Åbn brugeren i ADUC, fanen Organization. Hvor står IT?

# ------------------------------------------------------------
# Trin 3 · MODIFY_REPLACE: sæt en titel
# ------------------------------------------------------------
titel = "Konsulent"

if titel == "???":
    overskrift("Trin 3 · Stop")
    print("    Udfyld titel i Trin 3. Intet er ændret.")
    exit()

overskrift("Trin 3 · MODIFY_REPLACE på title")
conn.modify(dn, {"title": [(MODIFY_REPLACE, [titel])]})
vis_resultat(conn)
# 3a. Skift titel til noget andet og kør igen. Hvad sker der med den gamle titel?

# ------------------------------------------------------------
# Trin 4 · MODIFY_ADD: tilføj en beskrivelse
# ------------------------------------------------------------
overskrift("Trin 4 · MODIFY_ADD på description")
conn.modify(dn, {"description": [(MODIFY_ADD, ["Oprettet i Modul 8"])]})
vis_resultat(conn)
# 4a. Første gang giver det 0. Hvad giver det, når du kører scriptet igen? Hvorfor?
# 4b. Hvorfor fejler Trin 2 og 3 ikke på samme måde, når du kører igen?

# ------------------------------------------------------------
# Trin 5 · Skriv selv: sæt et telefonnummer med MODIFY_REPLACE
# ------------------------------------------------------------
telefon = "+45 12 34 56 78"

if telefon == "???":
    overskrift("Trin 5 · Stop")
    print("    Udfyld telefon i Trin 5. Intet er ændret.")
    exit()

overskrift("Trin 5 · MODIFY_REPLACE på telephoneNumber")
conn.modify(dn, {"telephoneNumber": [(MODIFY_REPLACE, [telefon])]})
vis_resultat(conn)
# 5a. Find nummeret i ADUC. Hvilken fane står det på?

# ------------------------------------------------------------
# Trin 6 · Skriv selv: ændr to attributter i ét kald
# ------------------------------------------------------------
kontor = "Aarhus"
firma = "CSIK Test A/S"

if kontor == "???" or firma == "???":
    overskrift("Trin 6 · Stop")
    print("    Udfyld kontor og firma i Trin 6. Intet er ændret.")
    exit()

overskrift("Trin 6 · To attributter i ét conn.modify()")
conn.modify(dn, {"physicalDeliveryOfficeName": [(MODIFY_REPLACE, [kontor])],
                 "company": [(MODIFY_REPLACE, [firma])]})
vis_resultat(conn)
# 6a. Hvor mange result-linjer fik du for to ændringer? Hvad betyder det,
#     hvis en af de to ændringer fejler?
# 6b. Find kontor og firma i ADUC. Hvilke felter er det?

# ------------------------------------------------------------
# Trin 7 · Fejl med vilje: fjern en værdi, der ikke findes
# ------------------------------------------------------------
overskrift("Trin 7 · MODIFY_DELETE på en værdi, der ikke findes")
conn.modify(dn, {"description": [(MODIFY_DELETE, ["Denne tekst findes ikke"])]})
vis_resultat(conn)
# 7a. Hvilken result-kode og description giver AD?
# 7b. Hvad er forskellen på MODIFY_DELETE med en værdi og MODIFY_DELETE med []?

# ------------------------------------------------------------
# Trin 8 · MODIFY_DELETE: fjern titlen igen
# ------------------------------------------------------------
overskrift("Trin 8 · MODIFY_DELETE på title")
conn.modify(dn, {"title": [(MODIFY_DELETE, [])]})
vis_resultat(conn)
vis_bruger(conn, dn)
# 8a. Kør scriptet igen. Trin 3 sætter titlen, og Trin 8 fjerner den. Hvad står der til sidst?
# 8b. Byt Trin 8 om, så den fjerner description i stedet. Hvad sker der så med Trin 4 næste gang?

# ------------------------------------------------------------
# Trin 9 · Skriv selv: giv bruger nummer to en afdeling og en titel
# ------------------------------------------------------------
overskrift("Trin 9 · Ret " + navn2)
conn.modify(dn2, {"department": [(MODIFY_REPLACE, ["HR"])],
                  "title": [(MODIFY_REPLACE, ["Rekrutterer"])]})
vis_resultat(conn)
vis_bruger(conn, dn2)
# 9a. Hvad svarer AD, hvis navn2 ikke findes (fx hvis Trin 8 i ex1 ikke er lavet)?

# ------------------------------------------------------------
# Trin 10 · Find alle IT-brugere i OU=Modul8 med et AND-filter (repetition fra Modul 7)
# ------------------------------------------------------------
filter_and = "(&(objectClass=user)(department=IT))"

if filter_and == "???":
    overskrift("Trin 10 · Stop")
    print("    Udfyld filter_and i Trin 10.")
    exit()

overskrift("Trin 10 · Brugere med department=IT")
conn.search(ou, filter_and, SUBTREE, attributes=["sAMAccountName", "department", "title"])
print("    antal       :", len(conn.entries))
for e in conn.entries:
    print("   ", e.sAMAccountName, "·", e.department, "·", e.title)
# 10a. Er navn2 med? Hvorfor ikke?
# 10b. Skift filteret, så det finder brugere med department=HR. Hvem finder du nu?

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
