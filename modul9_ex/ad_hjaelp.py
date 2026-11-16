"""
MODUL 9 · Hjælpemodul - du skal IKKE ændre noget her.

Modulet gør to ting, så øvelserne kan handle om selve auditten:

  forbind()               logger ind med oplysningerne i config_ad.json
  overskrift(tekst)       skriver en tydelig overskrift over hvert trin
"""

import json
from pathlib import Path
from ldap3 import Server, Connection, NTLM


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
