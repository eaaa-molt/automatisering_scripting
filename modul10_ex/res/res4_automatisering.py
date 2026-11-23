# ============================================================
#  MODUL 10 · Sprint 4 · Løsning 4 · Fra CSV til AD: find og kald
#  Repeterer: Modul 8 (opret og slet) og alt fra Modul 1-9
# ============================================================
#  Løsningsforslag. Hver opgave (TODO) og hvert spørgsmål står som i
#  øvelsen, med løsningen eller svaret lige under.
#  OBS: Løsningen SKRIVER til AD i Trin 8 og rydder op igen i Trin 9.
# ============================================================
from tekst_vaerktoej import overskrift
# TODO: importér de funktioner, du får brug for, efterhånden som du finder dem
from csv_vaerktoej import mappe, indlaes_json, indlaes_csv, valider_alle, saet_praefiks, som_dicts, gem_csv
from ad_vaerktoej import forbind, mit_logon, find_nye, opret_alle, find_mine, slet_alle


def main():
    # --------------------------------------------------------
    # Trin 1 · Forbind til AD
    # --------------------------------------------------------
    overskrift("Trin 1 · Forbind til AD")
    # TODO: forbind til AD med den funktion i ad_vaerktoej, der forbinder. Gem forbindelsen i conn.
    conn = forbind()
    # TODO: skriv en linje, der viser, at du er forbundet, fx:
    #       print("    forbundet    :", conn.bound)
    print("    forbundet    :", conn.bound)
    # 1a. Hvilken funktion valgte du? Hvor fandt du den?
    #     Svar: forbind() i ad_vaerktoej. Den står i oversigten øverst i modulet.
    # 1b. Hvorfor skal forbind() ikke have nogen parametre? Hvor kommer server og adgangskode fra?
    #     Svar: Funktionen læser selv config_ad.json. Så skal ingen hemmeligheder stå i koden.
    # 1c. Hvad betyder True i din print? Hvad ville der ske, hvis adgangskoden var forkert?
    #     Svar: True betyder, at login (bind) lykkedes. Med forkert kode når vi aldrig printet:
    #           forbind() skriver "Forbindelsesfejl" og stopper scriptet.

    # --------------------------------------------------------
    # Trin 2 · Indlæs indstillinger og CSV-fil
    # --------------------------------------------------------
    overskrift("Trin 2 · Indlæs filerne")
    # TODO: indlæs indstillinger.json i indstillinger og nye_brugere.csv i raekker.
    #       Begge filer ligger i samme mappe som modulerne.
    indstillinger = indlaes_json(mappe / "indstillinger.json")
    raekker = indlaes_csv(mappe / "nye_brugere.csv")
    # TODO: skriv en linje, der viser, at begge filer er indlæst
    print("    indstillinger:", list(indstillinger.keys()))
    print("    rækker       :", len(raekker))
    # 2a. Hvilke to funktioner brugte du? Hvorfor ikke den samme til begge filer?
    #     Svar: indlaes_json og indlaes_csv fra csv_vaerktoej. Filerne har forskelligt format:
    #           JSON bliver til en dict, CSV til en liste af dicts.
    # 2b. Hvordan fik du stien til filerne? Hvad sker der, hvis du staver et filnavn forkert?
    #     Svar: mappe / "filnavn" (mappe kommer fra csv_vaerktoej). Ved forkert navn skriver
    #           funktionen "Fejl: filen findes ikke" og returnerer en tom liste eller dict.
    # 2c. Hvordan ville din valideringslinje afsløre et forkert filnavn?
    #     Svar: Antallet bliver 0, eller listen med nøgler er tom. Derfor printer vi antal og
    #           ikke bare "OK".

    # --------------------------------------------------------
    # Trin 3 · Hvilke rækker kan bruges?
    # --------------------------------------------------------
    overskrift("Trin 3 · Valider rækkerne")
    # TODO: del raekker i gyldige brugere og ugyldige rækker. De tilladte afdelinger står i indstillinger.
    brugere, ugyldige = valider_alle(raekker, indstillinger["afdelinger"])
    # TODO: skriv en linje, der viser antal gyldige og antal ugyldige
    print("    gyldige      :", len(brugere))
    print("    ugyldige     :", len(ugyldige))
    # 3a. Der findes to funktioner med "valider" i navnet. Hvilken valgte du, og hvorfor?
    #     Svar: valider_alle, fordi den tager hele listen. valider_raekke tjekker kun én række,
    #           så den skulle vi selv have lavet en løkke om (som i Sprint 2, Trin 3).
    # 3b. Funktionen returnerer to ting. Hvordan tog du imod dem?
    #     Svar: brugere, ugyldige = valider_alle(...). Python pakker de to værdier ud i to variabler.
    # 3c. Læs valider_alle i csv_vaerktoej.py. Hvad fra Sprint 2 genkender du?
    #     Svar: Løkken med valider_raekke fra Trin 3, Bruger-objekterne fra Trin 4 og
    #           fejlkolonnen med "; ".join fra Trin 7.

    # --------------------------------------------------------
    # Trin 4 · Hvem er nye, og hvem findes allerede?
    # --------------------------------------------------------
    overskrift("Trin 4 · Nye og dubletter")
    # TODO: del brugere i nye og dubletter. Søg i hele domænet (det står i indstillinger).
    nye, dubletter = find_nye(conn, indstillinger["base"], brugere)
    # TODO: skriv en linje, der viser antal nye og logon på hver dublet
    print("    nye          :", len(nye))
    for b in dubletter:
        print("    [DUBLET]     :", b.logon)
    # 4a. Hvilken base gav du med, og hvorfor ikke OU'en, hvor brugerne skal oprettes?
    #     Svar: Domænet (indstillinger["base"]). sAMAccountName skal være unik i hele domænet,
    #           så en konto i en anden OU blokerer også.
    # 4b. ahansen er en dublet, men findes ikke i AD. Hvorfor? (Læs docstringen)
    #     Svar: Anne og Ali Hansen giver begge ahansen. find_nye husker de logons, den har set
    #           i listen, og den anden bliver en dublet.
    # 4c. Hvorfor valideres rækkerne i Trin 3, FØR vi spørger AD i Trin 4?
    #     Svar: Det kræver ingen forbindelse og er hurtigt. Vi spørger kun AD om rækker, der
    #           overhovedet kan oprettes.

    # --------------------------------------------------------
    # Trin 5 · Dry run
    # --------------------------------------------------------
    overskrift("Trin 5 · Dry run")
    # TODO: vis, hvad der VILLE ske, hvis de nye brugere blev oprettet i OU'en fra indstillinger.
    #       Der må IKKE skrives til AD.
    opret_alle(conn, indstillinger["ou"], nye, dry_run=True)
    # TODO: skriv en opsummering med antal nye, dubletter og ugyldige
    print("    nye          :", len(nye))
    print("    dubletter    :", len(dubletter))
    print("    ugyldige     :", len(ugyldige))
    # 5a. Både opret_bruger og opret_alle kan bruges. Hvilken valgte du, og hvad er forskellen?
    #     Svar: opret_alle tager en liste og kalder opret_bruger for hver. Med opret_bruger
    #           skulle vi selv skrive løkken. Begge giver samme resultat.
    # 5b. Hvilken parameter sikrer, at intet bliver skrevet? Hvad sker der, hvis du udelader den?
    #     Svar: dry_run=True. Udelader man den, er den stadig True, fordi det er standardværdien.
    #           Det er sikkert som standard, og man skal aktivt skrive False.
    # 5c. Hvordan kan du VALIDERE, at intet blev oprettet i AD?
    #     Svar: Kig i OU=Modul8 i ADUC (F5), eller kør scriptet igen: Trin 4 viser stadig de
    #           samme nye brugere. Oprettede brugere ville være blevet dubletter.

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
    print("    ugyldige.csv :", gem_csv(ugyldige, mappe / "ugyldige.csv"))
    print("    nye.csv      :", gem_csv(som_dicts(nye), mappe / "nye.csv"))
    # 6a. nye er en liste af Bruger-objekter. Hvorfor kan den ikke gives direkte til gem_csv?
    #     Svar: gem_csv skal have dicts. som_dicts laver objekterne om til dicts først.
    # 6b. Hvilken kolonne har ugyldige.csv, som nye_brugere.csv ikke har? Hvor kommer den fra?
    #     Svar: fejl. valider_alle tilføjer den til hver ugyldig række.

    # --------------------------------------------------------
    # Trin 7 · BONUS · Gør logon unikt for dig
    # --------------------------------------------------------
    #  Alle studerende har den samme CSV-fil. Før vi skriver til AD, sætter vi dit
    #  logon foran, så "ahansen" fx bliver "stud01.ahansen", og ingen støder sammen.
    overskrift("Trin 7 · BONUS · Præfiks")
    # TODO: sæt dit logon + "." foran logon på alle brugere (begge dele findes som funktioner)
    saet_praefiks(brugere, mit_logon(conn) + ".")
    # TODO: find nye og dubletter igen med de nye logons (som i Trin 4), og vis logon på de nye
    nye, dubletter = find_nye(conn, indstillinger["base"], brugere)
    for b in nye:
        print("    [NY]         :", b.logon)
    # 7a. Hvorfor skal Trin 4 køres igen efter præfikset?
    #     Svar: Det er nye logons. Om stud01.ahansen findes i AD, er et andet spørgsmål end
    #           om ahansen findes.
    # 7b. Hvorfor bliver Clara Christensen-Søndergaards logon kortere end de andres?
    #     Svar: saet_praefiks klipper til 20 tegn, grænsen for sAMAccountName.

    # --------------------------------------------------------
    # Trin 8 · BONUS · Opret i AD for alvor
    # --------------------------------------------------------
    #  Brugerne oprettes deaktiverede (514) i OU=Modul8, som i Modul 8.
    overskrift("Trin 8 · BONUS · Opret i AD")
    # TODO: sæt til True, når Trin 5 og Trin 7 ser rigtige ud
    skriv_til_ad = True
    # TODO: opret de nye brugere i AD for alvor
    opret_alle(conn, indstillinger["ou"], nye, dry_run=False)
    # 8a. Hvad ændrede du i forhold til Trin 5? Hvordan kan du se i outputtet, at det lykkedes?
    #     Svar: Kun dry_run=False. Hver bruger får "[OPRET]" og "result : 0 (success)".
    # 8b. Kør hele scriptet igen. Hvad viser Trin 7 nu? Hvorfor er det godt?
    #     Svar: Ingen nye. Alle er dubletter, fordi de nu findes i AD. Scriptet kan køres
    #           igen uden at lave dobbelte konti (det kaldes idempotent).


def ryd_op():
    # --------------------------------------------------------
    # Trin 9 · BONUS · Ryd op med en ny funktion
    # --------------------------------------------------------
    #  En ny opgave = en ny funktion, der genbruger modulerne.
    #  Kald ryd_op() nederst i filen (se dér).
    overskrift("Trin 9 · BONUS · Slet dine testbrugere")
    # TODO: forbind, find DN på dine egne brugere i OU'en (dit logon + "."), og slet dem.
    #       Kør først med dry run, og se listen igennem, før du sletter for alvor.
    indstillinger = indlaes_json(mappe / "indstillinger.json")
    conn = forbind()
    mine = find_mine(conn, indstillinger["ou"], mit_logon(conn) + ".")
    print("    fundet       :", len(mine))
    slet_alle(conn, mine, dry_run=False)
    # TODO: valider, at de er væk (søg efter dem igen)
    print("    tilbage      :", len(find_mine(conn, indstillinger["ou"], mit_logon(conn) + ".")))
    # 9a. Hvorfor er præfikset vigtigt, når man sletter?
    #     Svar: Uden præfikset ville find_mine også finde andre studerendes brugere, og du
    #           ville slette dem.
    # 9b. Hvilke funktioner fra main kunne du genbruge, og hvilke var nye?
    #     Svar: forbind, indlaes_json og mit_logon er de samme. Nye er find_mine og slet_alle.


def kun_tjek(filnavn):
    # --------------------------------------------------------
    # Trin 10 · BONUS · Samme byggeklodser, ny opgave
    # --------------------------------------------------------
    #  HR vil gerne have en fil tjekket UDEN at noget bliver oprettet.
    #  Byg funktionen af de samme kald som i main: forbind, indlæs filnavn, valider,
    #  find nye, og gem de nye i klar_til_oprettelse.csv. Kald den nederst i filen.
    overskrift("Trin 10 · BONUS · Kun tjek af " + str(filnavn))
    # TODO: byg funktionen
    indstillinger = indlaes_json(mappe / "indstillinger.json")
    conn = forbind()
    brugere, ugyldige = valider_alle(indlaes_csv(filnavn), indstillinger["afdelinger"])
    nye, dubletter = find_nye(conn, indstillinger["base"], brugere)
    print("    gemt         :", gem_csv(som_dicts(nye), mappe / "klar_til_oprettelse.csv"))
    # 10a. Hvor mange linjer skrev du? Hvor mange ville det være uden modulerne?
    #     Svar: Omkring 5. Uden modulerne skulle forbindelse, CSV, validering og AD-søgning
    #           skrives forfra. Det er pointen med at genbruge.
    # 10b. Hvorfor får funktionen filnavn som parameter i stedet for at bruge nye_brugere.csv?
    #     Svar: Så den kan tjekke enhver fil, HR sender. Samme funktion, nye data.


if __name__ == "__main__":
    main()
    kun_tjek(mappe / "nye_brugere.csv")     # Trin 10
    ryd_op()                                # Trin 9: til sidst, så AD er som før
