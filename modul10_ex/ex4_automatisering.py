# ============================================================
#  MODUL 10 · Sprint 4 · Øvelse 4 · Fra CSV til AD: find og kald
#  Repeterer: Modul 8 (opret og slet) og alt fra Modul 1-9
# ============================================================
#  Når vi automatiserer, skriver vi ikke alt forfra. Vi genbruger den kode, vi har.
#  Alt, du skal bruge i dag, findes allerede som funktioner i de tre moduler:
#      tekst_vaerktoej.py   csv_vaerktoej.py   ad_vaerktoej.py
#  Øverst i hvert modul står en oversigt over funktionerne.
#
#  I hvert trin gør du tre ting:
#      1. FIND den funktion, der løser opgaven
#      2. KALD den med de rigtige parametre (og importér den øverst i filen)
#      3. VALIDER: skriv en linje, der viser, at det virkede
#
#  Du bygger funktionen main(). Den bestemmer rækkefølgen, modulerne gør arbejdet.
#  Kernen (Trin 1-5) skriver IKKE til AD. Den slutter med et dry run.
#
#  Kræver config_ad.json, nye_brugere.csv og indstillinger.json i samme mappe.
#  Du skal IKKE ændre i modulerne. Kør scriptet efter hvert trin.
#
#  Trin 1-5 er kernen. Trin 6-10 er BONUS, hvis du har tid tilbage.
# ============================================================
from tekst_vaerktoej import overskrift
# TODO: importér de funktioner, du får brug for, efterhånden som du finder dem


def main():
    # --------------------------------------------------------
    # Trin 1 · Forbind til AD
    # --------------------------------------------------------
    overskrift("Trin 1 · Forbind til AD")
    # TODO: forbind til AD med den funktion i ad_vaerktoej, der forbinder. Gem forbindelsen i conn.
    # TODO: skriv en linje, der viser, at du er forbundet, fx:
    #       print("    forbundet    :", conn.bound)
    # 1a. Hvilken funktion valgte du? Hvor fandt du den?
    # 1b. Hvorfor skal forbind() ikke have nogen parametre? Hvor kommer server og adgangskode fra?
    # 1c. Hvad betyder True i din print? Hvad ville der ske, hvis adgangskoden var forkert?

    # --------------------------------------------------------
    # Trin 2 · Indlæs indstillinger og CSV-fil
    # --------------------------------------------------------
    overskrift("Trin 2 · Indlæs filerne")
    # TODO: indlæs indstillinger.json i indstillinger og nye_brugere.csv i raekker.
    #       Begge filer ligger i samme mappe som modulerne.
    # TODO: skriv en linje, der viser, at begge filer er indlæst
    # 2a. Hvilke to funktioner brugte du? Hvorfor ikke den samme til begge filer?
    # 2b. Hvordan fik du stien til filerne? Hvad sker der, hvis du staver et filnavn forkert?
    # 2c. Hvordan ville din valideringslinje afsløre et forkert filnavn?

    # --------------------------------------------------------
    # Trin 3 · Hvilke rækker kan bruges?
    # --------------------------------------------------------
    overskrift("Trin 3 · Valider rækkerne")
    # TODO: del raekker i gyldige brugere og ugyldige rækker. De tilladte afdelinger står i indstillinger.
    # TODO: skriv en linje, der viser antal gyldige og antal ugyldige
    # 3a. Der findes to funktioner med "valider" i navnet. Hvilken valgte du, og hvorfor?
    # 3b. Funktionen returnerer to ting. Hvordan tog du imod dem?
    # 3c. Læs valider_alle i csv_vaerktoej.py. Hvad fra Sprint 2 genkender du?

    # --------------------------------------------------------
    # Trin 4 · Hvem er nye, og hvem findes allerede?
    # --------------------------------------------------------
    overskrift("Trin 4 · Nye og dubletter")
    # TODO: del brugere i nye og dubletter. Søg i hele domænet (det står i indstillinger).
    # TODO: skriv en linje, der viser antal nye og logon på hver dublet
    # 4a. Hvilken base gav du med, og hvorfor ikke OU'en, hvor brugerne skal oprettes?
    # 4b. ahansen er en dublet, men findes ikke i AD. Hvorfor? (Læs docstringen)
    # 4c. Hvorfor valideres rækkerne i Trin 3, FØR vi spørger AD i Trin 4?

    # --------------------------------------------------------
    # Trin 5 · Dry run
    # --------------------------------------------------------
    overskrift("Trin 5 · Dry run")
    # TODO: vis, hvad der VILLE ske, hvis de nye brugere blev oprettet i OU'en fra indstillinger.
    #       Der må IKKE skrives til AD.
    # TODO: skriv en opsummering med antal nye, dubletter og ugyldige
    # 5a. Både opret_bruger og opret_alle kan bruges. Hvilken valgte du, og hvad er forskellen?
    # 5b. Hvilken parameter sikrer, at intet bliver skrevet? Hvad sker der, hvis du udelader den?
    # 5c. Hvordan kan du VALIDERE, at intet blev oprettet i AD?

    # ========================================================
    #  BONUS · Trin 6-8
    #  Gå kun videre, når Trin 1-5 er svaret.
    # ========================================================

    # --------------------------------------------------------
    # Trin 6 · BONUS · Filer til HR og IT
    # --------------------------------------------------------
    overskrift("Trin 6 · BONUS · ugyldige.csv og nye.csv")
    # TODO: gem de ugyldige rækker i ugyldige.csv (til HR) og de nye brugere i nye.csv (til IT),
    #       og vis, hvor mange rækker der blev gemt i hver fil
    # 6a. nye er en liste af Bruger-objekter. Hvorfor kan den ikke gives direkte til gem_csv?
    # 6b. Hvilken kolonne har ugyldige.csv, som nye_brugere.csv ikke har? Hvor kommer den fra?

    # --------------------------------------------------------
    # Trin 7 · BONUS · Gør logon unikt for dig
    # --------------------------------------------------------
    #  Alle studerende har den samme CSV-fil. Før vi skriver til AD, sætter vi dit
    #  logon foran, så "ahansen" fx bliver "stud01.ahansen", og ingen støder sammen.
    overskrift("Trin 7 · BONUS · Præfiks")
    # TODO: sæt dit logon + "." foran logon på alle brugere (begge dele findes som funktioner)
    # TODO: find nye og dubletter igen med de nye logons (som i Trin 4), og vis logon på de nye
    # 7a. Hvorfor skal Trin 4 køres igen efter præfikset?
    # 7b. Hvorfor bliver Clara Christensen-Søndergaards logon kortere end de andres?

    # --------------------------------------------------------
    # Trin 8 · BONUS · Opret i AD for alvor
    # --------------------------------------------------------
    #  Brugerne oprettes deaktiverede (514) i OU=Modul8, som i Modul 8.
    overskrift("Trin 8 · BONUS · Opret i AD")
    skriv_til_ad = "???"          # TODO: sæt til True, når Trin 5 og Trin 7 ser rigtige ud
    if skriv_til_ad == "???":
        print("    Sæt skriv_til_ad i Trin 8. Intet er skrevet til AD.")
        return
    # TODO: opret de nye brugere i AD for alvor
    # 8a. Hvad ændrede du i forhold til Trin 5? Hvordan kan du se i outputtet, at det lykkedes?
    # 8b. Kør hele scriptet igen. Hvad viser Trin 7 nu? Hvorfor er det godt?


def ryd_op():
    # --------------------------------------------------------
    # Trin 9 · BONUS · Ryd op med en ny funktion
    # --------------------------------------------------------
    #  En ny opgave = en ny funktion, der genbruger modulerne.
    #  Kald ryd_op() nederst i filen (se dér).
    overskrift("Trin 9 · BONUS · Slet dine testbrugere")
    # TODO: forbind, find DN på dine egne brugere i OU'en (dit logon + "."), og slet dem.
    #       Kør først med dry run, og se listen igennem, før du sletter for alvor.
    # TODO: valider, at de er væk (søg efter dem igen)
    # 9a. Hvorfor er præfikset vigtigt, når man sletter?
    # 9b. Hvilke funktioner fra main kunne du genbruge, og hvilke var nye?


def kun_tjek(filnavn):
    # --------------------------------------------------------
    # Trin 10 · BONUS · Samme byggeklodser, ny opgave
    # --------------------------------------------------------
    #  HR vil gerne have en fil tjekket UDEN at noget bliver oprettet.
    #  Byg funktionen af de samme kald som i main: forbind, indlæs filnavn, valider,
    #  find nye, og gem de nye i klar_til_oprettelse.csv. Kald den nederst i filen.
    overskrift("Trin 10 · BONUS · Kun tjek af " + str(filnavn))
    # TODO: byg funktionen
    # 10a. Hvor mange linjer skrev du? Hvor mange ville det være uden modulerne?
    # 10b. Hvorfor får funktionen filnavn som parameter i stedet for at bruge nye_brugere.csv?


if __name__ == "__main__":
    main()
    # ryd_op()                              # Trin 9: fjern # foran
    # kun_tjek(mappe / "nye_brugere.csv")   # Trin 10: fjern # foran
