# ============================================================
#  MODUL 10 · Sprint 1 · Løsning 1 · Tekst og logons
#  Repeterer: Modul 1 (typer, løkker, funktioner) og Modul 2 (substitution, optælling)
# ============================================================
#  Løsningsforslag. Hver opgave (TODO) og hvert spørgsmål står som i
#  øvelsen, med løsningen eller svaret lige under.
# ============================================================
from datetime import datetime
from tekst_vaerktoej import overskrift, erstat_danske, lav_logon, tael_tegn, kodeord_score, ad_dato

# ------------------------------------------------------------
# Trin 1 · Brug et færdigt modul
# ------------------------------------------------------------
overskrift("Trin 1 · lav_logon fra tekst_vaerktoej")
print("    Anne Hansen   :", lav_logon("Anne", "Hansen"))
# TODO: skriv logon ud for Søren Ægidius og for Clara Christensen-Søndergaard på samme måde
print("    Søren Ægidius :", lav_logon("Søren", "Ægidius"))
print("    Clara C-S     :", lav_logon("Clara", "Christensen-Søndergaard"))
# 1a. Åbn tekst_vaerktoej.py. Hvilke ting gør lav_logon ved navnet, før det returneres?
#     Svar: Fjerner mellemrum i enderne (strip), tager første bogstav af fornavnet og hele
#           efternavnet, laver alt til små bogstaver, fjerner mellemrum og bindestreg,
#           erstatter æ/ø/å via erstat_danske og klipper til højst 20 tegn.
# 1b. Hvorfor bliver Claras logon kortere end hendes navn? Hvor har du mødt grænsen før?
#     Svar: "cchristensensoendergaard" er 24 tegn og bliver klippet til 20 med [:maks].
#           sAMAccountName må højst være 20 tegn. Vi mødte det i Modul 8 med ("test." + logon)[:20].
# 1c. Hvad betyder maks=20 i linjen def lav_logon(fornavn, efternavn, maks=20)?
#     Svar: maks er en parameter med en standardværdi. Kalder man uden maks, bliver den 20.
#           Man kan selv vælge en anden, fx lav_logon("Anne", "Hansen", maks=5).

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
for p in personer:
    fornavn = p["fornavn"]
    efternavn = p["efternavn"]
    logon = lav_logon(fornavn, efternavn)
    print(f"    {fornavn:<7} {efternavn:<25} {logon}")
# 2a. Hvilken type har personer, og hvilken type har personer[0]? Tjek det med type().
#     Svar: personer er en list, personer[0] er en dict.
#           print(type(personer), type(personer[0])) giver <class 'list'> <class 'dict'>.
# 2b. To personer får samme logon. Hvem? Hvad ville AD svare, hvis vi oprettede begge (Modul 8)?
#     Svar: Anne Hansen og Ali Hansen får begge "ahansen". Anden oprettelse fejler med
#           result 68 entryAlreadyExists, fordi sAMAccountName skal være unik.
# 2c. Hvad betyder :<7 og :<25 i f-strengen?
#     Svar: Venstrestil og fyld op med mellemrum til 7 og 25 tegn, så kolonnerne står lige.

# ------------------------------------------------------------
# Trin 3 · Substitution (Modul 2)
# ------------------------------------------------------------
#  erstat_danske er en substitution: hvert tegn slås op i en tabel (en dict).
#  Nu laver du din egen tabel, der laver bogstaver om til tal, som mange gør i kodeord.
overskrift("Trin 3 · Egen substitutionstabel")
ordet = "sommerferie"
# TODO: fyld tabellen, så a bliver 4, e bliver 3, i bliver 1, o bliver 0 og s bliver 5
leet = {"a": "4", "e": "3", "i": "1", "o": "0", "s": "5"}
nyt = ""
# TODO: løb ordet igennem tegn for tegn, og byg nyt op med tabellen (samme mønster som erstat_danske)
for tegn in ordet:
    nyt += leet.get(tegn, tegn)
print("    før   :", ordet, "  score:", kodeord_score(ordet))
print("    efter :", nyt, "  score:", kodeord_score(nyt))
# 3a. Hvad gør leet.get(tegn, tegn)? Hvad ville der ske, hvis du skrev leet[tegn] i stedet?
#     Svar: get slår tegn op og returnerer tegnet selv, hvis det ikke står i tabellen.
#           leet[tegn] giver KeyError ved første tegn, der ikke er i tabellen (fx "m").
# 3b. Steg scoren? Er "50mm3rf3r13" et godt kodeord? Hvorfor ikke?
#     Svar: Scoren stiger fra 1 til 2 (nu også cifre). Men det er stadig et dårligt kodeord:
#           det er et almindeligt ord med en kendt substitution, og ordbogsangreb prøver netop
#           de udskiftninger. Scoren måler kun tegntyper, ikke hvor gætteligt det er.
# 3c. Hvorfor er en fast substitutionstabel nem at knække? Tænk på Modul 2.
#     Svar: Samme tegn bliver altid til samme tegn, så mønstre og bogstavhyppighed bevares.
#           Frekvensanalyse (Modul 2) afslører derfor tabellen.

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
for p in personer:
    afd = p["afdeling"]
    afdelinger[afd] = afdelinger.get(afd, 0) + 1
print("    afdelinger :", afdelinger)
# 4a. Hvad er nøglerne, og hvad er værdierne i afdelinger?
#     Svar: Nøglerne er afdelingsnavnene ("IT", "HR", "Salg"), værdierne er antal personer.
# 4b. Første gang en afdeling dukker op, findes den ikke i dict'en. Hvordan klarer din kode det?
#     Svar: afdelinger.get(afd, 0) giver 0, når nøglen mangler, så den første bliver 0 + 1 = 1.
# 4c. Hvilket bogstav er hyppigst i tekst? Hvordan brugte vi den slags optælling i Modul 2?
#     Svar: "e" (6 gange). I Modul 2 sammenlignede vi de hyppigste tegn i chifferteksten med
#           de hyppigste bogstaver i sproget for at gætte substitutionsnøglen.

# ------------------------------------------------------------
# Trin 5 · Skriv din egen funktion (Modul 1)
# ------------------------------------------------------------
overskrift("Trin 5 · Egen funktion: lav_email")


def lav_email(fornavn, efternavn, domaene):
    # TODO: brug lav_logon, og returnér en e-mailadresse som "ahansen@firma.dk"
    return lav_logon(fornavn, efternavn) + "@" + domaene


for p in personer:
    print(f"    {p['fornavn']:<7} {lav_email(p['fornavn'], p['efternavn'], 'firma.dk')}")
# 5a. Hvorfor kalder lav_email lav_logon i stedet for at gentage koden?
#     Svar: Genbrug. Reglerne for logon står ét sted, så en rettelse i lav_logon slår igennem
#           alle steder, og logon og e-mail passer altid sammen.
# 5b. Hvad er forskellen på at returnere værdien og bare printe den inde i funktionen?
#     Svar: return giver værdien tilbage til den, der kaldte, så den kan bruges videre
#           (gemmes, sammenlignes, skrives i en fil). print viser den kun på skærmen.
# 5c. Hvad sker der, hvis du kalder lav_email med domaene "FIRMA.DK"? Er det et problem?
#     Svar: Adressen bliver "ahansen@FIRMA.DK". Domæner er ikke case-sensitive, så den virker,
#           men det er pænest at gøre det ensartet, fx med domaene.lower().


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
print("    __name__ i ex1 :", __name__)
# 6a. Kør tekst_vaerktoej.py direkte (ikke ex1). Hvad ser du?
#     Svar: Selvtesten nederst i modulet kører og viser eksempler på alle funktionerne.
# 6b. Hvorfor kører selvtesten ikke, når ex1 importerer modulet?
#     Svar: Ved import er __name__ i modulet "tekst_vaerktoej", ikke "__main__", så
#           if __name__ == "__main__": er falsk, og selvtesten springes over.
# 6c. Hvad skrev din TODO ud? Hvorfor?
#     Svar: "__main__", fordi ex1 er den fil, du startede.

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
    start = logon
    while logon in brugte:
        logon = start + str(nr)
        nr += 1
    brugte.append(logon)
    print(f"    {p['fornavn']:<7} {logon}")
# 7a. Hvorfor er det en while-løkke og ikke en if?
#     Svar: if prøver kun én gang. Findes ahansen2 også, skal vi prøve igen. while bliver
#           ved, til logon er ledigt.
# 7b. Et logon på 20 tegn får et tal på. Hvilket problem opstår, og hvordan kan det løses?
#     Svar: Det bliver 21 tegn, og AD afviser det. Klip først, fx start[:18] + str(nr).
# 7c. brugte kender kun personerne i listen. Hvad mangler, før logon er unikt i hele AD?
#     Svar: Vi skal også spørge AD, om logon findes. Det gør vi i Sprint 3 og 4.

# ------------------------------------------------------------
# Trin 8 · BONUS · Datoer fra AD
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · Datoer fra AD")
oprettet = ["20240315123045.0Z", "20251201080000.0Z", None]
for vaerdi in oprettet:
    dage = "-"
    # TODO: hvis vaerdi ikke er None, så regn ud hvor mange dage siden datoen er (brug datetime)
    if vaerdi is not None:
        dage = (datetime.now() - datetime.strptime(vaerdi[:8], "%Y%m%d")).days
    print(f"    {str(vaerdi):<20} {ad_dato(vaerdi):<12} dage siden: {dage}")
# 8a. Hvad står de 14 første tegn i "20240315123045.0Z" for?
#     Svar: ÅÅÅÅMMDDttmmss: år 2024, måned 03, dag 15, kl. 12:30:45. Z betyder UTC.
# 8b. Hvorfor skal ad_dato og din kode tåle None?
#     Svar: Mange attributter er ikke sat på alle konti. Uden tjek giver None[:8] TypeError.
# 8c. Hvor brugte vi dage siden en dato i en audit? (Modul 9)
#     Svar: Konti, der ikke har logget på i 90 dage (lastLogonTimestamp) i Modul 9, Sprint 3.

# ------------------------------------------------------------
# Trin 9 · BONUS · Caesar (Modul 2)
# ------------------------------------------------------------
overskrift("Trin 9 · BONUS · Caesar")
alfabet = "abcdefghijklmnopqrstuvwxyz"


def caesar(tekst, flyt):
    resultat = ""
    # TODO: flyt hvert bogstav i tekst flyt pladser frem i alfabet. Andre tegn beholdes.
    #       Husk at z + 1 skal blive til a.
    for tegn in tekst:
        if tegn in alfabet:
            resultat += alfabet[(alfabet.index(tegn) + flyt) % 26]
        else:
            resultat += tegn
    return resultat


hemmelig = caesar("ahansen", 3)
print("    krypteret :", hemmelig)
print("    tilbage   :", caesar(hemmelig, -3))
# 9a. Hvordan sørger din kode for, at z + 1 bliver a?
#     Svar: % 26 (modulo) giver resten ved division med 26, så position 26 bliver 0 igen.
# 9b. Hvorfor kan caesar(..., -3) dekryptere?
#     Svar: Den flytter samme antal pladser tilbage. Med modulo virker negative tal også.
# 9c. Hvor mange forskellige nøgler findes der? Hvad betyder det for sikkerheden?
#     Svar: 25 brugbare nøgler. Man kan prøve dem alle på et øjeblik (brute force),
#           så Caesar beskytter intet.

# ------------------------------------------------------------
# Trin 10 · BONUS · Samlet oversigt
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · Samlet oversigt")
print(f"    {'navn':<32} {'logon':<20} {'afdeling'}")
print("    " + "-" * 62)
# TODO: skriv én linje pr. person med fulde navn, logon og afdeling under overskriften
for p in personer:
    navn = p["fornavn"] + " " + p["efternavn"]
    print(f"    {navn:<32} {lav_logon(p['fornavn'], p['efternavn']):<20} {p['afdeling']}")
# 10a. Hvilke funktioner fra tekst_vaerktoej har du brugt i dag?
#     Svar: overskrift, lav_logon, tael_tegn, kodeord_score og ad_dato (erstat_danske
#           indirekte via lav_logon, og direkte hvis man har prøvet den).
# 10b. Listen personer er skrevet direkte i koden. Hvor ville den komme fra i virkeligheden?
#     Svar: Fra en fil, typisk en CSV-eksport fra HR. Det er emnet i Sprint 2.
