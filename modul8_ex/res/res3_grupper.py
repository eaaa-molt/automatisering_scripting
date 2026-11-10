# ============================================================
#  LØSNINGSFORSLAG · MODUL 8 · Sprint 3 · Øvelse 3 · Gruppemedlemskab
# ============================================================
#  Medlemmer står i attributten member på GRUPPEN.
#  Derfor er det gruppen, der ændres, ikke brugeren:
#    conn.modify(gruppe_dn, {"member": [(MODIFY_ADD, [bruger_dn])]})
#  AD opdaterer selv memberOf på brugeren.
#  Kræver at ex1_opret.py er kørt, så dine to testbrugere findes.
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
# ============================================================
from ldap3 import SUBTREE, BASE, MODIFY_ADD, MODIFY_DELETE
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
gruppe = "CN=GRP_IT,OU=Grupper,OU=Testdata,DC=CSIK_DC_1,DC=local"

conn.search(ou, "(sAMAccountName=" + navn + ")", SUBTREE)
if len(conn.entries) == 0:
    overskrift("Trin 1 · Stop")
    print("    " + navn + " findes ikke. Kør ex1_opret.py først.")
    exit()

overskrift("Trin 1 · " + navn + " før ændringerne")
vis_bruger(conn, dn)
# 1a. Hvad står der i memberOf nu? Hvorfor står Domain Users ikke der? (Tip: primaryGroupID i ex1)

# ------------------------------------------------------------
# Trin 2 · Skriv selv: hvem er medlem af GRP_IT? (repetition fra Modul 7)
# ------------------------------------------------------------
overskrift("Trin 2 · Medlemmer af GRP_IT før")
conn.search(gruppe, "(objectClass=group)", BASE, attributes=["member"])
print("    antal       :", len(conn.entries[0].member.values))
for m in conn.entries[0].member.values:
    print("   ", m)
# 2a. Hvor mange medlemmer har GRP_IT? Står de som logonnavn eller som DN?

# ------------------------------------------------------------
# Trin 3 · MODIFY_ADD: meld testbrugeren ind i GRP_IT
# ------------------------------------------------------------
overskrift("Trin 3 · MODIFY_ADD på gruppens member")
conn.modify(gruppe, {"member": [(MODIFY_ADD, [dn])]})
vis_resultat(conn)
vis_bruger(conn, dn)
# 3a. Vi ændrede gruppen, men memberOf på brugeren ændrede sig også. Hvem opdaterede den?
# 3b. Åbn GRP_IT i ADUC (fanen Members) og brugeren (fanen Member Of). Ser du det begge steder?
# 3c. Hvorfor bruger member brugerens DN og ikke bare navn?

# ------------------------------------------------------------
# Trin 4 · Fejl med vilje: skriv memberOf direkte på brugeren
# ------------------------------------------------------------
overskrift("Trin 4 · MODIFY_ADD på brugerens memberOf")
conn.modify(dn, {"memberOf": [(MODIFY_ADD, [gruppe])]})
vis_resultat(conn)
# 4a. Hvilken result-kode giver AD? Læs message.
# 4b. Hvorfor giver det mening, at memberOf kun kan læses og ikke skrives?

# ------------------------------------------------------------
# Trin 5 · Skriv selv: meld også bruger nummer to ind i GRP_IT
# ------------------------------------------------------------
overskrift("Trin 5 · Meld " + navn2 + " ind i GRP_IT")
conn.modify(gruppe, {"member": [(MODIFY_ADD, [dn2])]})
vis_resultat(conn)
vis_bruger(conn, dn2)
# 5a. Hvilken linje fra Trin 3 skulle du ændre?

# ------------------------------------------------------------
# Trin 6 · Opret din egen gruppe i OU=Modul8
# ------------------------------------------------------------
gruppe_navn = "GRP_" + logon

if gruppe_navn == "???":
    overskrift("Trin 6 · Stop")
    print("    Udfyld gruppe_navn i Trin 6. Intet er oprettet.")
    exit()

egen_gruppe = "CN=" + gruppe_navn + "," + ou
overskrift("Trin 6 · Opret " + gruppe_navn)
conn.add(egen_gruppe, ["top", "group"], {"sAMAccountName": gruppe_navn})
vis_resultat(conn)
# 6a. Sammenlign med conn.add for en bruger i ex1. Hvad er anderledes?
# 6b. Find gruppen i ADUC. Hvilken Group scope og Group type har den fået? Hvorfor?

# ------------------------------------------------------------
# Trin 7 · Skriv selv: meld begge testbrugere ind i din gruppe i ét kald
# ------------------------------------------------------------
overskrift("Trin 7 · Begge brugere ind i " + gruppe_navn)
conn.modify(egen_gruppe, {"member": [(MODIFY_ADD, [dn, dn2])]})
vis_resultat(conn)
vis_bruger(conn, dn)
# 7a. Hvordan kan listen [dn, dn2] tilføje to medlemmer på én gang?
# 7b. Kør scriptet igen. Hvad sker der, når det ene medlem allerede er der?

# ------------------------------------------------------------
# Trin 8 · Hvilke grupper er testbrugeren medlem af? (repetition fra Modul 7)
# ------------------------------------------------------------
filter_member = "(&(objectClass=group)(member=" + dn + "))"

if filter_member == "???":
    overskrift("Trin 8 · Stop")
    print("    Udfyld filter_member i Trin 8.")
    exit()

overskrift("Trin 8 · Grupper med " + navn + " som member")
conn.search("DC=CSIK_DC_1,DC=local", filter_member, SUBTREE, attributes=["cn"])
for e in conn.entries:
    print("   ", e.cn)
# 8a. Giver søgningen samme svar som memberOf i Trin 7? Hvad er fordelen ved hver metode?

# ------------------------------------------------------------
# Trin 9 · Skriv selv: meld begge testbrugere ud af GRP_IT igen
# ------------------------------------------------------------
overskrift("Trin 9 · MODIFY_DELETE på gruppens member")
conn.modify(gruppe, {"member": [(MODIFY_DELETE, [dn, dn2])]})
vis_resultat(conn)
vis_bruger(conn, dn)
# 9a. GRP_IT er en rigtig gruppe, som alle hold bruger. Hvorfor er det vigtigt at rydde op?
# 9b. Hvad ville der ske med GRP_IT, hvis Trin 9 manglede, og 30 studerende kørte scriptet?

# ------------------------------------------------------------
# Trin 10 · Medlemmer af GRP_IT efter
# ------------------------------------------------------------
overskrift("Trin 10 · Medlemmer af GRP_IT efter")
conn.search(gruppe, "(objectClass=group)", BASE, attributes=["member"])
print("    antal       :", len(conn.entries[0].member.values))
# 10a. Er antallet det samme som i Trin 2? Hvis ikke: hvem mangler at rydde op?

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
