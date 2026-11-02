"""
=============================================================
  LEKTION 7  ·  Hjælpemodul til ex2, ex3 og ex4
=============================================================
Du skal IKKE ændre noget i denne fil.

Den samler den kode, der går igen i alle øvelserne, så
øvelsesfilerne kun indeholder det, du selv skal arbejde med:

  forbind()      - læser config_ad.json og forbinder til AD
  tekst()        - henter en attribut som tekst ("" hvis tom)
  kort_navn()    - CN=GRP_IT,OU=Grupper,... → GRP_IT
  vis_brugere()  - udskriver brugere som en pæn tabel

Brug i en øvelse:
  from ad_hjaelp import forbind, tekst, kort_navn, vis_brugere
=============================================================
"""

import json
from pathlib import Path
from ldap3 import Server, Connection, ALL, NTLM

MAPPE = Path(__file__).parent


def forbind():
    """Forbind til AD med oplysningerne i config_ad.json.

    Returnerer (conn, base_dn). Stopper scriptet ved fejl.
    """
    try:
        with open(MAPPE / "config_ad.json", encoding="utf-8") as f:
            cfg = json.load(f)
    except FileNotFoundError:
        print("Fejl: config_ad.json ikke fundet.")
        print("Kopiér config_ad_template.json til config_ad.json og udfyld.")
        raise SystemExit

    try:
        server = Server(cfg["server"], get_info=ALL)
        conn = Connection(
            server,
            user           = cfg["bruger"],
            password       = cfg["adgangskode"],
            authentication = NTLM,
            auto_bind      = True,
            auto_referrals = False,
        )
    except Exception as e:
        print(f"Forbindelsesfejl: {e}")
        print("Tjek server, bruger og adgangskode i config_ad.json.")
        raise SystemExit

    return conn, cfg["base_dn"]


def tekst(entry, attribut):
    """Returnér attributten som tekst - eller "" hvis den ikke er sat."""
    if attribut not in entry:
        return ""
    vaerdi = entry[attribut].value
    if vaerdi is None:
        return ""
    return str(vaerdi)


def kort_navn(dn):
    """CN=GRP_IT_Admins,OU=Grupper,... → GRP_IT_Admins"""
    return dn.split(",")[0].replace("CN=", "")


def vis_brugere(entries, overskrift):
    """Udskriv en liste af bruger-entries som tabel."""
    print(f"\n{'─' * 65}")
    print(f"  {overskrift}  →  {len(entries)} bruger(e)")
    print(f"{'─' * 65}")
    print(f"  {'Logonnavn':<26} {'Afdeling':<12} Titel")
    print(f"  {'·' * 26} {'·' * 12} {'·' * 22}")
    for e in entries:
        print(f"  {tekst(e, 'sAMAccountName'):<26} "
              f"{tekst(e, 'department'):<12} {tekst(e, 'title')}")
