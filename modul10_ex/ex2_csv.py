# ============================================================
#  MODUL 10 · Sprint 2 · Øvelse 2 · Filer, CSV og klasser
#  Repeterer: Modul 3 (stier, CSV, fejlhåndtering), Modul 4 (klasser, JSON)
#             og Modul 5 (det hele samlet)
# ============================================================
#  HR har sendt en liste med nye medarbejdere: nye_brugere.csv.
#  Før nogen bliver oprettet i AD, skal listen læses og tjekkes.
#  Værktøjet ligger færdigt i csv_vaerktoej.py. Hav filen åben ved siden af.
#  Scriptet bruger IKKE AD. Det skriver kun filer i din egen mappe.
#
#  Du skal IKKE ændre i modulerne. Alt, du skriver, skriver du i denne fil.
#  Arbejd ét trin ad gangen: udfyld TODO, kør scriptet, svar på spørgsmålene
#  under trinnet. Det er helt fint, at de tidligere trin kører igen.
#
#  Trin 1-5 er kernen. Trin 6-10 er BONUS, hvis du har tid tilbage.
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
#       Tip: hver række er en dict, og kolonnenavnene står i første linje af CSV-filen.
# 1a. Åbn nye_brugere.csv i VS Code. Hvilken linje bliver ikke til en række, og hvorfor?
# 1b. mappe / "nye_brugere.csv" bruger / mellem en Path og en tekst. Hvorfor ikke bare "nye_brugere.csv"?
# 1c. indlaes_csv åbner med encoding="utf-8-sig". Hvad er "sig", og hvem skriver den?

# ------------------------------------------------------------
# Trin 2 · Fejlhåndtering med try og except
# ------------------------------------------------------------
overskrift("Trin 2 · Når filen ikke findes")
mangler = indlaes_csv(mappe / "findes_ikke.csv")
print("    indlaes_csv gav :", mangler)
# TODO: åbn mappe / "findes_ikke.txt" med open() selv, og fang fejlen med try og except,
#       så scriptet skriver "    filen findes ikke" i stedet for at stoppe
# 2a. Hvad står der i terminalen, hvis du fjerner try og except? Hvad hedder fejlen?
# 2b. Find except-linjen i indlaes_csv. Hvorfor returnerer den [] i stedet for at stoppe?
# 2c. Hvorfor er det bedre at fange FileNotFoundError end at skrive bare except:?

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
print("    gyldige  :", len(gyldige))
print("    ugyldige :", len(ugyldige))
# 3a. Hvorfor returnerer valider_raekke en liste med fejl og ikke bare True eller False?
# 3b. Mia Holm står i afdelingen "it". Hvorfor er hun ugyldig? Hvordan kunne man tillade det?
# 3c. Peter Madsen har mellemrum omkring navnet i filen. Er han gyldig? Hvorfor?

# ------------------------------------------------------------
# Trin 4 · Fra dict til objekt (Modul 4)
# ------------------------------------------------------------
overskrift("Trin 4 · Bruger-objekter")
brugere = []
# TODO: lav et Bruger-objekt for hver række i gyldige, og læg det i brugere
for b in brugere:
    print(f"    {b.fulde_navn():<32} {b.logon:<22} {b.afdeling}")
# 4a. Find class Bruger i csv_vaerktoej.py. Hvilke attributter får et objekt i __init__?
# 4b. Hvad er forskellen på b.logon og b.fulde_navn()? Hvorfor har den ene parenteser?
# 4c. Hvor kommer logon fra? Du har ikke givet det med, da du lavede objektet.

# ------------------------------------------------------------
# Trin 5 · Gem resultatet i to CSV-filer
# ------------------------------------------------------------
overskrift("Trin 5 · Gem gyldige og ugyldige")
# TODO: gem brugerne som dicts i mappe / "gyldige.csv" og ugyldige i mappe / "ugyldige.csv"
#       med gem_csv, og skriv antallet ud for hver fil
#       Tip: gem_csv vil have en liste af dicts. Hvad kan et Bruger-objekt give dig?
# 5a. Åbn gyldige.csv. Hvilke kolonner har den, og hvor kommer de fra?
# 5b. Hvorfor kan du ikke give listen brugere direkte til gem_csv?
# 5c. Åbn gyldige.csv i Excel. Står alt i én kolonne? Hvad kan man gøre? (Modul 9)


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
afdelinger_fra_fil = "???"            # TODO: hent listen med afdelinger fra indstillinger
print("    afdelinger fra filen :", afdelinger_fra_fil)
# 6a. Hvilken Python-type bliver JSON-listen til? Og hele filen?
# 6b. Hvorfor er det smart at have afdelinger i en fil i stedet for i koden?
# 6c. Ret indstillinger.json, så "it" også er gyldig. Hvad sker der i Trin 3? Hvorfor?

# ------------------------------------------------------------
# Trin 7 · BONUS · Fejlen som kolonne
# ------------------------------------------------------------
overskrift("Trin 7 · BONUS · Fejlårsag i ugyldige.csv")
med_fejl = []
for r in ugyldige:
    ny = dict(r)
    # TODO: tilføj nøglen "fejl" til ny med fejlene fra valider_raekke samlet til én tekst
#       Tip: "; ".join(en_liste) laver en liste om til én tekst.
    med_fejl.append(ny)
print("    gemt :", gem_csv(med_fejl, mappe / "ugyldige.csv"))
# 7a. Hvorfor laver vi dict(r) i stedet for at ændre r direkte?
# 7b. Hvorfor samler vi fejlene til én tekst i stedet for at gemme listen?

# ------------------------------------------------------------
# Trin 8 · BONUS · Gem og læs som JSON (Modul 5)
# ------------------------------------------------------------
overskrift("Trin 8 · BONUS · brugere.json")
# TODO: gem alle brugere som dicts i mappe / "brugere.json" med gem_json,
#       læs filen igen med indlaes_json, og skriv antal og den første bruger ud
# 8a. Åbn brugere.json. Hvordan ser æ, ø og å ud? Hvad gør ensure_ascii=False i gem_json?
# 8b. Hvornår er JSON bedre end CSV, og omvendt?
# 8c. Kan du gemme selve Bruger-objekterne med gem_json? Prøv. Hvad sker der?

# ------------------------------------------------------------
# Trin 9 · BONUS · Sortér brugerne
# ------------------------------------------------------------
overskrift("Trin 9 · BONUS · Sorteret efter afdeling og efternavn")
# TODO: skriv brugerne ud sorteret efter afdeling og derefter efternavn
#       Tip: sorted() har en key, og key kan returnere flere værdier på én gang.
# 9a. Hvad sammenligner sorted, når key returnerer to værdier?
# 9b. Hvorfor sorteres "Ægidius" sidst blandt IT?

# ------------------------------------------------------------
# Trin 10 · BONUS · Dubletter i filen
# ------------------------------------------------------------
overskrift("Trin 10 · BONUS · Samme logon flere gange")
antal_logon = {}
# TODO: tæl hvor mange gange hvert logon optræder i brugere, og skriv dem ud, der står mere end én gang
# 10a. Hvilket logon står flere gange? Hvilken metode fra Sprint 1 lignede det her?
# 10b. Filen er nu tjekket. Hvad mangler, før vi ved, om logon er ledigt i AD?
