"""
MODUL 10 · ad_vaerktoej · færdige funktioner til Active Directory
Du skal IKKE ændre noget i denne fil. Du bruger den fra dine egne scripts:

    from ad_vaerktoej import forbind, soeg

Funktionerne bygger på det, du har lavet i Modul 7, 8 og 9:

  forbind()                              logger ind med oplysningerne i config_ad.json
  mit_logon(conn)                        det logonnavn, du er logget ind med (fx "stud01")
  vis_resultat(conn)                     viser AD's svar efter add, modify og delete
  soeg(conn, base, ldap_filter, attributter)
                                         søger i AD og returnerer listen af entries
  findes_i_ad(conn, base, logon)         True hvis sAMAccountName findes under base
  har_flag(uac, flag)                    True hvis flaget er sat i userAccountControl
  gruppe_medlemmer(conn, base, gruppe)   navnene på medlemmerne af en gruppe
  find_nye(conn, base, brugere)          deler Bruger-objekter i nye og dubletter
  find_mine(conn, base, praefiks)        DN på alle brugere, hvis logon starter med praefiks

  Disse SKRIVER til AD, men kun hvis du kalder dem med dry_run=False:
  opret_bruger(conn, ou, bruger, dry_run=True)
  opret_alle(conn, ou, brugere, dry_run=True)
  tilfoej_til_gruppe(conn, bruger_dn, gruppe_dn, dry_run=True)
  slet_bruger(conn, dn, dry_run=True)
  slet_alle(conn, dn_liste, dry_run=True)
"""

import json
from pathlib import Path
from ldap3 import Server, Connection, NTLM, SUBTREE, MODIFY_ADD


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


def mit_logon(conn):
    """Returnér logonnavnet uden domæne: "CSIK_DC_1\\stud01" bliver til "stud01"."""
    return conn.user.split("\\")[-1]


def vis_resultat(conn):
    """Vis svaret på den seneste operation: kode, beskrivelse og evt. besked."""
    r = conn.result
    print(f"    result      : {r['result']}  ({r['description']})")
    if r["result"] != 0 and r.get("message"):
        print(f"    message     : {r['message'].strip()}")


def soeg(conn, base, ldap_filter, attributter):
    """Søg under base (SUBTREE) og returnér listen af entries."""
    conn.search(base, ldap_filter, SUBTREE, attributes=attributter)
    return conn.entries


def findes_i_ad(conn, base, logon):
    """Returnér True, hvis der findes et objekt med sAMAccountName = logon under base."""
    conn.search(base, "(sAMAccountName=" + logon + ")", SUBTREE)
    return len(conn.entries) > 0


def har_flag(uac, flag):
    """Returnér True, hvis flaget er sat i userAccountControl (fx 2 = deaktiveret)."""
    return (uac & flag) != 0


def gruppe_medlemmer(conn, base, gruppe):
    """Returnér en liste med CN på medlemmerne af gruppen (fx "GRP_IT")."""
    conn.search(base, "(&(objectClass=group)(cn=" + gruppe + "))", SUBTREE, attributes=["member"])
    if len(conn.entries) == 0:
        return []
    navne = []
    for dn in conn.entries[0].member.values:
        navne.append(dn.split(",")[0].replace("CN=", ""))
    return navne


def find_nye(conn, base, brugere):
    """Del en liste af Bruger-objekter i to lister og returnér dem: nye, dubletter
    En bruger er en dublet, hvis logon findes i AD under base, eller hvis
    samme logon allerede er set tidligere i listen."""
    nye = []
    dubletter = []
    set_logon = []
    for b in brugere:
        if findes_i_ad(conn, base, b.logon) or b.logon in set_logon:
            dubletter.append(b)
        else:
            nye.append(b)
            set_logon.append(b.logon)
    return nye, dubletter


def find_mine(conn, base, praefiks):
    """Returnér en liste med DN på alle brugere under base, hvis logon starter med praefiks."""
    conn.search(base, "(&(objectClass=user)(sAMAccountName=" + praefiks + "*))", SUBTREE)
    dn_liste = []
    for e in conn.entries:
        dn_liste.append(e.entry_dn)
    return dn_liste


def opret_bruger(conn, ou, bruger, dry_run=True):
    """Opret et Bruger-objekt (fra csv_vaerktoej) i ou som deaktiveret konto (514).
    Med dry_run=True skrives kun, hvad der VILLE ske. Returnér brugerens DN."""
    dn = "CN=" + bruger.logon + "," + ou
    if dry_run:
        print(f"    [DRY RUN] ville oprette {dn}")
        return dn
    conn.add(dn,
             ["top", "person", "organizationalPerson", "user"],
             {"sAMAccountName": bruger.logon,
              "userPrincipalName": bruger.logon + "@CSIK_DC_1.local",
              "givenName": bruger.fornavn,
              "sn": bruger.efternavn,
              "displayName": bruger.fulde_navn(),
              "department": bruger.afdeling,
              "title": bruger.titel,
              "userAccountControl": 514})
    print(f"    [OPRET] {dn}")
    vis_resultat(conn)
    return dn


def opret_alle(conn, ou, brugere, dry_run=True):
    """Kald opret_bruger for hver bruger i listen. Returnér en liste med deres DN."""
    dn_liste = []
    for b in brugere:
        dn_liste.append(opret_bruger(conn, ou, b, dry_run))
    return dn_liste


def tilfoej_til_gruppe(conn, bruger_dn, gruppe_dn, dry_run=True):
    """Meld brugeren ind i gruppen (MODIFY_ADD på gruppens member)."""
    if dry_run:
        print(f"    [DRY RUN] ville melde {bruger_dn.split(',')[0]} ind i {gruppe_dn.split(',')[0]}")
        return
    conn.modify(gruppe_dn, {"member": [(MODIFY_ADD, [bruger_dn])]})
    print(f"    [GRUPPE] {bruger_dn.split(',')[0]} ind i {gruppe_dn.split(',')[0]}")
    vis_resultat(conn)


def slet_bruger(conn, dn, dry_run=True):
    """Slet objektet med dette DN. Der er ingen fortryd-knap."""
    if dry_run:
        print(f"    [DRY RUN] ville slette {dn}")
        return
    conn.delete(dn)
    print(f"    [SLETTET] {dn}")
    vis_resultat(conn)


def slet_alle(conn, dn_liste, dry_run=True):
    """Kald slet_bruger for hvert DN i listen. Der er ingen fortryd-knap."""
    for dn in dn_liste:
        slet_bruger(conn, dn, dry_run)


# Selvtest: kører KUN når du starter denne fil direkte, ikke når den importeres.
# Den LÆSER kun fra AD.
if __name__ == "__main__":
    from tekst_vaerktoej import overskrift
    overskrift("Selvtest af ad_vaerktoej (læser kun)")
    conn = forbind()
    print("    logget ind som       :", mit_logon(conn))
    print("    findes_i_ad (dig)    :", findes_i_ad(conn, "DC=CSIK_DC_1,DC=local", mit_logon(conn)))
    print("    har_flag(514, 2)     :", har_flag(514, 2))
    print("    GRP_IT medlemmer     :", len(gruppe_medlemmer(conn, "DC=CSIK_DC_1,DC=local", "GRP_IT")))
    conn.unbind()
