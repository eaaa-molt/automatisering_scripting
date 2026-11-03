# ============================================================
#  LEKTION 7  ·  Sprint 1  ·  Øvelse 0.1 · Løsning
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
server = Server("10.160.0.220")

print("Trin 1:", server)


# ── Trin 2 · Connection: hvem er du? ─────────────────────
conn = Connection(server, user="CSIK_DC_1\\dit.logonnavn",
                  password="DinAdgangskode", authentication=NTLM,
                  auto_bind=True)

print("Trin 2: logget ind =", conn.bound)


# ── Trin 3 · Operation: hvad vil du? ─────────────────────
conn.search("DC=CSIK_DC_1,DC=local", "(sAMAccountName=dit.logonnavn)",
            SUBTREE, attributes=["cn", "department"])

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
