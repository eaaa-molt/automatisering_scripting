# ============================================================
#  LEKTION 7  ·  Sprint 1  ·  Øvelse 0.1
#  De tre trin: Server, Connection og operation
# ============================================================
#
#  Skriv de tre linjer markeret med # TODO. Skriv dine egne
#  oplysninger direkte i koden. Kør filen, når alle tre er
#  skrevet, og se hvad hvert trin printer.
#
# ============================================================

from ldap3 import Server, Connection, NTLM, SUBTREE


# ── Trin 1 · Server: hvor er AD? ─────────────────────────
# TODO: opret et Server-objekt med DC'ens IP (Øvelse 0, Del 1)
#       Server("10.160.x.x")
server = None

print("Trin 1:", server)


# ── Trin 2 · Connection: hvem er du? ─────────────────────
# TODO: opret en Connection med server og dine egne oplysninger
#       user="CSIK_DC_1\\dit.logonnavn", password="DinAdgangskode",
#       authentication=NTLM, auto_bind=True
conn = None

print("Trin 2: logget ind =", conn.bound)


# ── Trin 3 · Operation: hvad vil du? ─────────────────────
# TODO: søg efter dig selv med conn.search(...)
#       base:       "DC=CSIK_DC_1,DC=local"  (Øvelse 0, Del 3)
#       filter:     "(sAMAccountName=dit.logonnavn)"
#       scope:      SUBTREE
#       attributes: ["cn", "department"]

print("Trin 3:")
print(conn.entries[0])

conn.unbind()


# ============================================================
#  Observationsopgaver
#  1. Hvad printer Trin 1? Er der sendt noget til DC'en endnu?
#  2. Skriv en forkert kode i Trin 2. Hvilket trin fejler,
#     og hvad hedder fejlen?
#  3. Hvad står der i dit entry i Trin 3? Find dig selv i
#     ADUC og sammenlign.
# ============================================================
