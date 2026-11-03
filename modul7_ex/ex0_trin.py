# ============================================================
#  LEKTION 7  ·  Sprint 1  ·  Øvelse 0.1
#  De tre trin: Server, Connection og operation
# ============================================================
#
#  Udfyld de tre konstanter og skriv de tre linjer markeret
#  med # TODO. Kør filen, når alle tre er skrevet, og se
#  hvad hvert trin printer.
#
# ============================================================

from ldap3 import Server, Connection, NTLM, SUBTREE

AD_SERVER  = "10.160.x.x"             # DC'ens IP-adresse (Øvelse 0, Del 1)
LOGONNAVN  = "dit.logonnavn"          # dit logonnavn uden domæne
AD_KODE    = "DinAdgangskode"         # din AD-adgangskode
AD_BASE_DN = "DC=CSIK_DC_1,DC=local"  # defaultNamingContext (Øvelse 0, Del 3)


# ── Trin 1 · Server: hvor er AD? ─────────────────────────
# TODO: opret et Server-objekt med AD_SERVER
server = None

print("Trin 1:", server)


# ── Trin 2 · Connection: hvem er du? ─────────────────────
# TODO: opret en Connection med server og
#       user="CSIK_DC_1\\" + LOGONNAVN, password=AD_KODE,
#       authentication=NTLM, auto_bind=True
conn = None

print("Trin 2: logget ind =", conn.bound)


# ── Trin 3 · Operation: hvad vil du? ─────────────────────
# TODO: søg i AD_BASE_DN med filteret
#       "(sAMAccountName=" + LOGONNAVN + ")", SUBTREE og
#       attributes=["cn", "department"]

print("Trin 3:")
print(conn.entries[0])

conn.unbind()


# ============================================================
#  Observationsopgaver
#  1. Hvad printer Trin 1? Er der sendt noget til DC'en endnu?
#  2. Skriv en forkert kode i AD_KODE. Hvilket trin fejler,
#     og hvad hedder fejlen?
#  3. Hvad står der i dit entry i Trin 3? Find dig selv i
#     ADUC og sammenlign.
# ============================================================
