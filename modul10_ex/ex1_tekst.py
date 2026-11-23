# ============================================================
#  MODUL 10 · Sprint 1 · Øvelse 1 · Tekst og logons
#  Repeterer: Modul 1 (typer, løkker, funktioner) og Modul 2 (substitution, optælling)
# ============================================================
#  I Modul 10 samler vi alt fra de første ni moduler. Værktøjet ligger
#  færdigt i tre moduler, som du importerer:
#      tekst_vaerktoej.py   (denne sprint)
#      csv_vaerktoej.py     (Sprint 2)
#      ad_vaerktoej.py      (Sprint 3)
#  I Sprint 4 bygger du ét script, der bruger dem alle.
#
#  Du skal IKKE ændre i modulerne. Alt, du skriver, skriver du i denne fil.
#  Hav tekst_vaerktoej.py åben ved siden af, mens du arbejder.
#
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
#
#  Trin 1-5 er kernen. Trin 6-10 er BONUS, hvis du har tid tilbage.
# ============================================================
from datetime import datetime
from tekst_vaerktoej import overskrift, erstat_danske, lav_logon, tael_tegn, kodeord_score, ad_dato

# ------------------------------------------------------------
# Trin 1 · Brug et færdigt modul
# ------------------------------------------------------------
overskrift("Trin 1 · lav_logon fra tekst_vaerktoej")
print("    Anne Hansen   :", lav_logon("Anne", "Hansen"))
# TODO: skriv logon ud for Søren Ægidius og for Clara Christensen-Søndergaard på samme måde
# 1a. Åbn tekst_vaerktoej.py. Hvilke ting gør lav_logon ved navnet, før det returneres?
# 1b. Hvorfor bliver Claras logon kortere end hendes navn? Hvor har du mødt grænsen før?
# 1c. Hvad betyder maks=20 i linjen def lav_logon(fornavn, efternavn, maks=20)?

# ------------------------------------------------------------
# Trin 2 · Lister, dicts og løkker
# ------------------------------------------------------------
personer = [
    {"fornavn": "Anne",  "efternavn": "Hansen",                 "afdeling": "IT"},
    {"fornavn": "Søren", "efternavn": "Ægidius",                "afdeling": "IT"},
    {"fornavn": "Clara", "efternavn": "Christensen-Søndergaard", "afdeling": "HR"},
    {"fornavn": "Ali",   "efternavn": "Hansen",                 "afdeling": "Salg"},
    {"fornavn": "Åse",   "efternavn": "Lund",                   "afdeling": "Salg"},
    {"fornavn": "Peter", "efternavn": "Madsen",                 "afdeling": "HR"},
]
overskrift("Trin 2 · Logon for alle personer")
# TODO: løb personer igennem, og skriv fornavn, efternavn og logon ud for hver person
#       Brug printet herunder i løkken:
#       print(f"    {fornavn:<7} {efternavn:<25} {logon}")
# 2a. Hvilken type har personer, og hvilken type har personer[0]? Tjek det med type().
# 2b. To personer får samme logon. Hvem? Hvad ville AD svare, hvis vi oprettede begge (Modul 8)?
# 2c. Hvad betyder :<7 og :<25 i f-strengen?

# ------------------------------------------------------------
# Trin 3 · Substitution (Modul 2)
# ------------------------------------------------------------
#  erstat_danske er en substitution: hvert tegn slås op i en tabel (en dict).
#  Nu laver du din egen tabel, der laver bogstaver om til tal, som mange gør i kodeord.
overskrift("Trin 3 · Egen substitutionstabel")
ordet = "sommerferie"
leet = {}           # TODO: fyld tabellen, så a bliver 4, e bliver 3, i bliver 1, o bliver 0 og s bliver 5
nyt = ""
# TODO: løb ordet igennem tegn for tegn, og byg nyt op med tabellen (samme mønster som erstat_danske)
print("    før   :", ordet, "  score:", kodeord_score(ordet))
print("    efter :", nyt, "  score:", kodeord_score(nyt))
# 3a. Hvad gør leet.get(tegn, tegn)? Hvad ville der ske, hvis du skrev leet[tegn] i stedet?
# 3b. Steg scoren? Er "50mm3rf3r13" et godt kodeord? Hvorfor ikke?
# 3c. Hvorfor er en fast substitutionstabel nem at knække? Tænk på Modul 2.

# ------------------------------------------------------------
# Trin 4 · Optælling (Modul 2)
# ------------------------------------------------------------
overskrift("Trin 4 · Optælling med en dict")
tekst = "hemmelig besked til it-afdelingen"
antal = tael_tegn(tekst.replace(" ", ""))
for tegn in sorted(antal, key=lambda t: antal[t], reverse=True)[:5]:
    print(f"    {tegn}  {antal[tegn]}")
afdelinger = {}
# TODO: løb personer igennem, og tæl hvor mange personer der er i hver afdeling
print("    afdelinger :", afdelinger)
# 4a. Hvad er nøglerne, og hvad er værdierne i afdelinger?
# 4b. Første gang en afdeling dukker op, findes den ikke i dict'en. Hvordan klarer din kode det?
# 4c. Hvilket bogstav er hyppigst i tekst? Hvordan brugte vi den slags optælling i Modul 2?

# ------------------------------------------------------------
# Trin 5 · Skriv din egen funktion (Modul 1)
# ------------------------------------------------------------
overskrift("Trin 5 · Egen funktion: lav_email")


def lav_email(fornavn, efternavn, domaene):
    # TODO: brug lav_logon, og returnér en e-mailadresse som "ahansen@firma.dk"
    return "???"


for p in personer:
    print(f"    {p['fornavn']:<7} {lav_email(p['fornavn'], p['efternavn'], 'firma.dk')}")
# 5a. Hvorfor kalder lav_email lav_logon i stedet for at gentage koden?
# 5b. Hvad er forskellen på at returnere værdien og bare printe den inde i funktionen?
# 5c. Hvad sker der, hvis du kalder lav_email med domaene "FIRMA.DK"? Er det et problem?


# ============================================================
#  BONUS · Trin 6-10
#  Gå kun videre, når Trin 1-5 er svaret.
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Kør modulet direkte
# ------------------------------------------------------------
#  Python giver hver fil en variabel, der hedder __name__.
#  Starter du filen selv, er __name__ lig "__main__".
#  Bliver filen importeret, er __name__ lig filens navn.
overskrift("Trin 6 · BONUS · __name__")
# TODO: skriv værdien af __name__ ud her i ex1
# 6a. Kør tekst_vaerktoej.py direkte (ikke ex1). Hvad ser du?
# 6b. Hvorfor kører selvtesten ikke, når ex1 importerer modulet?
# 6c. Hvad skrev din TODO ud? Hvorfor?

# ------------------------------------------------------------
# Trin 7 · BONUS · Unikke logons
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · Unikke logons")
brugte = []
for p in personer:
    logon = lav_logon(p["fornavn"], p["efternavn"])
    nr = 2
    # TODO: så længe logon allerede står i brugte, så prøv det oprindelige logon + nr (ahansen2,
    #       ahansen3 ...), og læg 1 til nr hver gang
    brugte.append(logon)
    print(f"    {p['fornavn']:<7} {logon}")
# 7a. Hvorfor er det en while-løkke og ikke en if?
# 7b. Et logon på 20 tegn får et tal på. Hvilket problem opstår, og hvordan kan det løses?
# 7c. brugte kender kun personerne i listen. Hvad mangler, før logon er unikt i hele AD?

# ------------------------------------------------------------
# Trin 8 · BONUS · Datoer fra AD
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · Datoer fra AD")
oprettet = ["20240315123045.0Z", "20251201080000.0Z", None]
for vaerdi in oprettet:
    dage = "-"
    # TODO: hvis vaerdi ikke er None, så regn ud hvor mange dage siden datoen er (brug datetime)
    print(f"    {str(vaerdi):<20} {ad_dato(vaerdi):<12} dage siden: {dage}")
# 8a. Hvad står de 14 første tegn i "20240315123045.0Z" for?
# 8b. Hvorfor skal ad_dato og din kode tåle None?
# 8c. Hvor brugte vi dage siden en dato i en audit? (Modul 9)

# ------------------------------------------------------------
# Trin 9 · BONUS · Caesar (Modul 2)
# ------------------------------------------------------------
overskrift("Trin 9 · BONUS · Caesar")
alfabet = "abcdefghijklmnopqrstuvwxyz"


def caesar(tekst, flyt):
    resultat = ""
    # TODO: flyt hvert bogstav i tekst flyt pladser frem i alfabet. Andre tegn beholdes.
    #       Husk at z + 1 skal blive til a.
    return resultat


hemmelig = caesar("ahansen", 3)
print("    krypteret :", hemmelig)
print("    tilbage   :", caesar(hemmelig, -3))
# 9a. Hvordan sørger din kode for, at z + 1 bliver a?
# 9b. Hvorfor kan caesar(..., -3) dekryptere?
# 9c. Hvor mange forskellige nøgler findes der? Hvad betyder det for sikkerheden?

# ------------------------------------------------------------
# Trin 10 · BONUS · Samlet oversigt
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · Samlet oversigt")
print(f"    {'navn':<32} {'logon':<20} {'afdeling'}")
print("    " + "-" * 62)
# TODO: skriv én linje pr. person med fulde navn, logon og afdeling under overskriften
# 10a. Hvilke funktioner fra tekst_vaerktoej har du brugt i dag?
# 10b. Listen personer er skrevet direkte i koden. Hvor ville den komme fra i virkeligheden?
