# ============================================================
#  MODUL 9 · Sprint 4 · Øvelse 4 · Samlet auditscript
# ============================================================
#  Nu samler du Sprint 1-3 i ét script, der gemmer hele auditten som JSON.
#  JSON er formatet til maskiner: et andet script kan læse rapporten igen,
#  fx for at se hvad der har ændret sig siden sidste uge.
#  Scriptet LÆSER kun fra AD. Det skriver kun filer i din egen mappe.
#
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
#
#  Trin 1-5 er kernen. Trin 6-10 er BONUS, hvis du har tid tilbage.
# ============================================================
import json
from datetime import date, datetime
from pathlib import Path
from ldap3 import SUBTREE
from ad_hjaelp import forbind, overskrift

conn = forbind()
ou = "OU=Testdata,DC=CSIK_DC_1,DC=local"
domaene = "DC=CSIK_DC_1,DC=local"
mappe = Path(__file__).parent

# ------------------------------------------------------------
# Trin 1 · To funktioner til alle audit-søgninger
# ------------------------------------------------------------
#  I Sprint 1 skrev du næsten den samme søgning flere gange. Nu skriver du den én gang.
overskrift("Trin 1 · Funktionerne soeg() og med_flag()")


def soeg(ldap_filter):
    """Søg i ou med ldap_filter, og returnér en liste med sAMAccountName for hvert fund."""
    # TODO: søg i ou med ldap_filter, og hent sAMAccountName
    # TODO: lav en liste med sAMAccountName.value for hver entry, og returnér den
    return "???"


def med_flag(flag):
    """Returnér en liste med sAMAccountName for brugerne i ou, hvor flaget er sat i userAccountControl."""
    conn.search(ou, "(objectClass=user)", SUBTREE,
                attributes=["sAMAccountName", "userAccountControl"])
    logons = []
    for e in conn.entries:
        # TODO: tilføj e.sAMAccountName.value til logons, hvis flaget er sat (som i Sprint 1)
        pass
    return logons


test = soeg("(objectClass=user)")
if test == "???":
    print("    Udfyld funktionen soeg() i Trin 1.")
    exit()
print("    brugere     :", len(test))
print("    de første 3 :", test[:3])
print("    deaktiverede:", med_flag(2))
# 1a. Hvad er forskellen på at returnere conn.entries og at returnere en liste af tekster?
# 1b. Hvorfor er det en fordel at have søgningen i én funktion?
# 1c. Hvorfor bruger med_flag() Python & og ikke et LDAP-filter som soeg()?

# ------------------------------------------------------------
# Trin 2 · Saml auditten i én dict
# ------------------------------------------------------------
overskrift("Trin 2 · Auditten som dict")
filter_ingen_afd = "(&(objectClass=user)(!(department=*)))"

audit = {
    "dato": date.today().isoformat(),
    "udfoert_af": conn.user,
    "deaktiverede": "???",                 # TODO: kald med_flag() med det rigtige flag
    "udloeber_aldrig": "???",              # TODO: kald med_flag() med det rigtige flag
    "ingen_afdeling": "???",               # TODO: kald soeg() med filter_ingen_afd
}
if "???" in audit.values():
    print("    Udfyld de tre kald i Trin 2.")
    exit()
print("   ", audit)
# 2a. Hvilke datatyper er værdierne i audit? (Tip: print(type(...)))
# 2b. Hvorfor gemmer vi, hvem der har kørt auditten, og hvornår?

# ------------------------------------------------------------
# Trin 3 · Gem auditten som audit.json
# ------------------------------------------------------------
overskrift("Trin 3 · Gem audit.json")
fil = mappe / "audit.json"
with open(fil, "w", encoding="utf-8") as f:
    pass                                   # TODO: erstat pass med json.dump(...), så audit gemmes i f med indent=2
if fil.stat().st_size == 0:
    print("    audit.json er tom. Udfyld json.dump i Trin 3.")
    exit()
print("    gemt        :", fil)
print("    størrelse   :", fil.stat().st_size, "bytes")
# 3a. Åbn audit.json i VS Code. Ligner den din dict fra Trin 2? Hvad er forskellen?
# 3b. Fjern indent=2, og kør igen. Hvad sker der med filen? Hvornår ville du undlade indent?
# 3c. Sæt et æ i "udfoert_af"-teksten, og kør. Hvordan står det i filen? Prøv så med ensure_ascii=False.

# ------------------------------------------------------------
# Trin 4 · Læs auditten igen
# ------------------------------------------------------------
overskrift("Trin 4 · Læs audit.json")
with open(fil, encoding="utf-8") as f:
    indlaest = json.load(f)
print("    type        :", type(indlaest))
print("    dato        :", indlaest["dato"])
# TODO: lav en for-løkke over indlaest.items(), og skriv nøgle og antal ud for hver værdi, der er en liste
#       (Tip: isinstance(vaerdi, list))
# 4a. Hvilken datatype har indlaest, og hvilken har indlaest["deaktiverede"]?
# 4b. Er indlaest == audit? Prøv print(indlaest == audit).

# ------------------------------------------------------------
# Trin 5 · Hvornår CSV, og hvornår JSON?
# ------------------------------------------------------------
overskrift("Trin 5 · CSV eller JSON")
print("    Svar på spørgsmålene herunder. Der er ingen kode i dette trin.")
# 5a. Kunne audit-dict'en fra Trin 2 gemmes som én CSV-fil? Hvad ville der ske med listerne?
# 5b. Hvem er modtageren af brugere.csv (Sprint 2), og hvem er modtageren af audit.json?
# 5c. Hvad er serialisering? Forklar det med dine egne ord ud fra Trin 3 og 4.


# ============================================================
#  BONUS · Trin 6-10
#  Gå kun videre, når Trin 1-5 er svaret.
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Tilføj en opsummering
# ------------------------------------------------------------
overskrift("Trin 6 · BONUS · Opsummering med antal")
# TODO: tilføj nøglen "antal" til audit med en dict, fx {"deaktiverede": 4, "udloeber_aldrig": 1, ...}
#       Byg den med en for-løkke over de tre fund-nøgler
print("    antal       :", audit.get("antal"))
# 6a. Hvorfor er det smart at have antallet i filen, når listerne allerede står der?
# 6b. Hvad giver audit.get("antal"), hvis du ikke har lavet TODO'en? Og audit["antal"]?

# ------------------------------------------------------------
# Trin 7 · BONUS · Admin-grupper i auditten (Sprint 3)
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · Domain Admins i auditten")


def medlemmer(gruppe):
    """Returnér en liste med navnene (CN) på de direkte medlemmer af gruppen."""
    # TODO: søg efter gruppen i domaene (som i Sprint 3, Trin 3), og returnér navnene som en liste
    return []


audit["domain_admins"] = medlemmer("Domain Admins")
print("    domain_admins:", audit["domain_admins"])
# 7a. Hvorfor returnerer funktionen i øvelsen en tom liste [] og ikke en tekst med spørgsmålstegn som de andre stopklodser?

# ------------------------------------------------------------
# Trin 8 · BONUS · Hvad har ændret sig siden sidst?
# ------------------------------------------------------------
#  Kør scriptet to gange. Anden gang findes audit_forrige.json fra første kørsel.
overskrift("Trin 8 · BONUS · Ændringer siden forrige kørsel")
forrige_fil = mappe / "audit_forrige.json"
if forrige_fil.exists():
    with open(forrige_fil, encoding="utf-8") as f:
        forrige = json.load(f)
    # TODO: find de logons, der er deaktiverede nu, men ikke var det sidst (Tip: set og minus)
    # TODO: find de logons, der var deaktiverede sidst, men ikke er det nu
else:
    print("    Ingen forrige audit endnu. Kør scriptet en gang til.")
with open(forrige_fil, "w", encoding="utf-8") as f:
    json.dump(audit, f, indent=2, ensure_ascii=False)
# 8a. Hvad er resultatet, hvis intet har ændret sig? Hvilken datatype er det?
# 8b. Kør ex1_opret.py fra Modul 8 (den opretter test.<dit logon> som deaktiveret), og kør så dette script igen.
#     Hvad viser Trin 8? Husk at slette brugeren igen bagefter (Modul 8, Øvelse 4, eller spørg Michael).
# 8c. Hvorfor kan man kun lave denne sammenligning, fordi auditten er gemt som JSON og ikke som tekst?

# ------------------------------------------------------------
# Trin 9 · BONUS · Dato i filnavnet
# ------------------------------------------------------------
overskrift("Trin 9 · BONUS · audit_<dato>.json")
dato_fil = "???"                          # TODO: mappe / "audit_2026-11-16.json", men med dagens dato fra audit["dato"]
if dato_fil == "???":
    print("    Udfyld dato_fil i Trin 9.")
    exit()
with open(dato_fil, "w", encoding="utf-8") as f:
    json.dump(audit, f, indent=2, ensure_ascii=False)
print("    gemt        :", dato_fil)
# 9a. Hvorfor er formatet 2026-11-16 bedre i et filnavn end 16-11-2026?
# 9b. Hvad sker der, hvis du kører scriptet to gange samme dag?

# ------------------------------------------------------------
# Trin 10 · BONUS · Ikke alt kan blive til JSON
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · datetime i JSON")
proeve = {"tidspunkt": datetime.now()}
try:
    print("   ", json.dumps(proeve))
except TypeError as fejl:
    print("    TypeError   :", fejl)
# TODO: lav proeve om, så tidspunktet kan gemmes som JSON, og skriv json.dumps(...) ud
# 10a. Hvilken fejl giver json.dumps, og hvorfor?
# 10b. Hvorfor brugte vi date.today().isoformat() i Trin 2 og ikke bare date.today()?

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
