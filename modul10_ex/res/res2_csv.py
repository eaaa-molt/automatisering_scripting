# ============================================================
#  MODUL 10 · Sprint 2 · Løsning 2 · Filer, CSV og klasser
#  Repeterer: Modul 3 (stier, CSV, fejlhåndtering), Modul 4 (klasser, JSON)
#             og Modul 5 (det hele samlet)
# ============================================================
#  Løsningsforslag. Hver opgave (TODO) og hvert spørgsmål står som i
#  øvelsen, med løsningen eller svaret lige under.
# ============================================================
from tekst_vaerktoej import overskrift
from csv_vaerktoej import mappe, indlaes_csv, gem_csv, indlaes_json, gem_json, valider_raekke, Bruger

# ------------------------------------------------------------
# Trin 1 · Læs CSV-filen
# ------------------------------------------------------------
overskrift("Trin 1 · nye_brugere.csv")
raekker = indlaes_csv(mappe / "nye_brugere.csv")
print("    antal rækker :", len(raekker))
# TODO: løb raekker igennem, og skriv fornavn, efternavn og afdeling ud for hver række
for r in raekker:
    print(f"    {r['fornavn']:<8} {r['efternavn']:<25} {r['afdeling']}")
# 1a. Åbn nye_brugere.csv i VS Code. Hvilken linje bliver ikke til en række, og hvorfor?
#     Svar: Første linje (fornavn,efternavn,afdeling,titel). DictReader bruger den som
#           kolonnenavne, altså som nøgler i hver dict.
# 1b. mappe / "nye_brugere.csv" bruger / mellem en Path og en tekst. Hvorfor ikke bare "nye_brugere.csv"?
#     Svar: mappe er mappen, hvor modulet ligger. Så findes filen, uanset hvilken mappe
#           terminalen står i, når scriptet startes (Modul 3).
# 1c. indlaes_csv åbner med encoding="utf-8-sig". Hvad er "sig", og hvem skriver den?
#     Svar: sig er BOM, et usynligt mærke først i filen, som Excel skriver. Med utf-8-sig
#           bliver det fjernet, ellers ville første kolonnenavn hedde "﻿fornavn" (Modul 9).

# ------------------------------------------------------------
# Trin 2 · Fejlhåndtering med try og except
# ------------------------------------------------------------
overskrift("Trin 2 · Når filen ikke findes")
mangler = indlaes_csv(mappe / "findes_ikke.csv")
print("    indlaes_csv gav :", mangler)
# TODO: åbn mappe / "findes_ikke.txt" med open() selv, og fang fejlen med try og except,
#       så scriptet skriver "    filen findes ikke" i stedet for at stoppe
try:
    with open(mappe / "findes_ikke.txt", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("    filen findes ikke")
# 2a. Hvad står der i terminalen, hvis du fjerner try og except? Hvad hedder fejlen?
#     Svar: En Traceback, der slutter med FileNotFoundError: [Errno 2] No such file or directory.
#           Scriptet stopper, og resten af trinene kører ikke.
# 2b. Find except-linjen i indlaes_csv. Hvorfor returnerer den [] i stedet for at stoppe?
#     Svar: Den, der kalder, får altid en liste og kan fortsætte, fx med en løkke, der bare
#           ikke kører. En tom liste har samme type som et rigtigt resultat.
# 2c. Hvorfor er det bedre at fange FileNotFoundError end at skrive bare except:?
#     Svar: except: fanger ALLE fejl, også stavefejl i koden og Ctrl+C. Så skjuler man fejl,
#           man ikke havde forudset. Fang kun den fejl, du ved, hvad du skal gøre ved.

# ------------------------------------------------------------
# Trin 3 · Valider rækkerne
# ------------------------------------------------------------
overskrift("Trin 3 · Gyldige og ugyldige rækker")
afdelinger = ["IT", "HR", "Salg", "Support"]
gyldige = []
ugyldige = []
for r in raekker:
    fejl = valider_raekke(r, afdelinger)
    # TODO: læg rækken i gyldige, hvis fejl er tom, ellers i ugyldige,
    #       og skriv "[UGYLDIG]", navnet og fejl ud for de ugyldige
    if len(fejl) == 0:
        gyldige.append(r)
    else:
        ugyldige.append(r)
        print(f"    [UGYLDIG] {r['fornavn']} {r['efternavn']:<12} {fejl}")
print("    gyldige  :", len(gyldige))
print("    ugyldige :", len(ugyldige))
# 3a. Hvorfor returnerer valider_raekke en liste med fejl og ikke bare True eller False?
#     Svar: Så vi kan se HVORFOR en række er ugyldig, og en række kan have flere fejl på én
#           gang. En tom liste betyder gyldig.
# 3b. Mia Holm står i afdelingen "it". Hvorfor er hun ugyldig? Hvordan kunne man tillade det?
#     Svar: "it" er ikke det samme som "IT", for sammenligning af tekst skelner mellem store
#           og små bogstaver. Man kunne sammenligne med .upper(), men så skal listen også
#           være med store bogstaver (fx "SALG"). Bedre er at få HR til at rette filen.
# 3c. Peter Madsen har mellemrum omkring navnet i filen. Er han gyldig? Hvorfor?
#     Svar: Ja. valider_raekke bruger .strip(), så mellemrum i enderne tæller ikke.

# ------------------------------------------------------------
# Trin 4 · Fra dict til objekt (Modul 4)
# ------------------------------------------------------------
overskrift("Trin 4 · Bruger-objekter")
brugere = []
# TODO: lav et Bruger-objekt for hver række i gyldige, og læg det i brugere
for r in gyldige:
    brugere.append(Bruger(r["fornavn"], r["efternavn"], r["afdeling"], r["titel"]))
for b in brugere:
    print(f"    {b.fulde_navn():<32} {b.logon:<22} {b.afdeling}")
# 4a. Find class Bruger i csv_vaerktoej.py. Hvilke attributter får et objekt i __init__?
#     Svar: fornavn, efternavn, afdeling, titel og logon.
# 4b. Hvad er forskellen på b.logon og b.fulde_navn()? Hvorfor har den ene parenteser?
#     Svar: logon er en attribut (en gemt værdi). fulde_navn er en metode (en funktion på
#           objektet), og den skal kaldes med () for at køre.
# 4c. Hvor kommer logon fra? Du har ikke givet det med, da du lavede objektet.
#     Svar: __init__ kalder lav_logon fra tekst_vaerktoej (Sprint 1). Klassen bruger altså
#           et andet modul, og reglen for logon står stadig kun ét sted.

# ------------------------------------------------------------
# Trin 5 · Gem resultatet i to CSV-filer
# ------------------------------------------------------------
overskrift("Trin 5 · Gem gyldige og ugyldige")
# TODO: gem brugerne som dicts i mappe / "gyldige.csv" og ugyldige i mappe / "ugyldige.csv"
#       med gem_csv, og skriv antallet ud for hver fil
som_dicts = []
for b in brugere:
    som_dicts.append(b.som_dict())
print("    gyldige.csv  :", gem_csv(som_dicts, mappe / "gyldige.csv"))
print("    ugyldige.csv :", gem_csv(ugyldige, mappe / "ugyldige.csv"))
# 5a. Åbn gyldige.csv. Hvilke kolonner har den, og hvor kommer de fra?
#     Svar: logon, fornavn, efternavn, afdeling og titel. De er nøglerne i som_dict(), og
#           gem_csv tager kolonnerne fra den første række.
# 5b. Hvorfor kan du ikke give listen brugere direkte til gem_csv?
#     Svar: DictWriter skal have dicts. Et Bruger-objekt er ikke en dict, så vi bruger
#           som_dict() på hvert objekt først.
# 5c. Åbn gyldige.csv i Excel. Står alt i én kolonne? Hvad kan man gøre? (Modul 9)
#     Svar: Dansk Excel forventer semikolon. Gem med skilletegn=";" eller brug Data,
#           Fra tekst/CSV og vælg komma som afgrænser.


# ============================================================
#  BONUS · Trin 6-10
#  Gå kun videre, når Trin 1-5 er svaret.
# ============================================================

# ------------------------------------------------------------
# Trin 6 · BONUS · Indstillinger fra JSON (Modul 4)
# ------------------------------------------------------------
overskrift("Trin 6 · BONUS · indstillinger.json")
indstillinger = indlaes_json(mappe / "indstillinger.json")
print("    nøgler :", list(indstillinger.keys()))
# TODO: hent listen med afdelinger fra indstillinger
afdelinger_fra_fil = indstillinger["afdelinger"]
print("    afdelinger fra filen :", afdelinger_fra_fil)
# 6a. Hvilken Python-type bliver JSON-listen til? Og hele filen?
#     Svar: En JSON-liste bliver til en list, et JSON-objekt ({ }) bliver til en dict.
# 6b. Hvorfor er det smart at have afdelinger i en fil i stedet for i koden?
#     Svar: Man kan ændre opsætningen uden at røre koden, og samme script kan bruges af flere
#           med hver deres indstillinger (som config_ad.json i Modul 7-9).
# 6c. Ret indstillinger.json, så "it" også er gyldig. Hvad sker der i Trin 3? Hvorfor?
#     Svar: Intet, for Trin 3 bruger stadig listen, der er skrevet i koden. Først når Trin 3
#           bruger afdelinger_fra_fil, slår ændringen igennem. Husk at rette filen tilbage.

# ------------------------------------------------------------
# Trin 7 · BONUS · Fejlen som kolonne
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · Fejlårsag i ugyldige.csv")
med_fejl = []
for r in ugyldige:
    ny = dict(r)
    # TODO: tilføj nøglen "fejl" til ny med fejlene fra valider_raekke samlet til én tekst
    ny["fejl"] = "; ".join(valider_raekke(r, afdelinger))
    med_fejl.append(ny)
print("    gemt :", gem_csv(med_fejl, mappe / "ugyldige.csv"))
# 7a. Hvorfor laver vi dict(r) i stedet for at ændre r direkte?
#     Svar: dict(r) er en kopi. Ændrer vi r, ændrer vi også rækken i listen ugyldige, fordi
#           begge navne peger på samme dict.
# 7b. Hvorfor samler vi fejlene til én tekst i stedet for at gemme listen?
#     Svar: En CSV-celle kan kun rumme én værdi (tekst eller tal), ikke en liste.

# ------------------------------------------------------------
# Trin 8 · BONUS · Gem og læs som JSON (Modul 5)
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · brugere.json")
# TODO: gem alle brugere som dicts i mappe / "brugere.json" med gem_json,
#       læs filen igen med indlaes_json, og skriv antal og den første bruger ud
som_dicts = []
for b in brugere:
    som_dicts.append(b.som_dict())
gem_json(som_dicts, mappe / "brugere.json")
igen = indlaes_json(mappe / "brugere.json")
print("    antal i filen :", len(igen))
print("    første        :", igen[0])
# 8a. Åbn brugere.json. Hvordan ser æ, ø og å ud? Hvad gør ensure_ascii=False i gem_json?
#     Svar: De står som almindelige bogstaver. Uden ensure_ascii=False ville ø stå som ø.
# 8b. Hvornår er JSON bedre end CSV, og omvendt?
#     Svar: JSON kan rumme lister og dicts inde i hinanden og læses direkte tilbage som
#           Python-data. CSV er en flad tabel, som Excel og mennesker læser let.
# 8c. Kan du gemme selve Bruger-objekterne med gem_json? Prøv. Hvad sker der?
#     Svar: Nej. json.dump giver TypeError: Object of type Bruger is not JSON serializable.
#           JSON kender kun dict, list, tekst, tal, True/False og None.

# ------------------------------------------------------------
# Trin 9 · BONUS · Sortér brugerne
# ------------------------------------------------------------
overskrift("Trin 9 · BONUS · Sorteret efter afdeling og efternavn")
# TODO: skriv brugerne ud sorteret efter afdeling og derefter efternavn
for b in sorted(brugere, key=lambda b: (b.afdeling, b.efternavn)):
    print(f"    {b.afdeling:<8} {b.efternavn:<25} {b.fornavn}")
# 9a. Hvad sammenligner sorted, når key returnerer to værdier?
#     Svar: Først den første værdi (afdeling). Kun når den er ens, den næste (efternavn).
# 9b. Hvorfor sorteres "Ægidius" sidst blandt IT?
#     Svar: Python sorterer efter tegnkoder, og Æ har en højere kode end A-Z.

# ------------------------------------------------------------
# Trin 10 · BONUS · Dubletter i filen
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · Samme logon flere gange")
antal_logon = {}
# TODO: tæl hvor mange gange hvert logon optræder i brugere, og skriv dem ud, der står mere end én gang
for b in brugere:
    antal_logon[b.logon] = antal_logon.get(b.logon, 0) + 1
for logon in antal_logon:
    if antal_logon[logon] > 1:
        print(f"    [DUBLET] {logon} står {antal_logon[logon]} gange")
# 10a. Hvilket logon står flere gange? Hvilken metode fra Sprint 1 lignede det her?
#     Svar: ahansen (Anne og Ali Hansen). Samme optælling med en dict som afdelinger og
#           tael_tegn i Sprint 1, Trin 4.
# 10b. Filen er nu tjekket. Hvad mangler, før vi ved, om logon er ledigt i AD?
#     Svar: Vi skal spørge AD, om sAMAccountName allerede findes. Det gør vi i Sprint 3.
