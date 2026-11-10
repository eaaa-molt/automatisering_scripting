"""
MODUL 8 · Hjælpemodul - du skal IKKE ændre noget her.

Modulet gør to ting, så øvelserne kan handle om selve LDAP-operationerne:

  forbind()               logger ind med oplysningerne i config_ad.json
  overskrift(tekst)       skriver en tydelig overskrift over hvert trin
  vis_resultat(conn)      viser AD's svar efter add, modify og delete
  vis_bruger(conn, dn)    viser en brugers attributter som en pæn liste
"""

import json
from pathlib import Path
from ldap3 import Server, Connection, NTLM, BASE


def forbind():
    """Log ind i AD med config_ad.json og returnér forbindelsen."""
    try:
        cfg = json.loads((Path(__file__).parent / "config_ad.json").read_text(encoding="utf-8"))
    except FileNotFoundError:
        print("Fejl: config_ad.json findes ikke.")
        print("Kopiér config_ad_template.json til config_ad.json og udfyld den.")
        raise SystemExit
    try:
        server = Server(cfg["server"])
        return Connection(server, user=cfg["bruger"], password=cfg["adgangskode"],
                          authentication=NTLM, auto_bind=True)
    except Exception as fejl:
        print(f"Forbindelsesfejl: {fejl}")
        print("Tjek server, bruger og adgangskode i config_ad.json.")
        raise SystemExit


def overskrift(tekst):
    """Skriv en overskrift med streger over og under, så trinene er lette at skelne."""
    print()
    print("=" * 65)
    print("  " + tekst)
    print("=" * 65)


def vis_resultat(conn):
    """Vis svaret på den seneste operation: kode, beskrivelse og evt. besked."""
    r = conn.result
    print(f"    result      : {r['result']}  ({r['description']})")
    if r["result"] != 0 and r.get("message"):
        print(f"    message     : {r['message'].strip()}")


def vis_bruger(conn, dn):
    """Slå brugeren op via sit DN og vis de vigtigste attributter."""
    if not conn.search(dn, "(objectClass=user)", BASE, attributes=["*"]):
        print(f"    (brugeren findes ikke: {dn})")
        return
    e = conn.entries[0]
    for attr in ["sAMAccountName", "userPrincipalName", "givenName", "sn", "displayName",
                 "department", "title",
                 "description", "userAccountControl", "memberOf"]:
        vaerdier = e[attr].values if attr in e else []
        tekst = ", ".join(str(v).split(",")[0].replace("CN=", "") if attr == "memberOf" else str(v)
                          for v in vaerdier)
        print(f"    {attr:<20}: {tekst or '-'}")
