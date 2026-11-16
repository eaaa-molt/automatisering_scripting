# ============================================================
#  MODUL 9 · Sprint 4 · Løsning 4 · Samlet auditscript
# ============================================================
#  Løsningsforslag. Hver opgave (TODO) og hvert spørgsmål står som i
#  øvelsen, med løsningen eller svaret lige under.
#  Tal i svarene afhænger af, hvad der ligger i AD på dagen.
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
    conn.search(ou, ldap_filter, SUBTREE, attributes=["sAMAccountName"])
    # TODO: lav en liste med sAMAccountName.value for hver entry, og returnér den
    logons = []
    for e in conn.entries:
        logons.append(e.sAMAccountName.value)
    return logons


def med_flag(flag):
    """Returnér en liste med sAMAccountName for brugerne i ou, hvor flaget er sat i userAccountControl."""
    conn.search(ou, "(objectClass=user)", SUBTREE,
                attributes=["sAMAccountName", "userAccountControl"])
    logons = []
    for e in conn.entries:
        # TODO: tilføj e.sAMAccountName.value til logons, hvis flaget er sat (som i Sprint 1)
        if (e.userAccountControl.value & flag) != 0:
            logons.append(e.sAMAccountName.value)
    return logons


test = soeg("(objectClass=user)")
print("    brugere     :", len(test))
print("    de første 3 :", test[:3])
print("    deaktiverede:", med_flag(2))
# 1a. Hvad er forskellen på at returnere conn.entries og at returnere en liste af tekster?
#     Svar: conn.entries er ldap3-objekter, som bliver overskrevet ved næste søgning og
#           ikke kan gemmes som JSON. En liste af tekster er simpel data, som kan gemmes,
#           sammenlignes og sendes videre.
# 1b. Hvorfor er det en fordel at have søgningen i én funktion?
#     Svar: Koden står ét sted. Skal den rettes (fx en anden OU eller flere attributter),
#           rettes den én gang. Kaldene bliver korte og læsbare: med_flag(2).
# 1c. Hvorfor bruger med_flag() Python & og ikke et LDAP-filter som soeg()?
#     Svar: Et almindeligt LDAP-filter sammenligner hele tallet i userAccountControl og
#           kan ikke teste ét flag. Derfor henter vi alle brugere og tester flaget i Python,
#           som i Sprint 1. (Bitwise LDAP-filteret fra Sprint 1, BONUS Trin 9, kunne
#           også bruges.)

# ------------------------------------------------------------
# Trin 2 · Saml auditten i én dict
# ------------------------------------------------------------
overskrift("Trin 2 · Auditten som dict")
filter_ingen_afd = "(&(objectClass=user)(!(department=*)))"

audit = {
    "dato": date.today().isoformat(),
    "udfoert_af": conn.user,
    # TODO: kald med_flag() med det rigtige flag (to gange) og soeg() med filter_ingen_afd
    "deaktiverede": med_flag(2),
    "udloeber_aldrig": med_flag(65536),
    "ingen_afdeling": soeg(filter_ingen_afd),
}
print("   ", audit)
# 2a. Hvilke datatyper er værdierne i audit? (Tip: print(type(...)))
#     Svar: "dato" og "udfoert_af" er str. De tre fund er list med str i.
# 2b. Hvorfor gemmer vi, hvem der har kørt auditten, og hvornår?
#     Svar: En audit skal kunne spores. Uden dato og person ved man ikke, hvor gamle
#           tallene er, eller hvem der har set dataene. Det er god praksis (og et krav i
#           mange standarder, fx ISO 27001).

# ------------------------------------------------------------
# Trin 3 · Gem auditten som audit.json
# ------------------------------------------------------------
overskrift("Trin 3 · Gem audit.json")
fil = mappe / "audit.json"
with open(fil, "w", encoding="utf-8") as f:
    # TODO: erstat pass med json.dump(...), så audit gemmes i f med indent=2
    json.dump(audit, f, indent=2, ensure_ascii=False)
if fil.stat().st_size == 0:
    print("    audit.json er tom. Udfyld json.dump i Trin 3.")
    exit()
print("    gemt        :", fil)
print("    størrelse   :", fil.stat().st_size, "bytes")
# 3a. Åbn audit.json i VS Code. Ligner den din dict fra Trin 2? Hvad er forskellen?
#     Svar: Næsten ens. JSON bruger altid dobbelte anførselstegn, og strukturen er den
#           samme: {} for dict og [] for list.
# 3b. Fjern indent=2, og kør igen. Hvad sker der med filen? Hvornår ville du undlade indent?
#     Svar: Alt står på én linje, og filen bliver mindre. Uden indent er fint, når kun
#           maskiner skal læse filen. Med indent kan mennesker læse den.
# 3c. Sæt et æ i "udfoert_af"-teksten, og kør. Hvordan står det i filen? Prøv så med ensure_ascii=False.
#     Svar: Som standard skrives æ som æ. Med ensure_ascii=False skrives æ som æ.
#           Begge dele læses korrekt af json.load, men kun det sidste er læsbart for mennesker.

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
for noegle, vaerdi in indlaest.items():
    if isinstance(vaerdi, list):
        print(f"    {noegle:<16}: {len(vaerdi)}")
# 4a. Hvilken datatype har indlaest, og hvilken har indlaest["deaktiverede"]?
#     Svar: dict og list. JSON husker strukturen og datatyperne (tekst, tal, lister,
#           dicts, True/False). Det gør CSV ikke (Sprint 2, 5c).
# 4b. Er indlaest == audit? Prøv print(indlaest == audit).
#     Svar: True. Data kommer uændret tilbage. Det kaldes en rundtur (round trip):
#           serialisering til fil og tilbage igen.

# ------------------------------------------------------------
# Trin 5 · Hvornår CSV, og hvornår JSON?
# ------------------------------------------------------------
overskrift("Trin 5 · CSV eller JSON")
print("    Svar på spørgsmålene herunder. Der er ingen kode i dette trin.")
# 5a. Kunne audit-dict'en fra Trin 2 gemmes som én CSV-fil? Hvad ville der ske med listerne?
#     Svar: Ikke direkte. CSV er en flad tabel. Listerne har forskellig længde og skulle
#           laves om, fx til rækker med (kategori, logon). Dato og udført af passer
#           ikke ind i tabellen.
# 5b. Hvem er modtageren af brugere.csv (Sprint 2), og hvem er modtageren af audit.json?
#     Svar: brugere.csv er til mennesker i et regneark (HR, ledere). audit.json er til
#           programmer: et andet script, et dashboard eller et SIEM.
# 5c. Hvad er serialisering? Forklar det med dine egne ord ud fra Trin 3 og 4.
#     Svar: At lave data i hukommelsen (dict, list) om til tekst eller bytes, der kan gemmes
#           eller sendes, og bagefter genskabe dem (deserialisering). json.dump og
#           json.load er de to retninger.


# ============================================================
#  BONUS · Trin 6-10
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Tilføj en opsummering
# ------------------------------------------------------------
overskrift("Trin 6 · BONUS · Opsummering med antal")
# TODO: tilføj nøglen "antal" til audit med en dict, fx {"deaktiverede": 4, "udloeber_aldrig": 1, ...}
#       Byg den med en for-løkke over de tre fund-nøgler
antal = {}
for noegle in ["deaktiverede", "udloeber_aldrig", "ingen_afdeling"]:
    antal[noegle] = len(audit[noegle])
audit["antal"] = antal
print("    antal       :", audit.get("antal"))
# 6a. Hvorfor er det smart at have antallet i filen, når listerne allerede står der?
#     Svar: Den, der læser filen, kan se overblikket med det samme uden at tælle. Et
#           dashboard kan læse tallene direkte.
# 6b. Hvad giver audit.get("antal"), hvis du ikke har lavet TODO'en? Og audit["antal"]?
#     Svar: get giver None. Med firkantede parenteser får man KeyError.

# ------------------------------------------------------------
# Trin 7 · BONUS · Admin-grupper i auditten (Sprint 3)
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · Domain Admins i auditten")


def medlemmer(gruppe):
    """Returnér en liste med navnene (CN) på de direkte medlemmer af gruppen."""
    # TODO: søg efter gruppen i domaene (som i Sprint 3, Trin 3), og returnér navnene som en liste
    conn.search(domaene, "(cn=" + gruppe + ")", SUBTREE, attributes=["member"])
    navne = []
    for dn in conn.entries[0].member.values:
        navne.append(dn.split(",")[0].replace("CN=", ""))
    return navne


audit["domain_admins"] = medlemmer("Domain Admins")
print("    domain_admins:", audit["domain_admins"])
# 7a. Hvorfor returnerer funktionen i øvelsen en tom liste [] og ikke en tekst med spørgsmålstegn som de andre stopklodser?
#     Svar: Så scriptet kan køre videre, før TODO'en er lavet. En tom liste har samme
#           datatype som svaret, så resten af koden virker.

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
    nye = set(audit["deaktiverede"]) - set(forrige["deaktiverede"])
    print("    nye deaktiverede     :", nye)
    # TODO: find de logons, der var deaktiverede sidst, men ikke er det nu
    genaktiverede = set(forrige["deaktiverede"]) - set(audit["deaktiverede"])
    print("    ikke deaktiveret mere:", genaktiverede)
else:
    print("    Ingen forrige audit endnu. Kør scriptet en gang til.")
with open(forrige_fil, "w", encoding="utf-8") as f:
    json.dump(audit, f, indent=2, ensure_ascii=False)
# 8a. Hvad er resultatet, hvis intet har ændret sig? Hvilken datatype er det?
#     Svar: set() (et tomt sæt). Mængdeforskel giver altid et set.
# 8b. Kør ex1_opret.py fra Modul 8 (den opretter test.<dit logon> som deaktiveret), og kør så dette script igen.
#     Hvad viser Trin 8? Husk at slette brugeren igen bagefter (Modul 8, Øvelse 4, eller spørg Michael).
#     Svar: test.<logon> står under "nye deaktiverede". OU=Modul8 ligger under OU=Testdata,
#           og med_flag() søger med SUBTREE, så den kommer med. Efter sletning og en ny kørsel
#           forsvinder den igen (den står så ikke under nogen af de to, fordi den slet ikke
#           findes mere, men den står i forrige).
# 8c. Hvorfor kan man kun lave denne sammenligning, fordi auditten er gemt som JSON og ikke som tekst?
#     Svar: json.load giver listerne tilbage som lister, som kan laves om til sets. Fra en
#           tekstrapport skulle man selv skille linjerne ad igen.

# ------------------------------------------------------------
# Trin 9 · BONUS · Dato i filnavnet
# ------------------------------------------------------------
overskrift("Trin 9 · BONUS · audit_<dato>.json")
# TODO: mappe / "audit_2026-11-16.json", men med dagens dato fra audit["dato"]
dato_fil = mappe / ("audit_" + audit["dato"] + ".json")
with open(dato_fil, "w", encoding="utf-8") as f:
    json.dump(audit, f, indent=2, ensure_ascii=False)
print("    gemt        :", dato_fil)
# 9a. Hvorfor er formatet 2026-11-16 bedre i et filnavn end 16-11-2026?
#     Svar: ÅÅÅÅ-MM-DD (ISO 8601) sorteres i rigtig rækkefølge alfabetisk. Så står
#           filerne i datoorden i Finder og Stifinder.
# 9b. Hvad sker der, hvis du kører scriptet to gange samme dag?
#     Svar: Filen overskrives. Vil man gemme hver kørsel, skal klokkeslættet med i navnet.

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
proeve = {"tidspunkt": datetime.now().isoformat(timespec="seconds")}
print("   ", json.dumps(proeve))
# 10a. Hvilken fejl giver json.dumps, og hvorfor?
#      Svar: TypeError: Object of type datetime is not JSON serializable. JSON kender kun
#            tekst, tal, true/false, null, lister og objekter. Et datetime er ingen af dem.
# 10b. Hvorfor brugte vi date.today().isoformat() i Trin 2 og ikke bare date.today()?
#      Svar: isoformat() laver datoen om til tekst ("2026-11-16"), som JSON kan gemme.
#            Ellers ville json.dump i Trin 3 fejle med samme TypeError.

conn.unbind()
overskrift("Færdig · husk at svare på spørgsmålene under hvert trin")
