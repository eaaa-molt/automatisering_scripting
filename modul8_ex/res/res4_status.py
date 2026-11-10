# ============================================================
#  LØSNINGSFORSLAG · MODUL 8 · Sprint 4 · Øvelse 4 · Aktivér, deaktivér og slet
# ============================================================
#  userAccountControl (UAC) er et tal, hvor hver bit er et flag:
#      2  ACCOUNTDISABLE   kontoen er deaktiveret
#     32  PASSWD_NOTREQD   kontoen kræver ingen adgangskode
#    512  NORMAL_ACCOUNT   almindelig brugerkonto
#  conn.delete(dn) sletter et objekt. Der er ingen fortryd-knap.
#  Kræver at ex1_opret.py og ex3_grupper.py er kørt.
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
# ============================================================
from ldap3 import SUBTREE, MODIFY_REPLACE
from ad_hjaelp import forbind, overskrift, vis_resultat, vis_bruger

conn = forbind()

# ------------------------------------------------------------
# Trin 1 · Dine testbrugere og din gruppe fra ex1 og ex3. Findes de?
# ------------------------------------------------------------
ou = "OU=Modul8,OU=Testdata,DC=CSIK_DC_1,DC=local"
logon = conn.user.split("\\")[-1]
navn = ("test." + logon)[:20]
dn = "CN=" + navn + "," + ou
navn2 = ("test2." + logon)[:20]
dn2 = "CN=" + navn2 + "," + ou
egen_gruppe = "CN=GRP_" + logon + "," + ou

conn.search(ou, "(sAMAccountName=" + navn + ")", SUBTREE)
if len(conn.entries) == 0:
    overskrift("Trin 1 · Stop")
    print("    " + navn + " findes ikke. Kør ex1_opret.py først.")
    exit()

overskrift("Trin 1 · Dine objekter i OU=Modul8")
conn.search(ou, "(|(sAMAccountName=" + navn + ")(sAMAccountName=" + navn2 + ")(sAMAccountName=GRP_" + logon + "))",
            SUBTREE, attributes=["sAMAccountName", "objectClass"])
for e in conn.entries:
    print("   ", e.sAMAccountName, "·", e.objectClass.values)
# 1a. Hvor mange objekter har du? Hvordan kan du se på objectClass, om det er en bruger eller en gruppe?

# ------------------------------------------------------------
# Trin 2 · Læs UAC og find bittene
# ------------------------------------------------------------
overskrift("Trin 2 · userAccountControl på " + navn)
conn.search(dn, "(objectClass=user)", attributes=["userAccountControl"])
uac = conn.entries[0].userAccountControl.value
print("    uac         :", uac)
print("    binær       :", bin(uac))
print("    uac & 2     :", uac & 2, " (2 betyder deaktiveret)")
print("    uac & 512   :", uac & 512, " (512 betyder almindelig konto)")
# 2a. Hvilke bit er sat i 514? Skriv tallet som en sum af flag.
# 2b. Hvad gør & (bitwise AND)? Hvorfor giver uac & 32 nul lige nu?

# ------------------------------------------------------------
# Trin 3 · Aktivér som almindelig konto (512)
# ------------------------------------------------------------
overskrift("Trin 3 · UAC = 512")
conn.modify(dn, {"userAccountControl": [(MODIFY_REPLACE, [512])]})
vis_resultat(conn)
# 3a. Hvorfor afviser AD ændringen? Læs message, og søg på nettet efter fejlkoden i starten af den.
# 3b. Hvilken indstilling i domænet står bag afvisningen? Hvor i AD finder man den?

# ------------------------------------------------------------
# Trin 4 · Aktivér uden krav om adgangskode
# ------------------------------------------------------------
flag = 32                                  # PASSWD_NOTREQD

if flag == "???":
    overskrift("Trin 4 · Stop")
    print("    Udfyld flag i Trin 4. Intet er ændret.")
    exit()

overskrift("Trin 4 · UAC = 512 + " + str(flag))
conn.modify(dn, {"userAccountControl": [(MODIFY_REPLACE, [512 + flag])]})
vis_resultat(conn)
vis_bruger(conn, dn)
# 4a. Hvilket tal endte UAC på? Hvordan ser kontoen ud i ADUC nu (F5)?
# 4b. Hvorfor er en aktiv konto uden krav om adgangskode farlig?

# ------------------------------------------------------------
# Trin 5 · Skriv selv: deaktivér brugeren igen (514)
# ------------------------------------------------------------
overskrift("Trin 5 · UAC = 514")
conn.modify(dn, {"userAccountControl": [(MODIFY_REPLACE, [514])]})
vis_resultat(conn)
vis_bruger(conn, dn)
# 5a. Hvad blev der af PASSWD_NOTREQD, da du skrev 514? Hvorfor?

# ------------------------------------------------------------
# Trin 6 · Audit: find konti uden krav om adgangskode (bitwise LDAP-filter)
# ------------------------------------------------------------
#  :1.2.840.113556.1.4.803: betyder "bitwise AND" i et LDAP-filter.
#  Eksempel: deaktiverede brugere (bit 2)
filter_deaktiveret = "(userAccountControl:1.2.840.113556.1.4.803:=2)"
filter_passwd = "(userAccountControl:1.2.840.113556.1.4.803:=32)"

if filter_passwd == "???":
    overskrift("Trin 6 · Stop")
    print("    Udfyld filter_passwd i Trin 6.")
    exit()

overskrift("Trin 6 · Deaktiverede konti og konti med PASSWD_NOTREQD")
conn.search(ou, filter_deaktiveret, SUBTREE, attributes=["sAMAccountName"])
print("    deaktiverede:", len(conn.entries))
conn.search(ou, filter_passwd, SUBTREE, attributes=["sAMAccountName", "userAccountControl"])
print("    uden krav   :", len(conn.entries))
for e in conn.entries:
    print("   ", e.sAMAccountName, "·", e.userAccountControl)
# 6a. Hvorfor kan man ikke bare søge på (userAccountControl=32)?
# 6b. Hvorfor er det en god audit-kontrol at køre filteret med 32 på hele domænet?

# ------------------------------------------------------------
# Trin 7 · Fejl med vilje: slet en bruger, der ikke findes
# ------------------------------------------------------------
overskrift("Trin 7 · conn.delete() på en bruger, der ikke findes")
conn.delete("CN=findes.ikke," + ou)
vis_resultat(conn)
# 7a. Hvilken result-kode får du? Hvor har du set den før?

# ------------------------------------------------------------
# Trin 8 · Skriv selv: slet din gruppe fra ex3
# ------------------------------------------------------------
overskrift("Trin 8 · Slet GRP_" + logon)
conn.delete(egen_gruppe)
vis_resultat(conn)
# 8a. Gruppen havde to medlemmer. Blev brugerne slettet sammen med gruppen?

# ------------------------------------------------------------
# Trin 9 · Skriv selv: slet bruger nummer to
# ------------------------------------------------------------
svar = input("\nSlet " + navn2 + " nu? (j/n): ")
if svar == "j":
    overskrift("Trin 9 · Slet " + navn2)
    conn.delete(dn2)
    vis_resultat(conn)
    vis_bruger(conn, dn2)
# 9a. Hvorfor spørger scriptet, før det sletter?

# ------------------------------------------------------------
# Trin 10 · Slet testbrugeren
# ------------------------------------------------------------
svar = input("\nSlet " + navn + " nu? (j/n): ")
if svar == "j":
    overskrift("Trin 10 · Slet " + navn)
    conn.delete(dn)
    vis_resultat(conn)
    vis_bruger(conn, dn)
# 10a. Hvad sker der med brugerens SID, når den slettes? Kan en ny bruger med samme navn få den?
# 10b. Kør ex1_opret.py igen og opret brugeren på ny. Er objectGUID og objectSid de samme som før?

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
