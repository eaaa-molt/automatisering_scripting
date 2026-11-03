from ldap3 import Server, Connection, NTLM, SUBTREE

# Trin 1 · Server: hvor er AD?
server = Server("10.160.0.220")
print("Trin 1:", server)

# Trin 2 · Connection: hvem er du?
conn = Connection(server,
                  user="CSIK_DC_1\\dit.logonnavn",
                  password="DinAdgangskode",
                  authentication=NTLM, auto_bind=True)
print("Trin 2: logget ind =", conn.bound)

# Trin 3 · Operation: hvad vil du?
conn.search("DC=CSIK_DC_1,DC=local",
            "(sAMAccountName=dit.logonnavn)",     
            SUBTREE, attributes=["cn", "department"])
print("Trin 3:", conn.entries[0])

conn.unbind()
