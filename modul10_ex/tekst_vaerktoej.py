"""
MODUL 10 · tekst_vaerktoej · færdige funktioner til tekst
Du skal IKKE ændre noget i denne fil. Du bruger den fra dine egne scripts:

    from tekst_vaerktoej import lav_logon

Funktionerne bygger på det, du har lavet i Modul 1 og Modul 2:

  overskrift(tekst)                  skriver en tydelig overskrift over hvert trin
  erstat_danske(tekst)               æ, ø, å bliver til ae, oe, aa (en substitutionstabel)
  lav_logon(fornavn, efternavn)      laver et logon (sAMAccountName) ud fra et navn
  tael_tegn(tekst)                   tæller hvor mange gange hvert tegn optræder
  kodeord_score(kodeord)             giver et kodeord 0-5 point
  ad_dato(vaerdi)                    viser en AD-dato som DD.MM.ÅÅÅÅ
"""

from datetime import datetime

# Substitutionstabel: hvert tegn til venstre erstattes af teksten til højre.
danske_bogstaver = {
    "æ": "ae", "ø": "oe", "å": "aa",
    "Æ": "Ae", "Ø": "Oe", "Å": "Aa",
}


def overskrift(tekst):
    """Skriv en overskrift med streger over og under, så trinene er lette at skelne."""
    print()
    print("=" * 65)
    print("  " + tekst)
    print("=" * 65)


def erstat_danske(tekst):
    """Returnér tekst, hvor æ, ø og å er erstattet med ae, oe og aa."""
    resultat = ""
    for tegn in tekst:
        resultat += danske_bogstaver.get(tegn, tegn)
    return resultat


def lav_logon(fornavn, efternavn, maks=20):
    """Returnér et logon: første bogstav i fornavn + efternavn, små bogstaver,
    uden mellemrum og bindestreg, uden æøå og højst maks tegn langt."""
    logon = fornavn.strip()[0] + efternavn.strip()
    logon = logon.lower().replace(" ", "").replace("-", "")
    logon = erstat_danske(logon)
    return logon[:maks]


def tael_tegn(tekst):
    """Returnér en dict med hvor mange gange hvert tegn optræder, fx {'a': 3, 'n': 2}."""
    antal = {}
    for tegn in tekst:
        antal[tegn] = antal.get(tegn, 0) + 1
    return antal


def kodeord_score(kodeord):
    """Returnér 0-5 point: ét point for hvert opfyldt krav (som i Modul 1)."""
    har_stort = False
    har_lille = False
    har_ciffer = False
    har_special = False
    for tegn in kodeord:
        if tegn.isupper():
            har_stort = True
        elif tegn.islower():
            har_lille = True
        elif tegn.isdigit():
            har_ciffer = True
        else:
            har_special = True
    score = 0
    if len(kodeord) >= 12:
        score += 1
    if har_stort:
        score += 1
    if har_lille:
        score += 1
    if har_ciffer:
        score += 1
    if har_special:
        score += 1
    return score


def ad_dato(vaerdi):
    """Returnér en AD-dato som DD.MM.ÅÅÅÅ.
    vaerdi kan være tekst som "20240315123045.0Z" eller et datetime-objekt.
    Mangler datoen, returneres "-"."""
    if vaerdi is None or vaerdi == "":
        return "-"
    if isinstance(vaerdi, str):
        vaerdi = datetime.strptime(vaerdi[:8], "%Y%m%d")
    return vaerdi.strftime("%d.%m.%Y")


# Selvtest: kører KUN når du starter denne fil direkte, ikke når den importeres.
if __name__ == "__main__":
    overskrift("Selvtest af tekst_vaerktoej")
    print("    erstat_danske('Søren Ærø')   :", erstat_danske("Søren Ærø"))
    print("    lav_logon('Anne', 'Hansen')  :", lav_logon("Anne", "Hansen"))
    print("    tael_tegn('banan')           :", tael_tegn("banan"))
    print("    kodeord_score('Sommer2026!') :", kodeord_score("Sommer2026!"))
    print("    ad_dato('20240315123045.0Z') :", ad_dato("20240315123045.0Z"))
