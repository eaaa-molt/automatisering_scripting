"""
MODUL 10 · csv_vaerktoej · færdige funktioner til filer, CSV og JSON
Du skal IKKE ændre noget i denne fil. Du bruger den fra dine egne scripts:

    from csv_vaerktoej import indlaes_csv

Funktionerne bygger på det, du har lavet i Modul 3, 4 og 5:

  mappe                              mappen, som denne fil ligger i (en Path)
  indlaes_csv(filnavn)               læser en CSV-fil og returnerer en liste af dicts
  gem_csv(raekker, filnavn)          skriver en liste af dicts til en CSV-fil
  indlaes_json(filnavn)              læser en JSON-fil og returnerer indholdet
  gem_json(data, filnavn)            skriver data til en JSON-fil
  valider_raekke(raekke, afdelinger) returnerer en liste med fejl i én CSV-række
  valider_alle(raekker, afdelinger)  deler rækkerne i Bruger-objekter og ugyldige rækker
  saet_praefiks(brugere, praefiks)   sætter praefiks foran logon på alle brugere
  som_dicts(brugere)                 laver en liste af Bruger-objekter om til dicts
  Bruger(fornavn, efternavn, afdeling, titel)
                                     en klasse for én ny bruger
"""

import csv
import json
from pathlib import Path

from tekst_vaerktoej import lav_logon

mappe = Path(__file__).parent


def indlaes_csv(filnavn, skilletegn=","):
    """Læs en CSV-fil og returnér en liste af dicts (én dict pr. række).
    Findes filen ikke, skrives en besked, og der returneres en tom liste."""
    try:
        with open(filnavn, encoding="utf-8-sig", newline="") as f:
            return list(csv.DictReader(f, delimiter=skilletegn))
    except FileNotFoundError:
        print(f"    Fejl: filen findes ikke: {filnavn}")
        return []


def gem_csv(raekker, filnavn, skilletegn=","):
    """Skriv en liste af dicts til en CSV-fil. Kolonnerne tages fra den første række.
    Returnér antal skrevne rækker."""
    if len(raekker) == 0:
        print(f"    Intet at gemme i {filnavn}")
        return 0
    with open(filnavn, "w", encoding="utf-8-sig", newline="") as f:
        skriver = csv.DictWriter(f, fieldnames=list(raekker[0].keys()), delimiter=skilletegn)
        skriver.writeheader()
        skriver.writerows(raekker)
    return len(raekker)


def indlaes_json(filnavn):
    """Læs en JSON-fil og returnér indholdet (typisk en dict eller en liste).
    Findes filen ikke, skrives en besked, og der returneres en tom dict."""
    try:
        with open(filnavn, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"    Fejl: filen findes ikke: {filnavn}")
        return {}


def gem_json(data, filnavn):
    """Skriv data (dict, liste, tekst og tal) til en JSON-fil med pæne indrykninger."""
    with open(filnavn, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def valider_raekke(raekke, afdelinger):
    """Returnér en liste med fejl i rækken. En tom liste betyder, at rækken er gyldig."""
    fejl = []
    if raekke["fornavn"].strip() == "":
        fejl.append("mangler fornavn")
    if raekke["efternavn"].strip() == "":
        fejl.append("mangler efternavn")
    if raekke["afdeling"].strip() not in afdelinger:
        fejl.append("ukendt afdeling: " + raekke["afdeling"])
    return fejl


def valider_alle(raekker, afdelinger):
    """Valider alle rækker og returnér to lister: brugere, ugyldige
    brugere  = Bruger-objekter for de gyldige rækker
    ugyldige = de ugyldige rækker (dicts) med en ekstra nøgle "fejl"."""
    brugere = []
    ugyldige = []
    for r in raekker:
        fejl = valider_raekke(r, afdelinger)
        if len(fejl) == 0:
            brugere.append(Bruger(r["fornavn"], r["efternavn"], r["afdeling"], r["titel"]))
        else:
            ny = dict(r)
            ny["fejl"] = "; ".join(fejl)
            ugyldige.append(ny)
    return brugere, ugyldige


def saet_praefiks(brugere, praefiks):
    """Sæt praefiks foran logon på hver bruger (højst 20 tegn i alt). Returnér listen."""
    for b in brugere:
        b.logon = (praefiks + b.logon)[:20]
    return brugere


def som_dicts(brugere):
    """Returnér en liste med hver Bruger som dict (til gem_csv eller gem_json)."""
    resultat = []
    for b in brugere:
        resultat.append(b.som_dict())
    return resultat


class Bruger:
    """Én ny bruger, der skal oprettes. logon laves automatisk ud fra navnet."""

    def __init__(self, fornavn, efternavn, afdeling, titel=""):
        self.fornavn = fornavn.strip()
        self.efternavn = efternavn.strip()
        self.afdeling = afdeling.strip()
        self.titel = titel.strip()
        self.logon = lav_logon(self.fornavn, self.efternavn)

    def fulde_navn(self):
        """Returnér fornavn og efternavn med mellemrum imellem."""
        return self.fornavn + " " + self.efternavn

    def som_dict(self):
        """Returnér brugeren som en dict, så den kan gemmes i CSV eller JSON."""
        return {"logon": self.logon, "fornavn": self.fornavn, "efternavn": self.efternavn,
                "afdeling": self.afdeling, "titel": self.titel}


# Selvtest: kører KUN når du starter denne fil direkte, ikke når den importeres.
if __name__ == "__main__":
    from tekst_vaerktoej import overskrift
    overskrift("Selvtest af csv_vaerktoej")
    raekker = indlaes_csv(mappe / "nye_brugere.csv")
    print("    rækker i nye_brugere.csv :", len(raekker))
    print("    første række             :", raekker[0] if raekker else "-")
    print("    valider_raekke           :", valider_raekke({"fornavn": "", "efternavn": "Lund",
                                                            "afdeling": "Marked"}, ["IT"]))
    b = Bruger(" Anne ", "Hansen", "IT", "Udvikler")
    print("    Bruger                   :", b.fulde_navn(), "/", b.logon)
    print("    som_dict                 :", b.som_dict())
