# ============================================================
#  LEKTION 7  ·  Sprint 2  ·  Øvelse 2
#  Læs og udforsk brugere fra AD
# ============================================================
#
#  Kræver: config_ad.json i samme mappe (kopiér template-filen)
#  Forbindelsen klares af ad_hjaelp.py - den skal du ikke røre.
#
#  DIN OPGAVE:
#    Opgave 1  kør og observér - eksemplet på conn.search()
#    Opgave 2  skriv én linje i tælle-løkken
#    Opgave 3  skriv en søgning + UAC-tjekket
#    Opgave 4  skriv en søgning efter én bestemt bruger
#    BONUS     kør og observér
#    Svar på observationsopgaverne i bunden af output.
#
# ============================================================

from ldap3 import SUBTREE
from ad_hjaelp import forbind, tekst, vis_brugere

conn, AD_BASE_DN = forbind()
BRUGERE_OU = f"OU=Brugere,OU=Testdata,{AD_BASE_DN}"


# ── Opgave 1 · Alle brugere (eksempel - kør og observér) ─

conn.search(
    search_base   = BRUGERE_OU,
    search_filter = "(objectClass=user)",
    search_scope  = SUBTREE,
    attributes    = ["sAMAccountName", "department", "title"],
)
vis_brugere(conn.entries, "Opgave 1 · Alle brugere i Testdata")


# ── Opgave 2 · Tæl brugere pr. afdeling ──────────────────

print("\n" + "=" * 65)
print("  Opgave 2 · Antal brugere pr. afdeling")
print("=" * 65)

taeller = {}
for entry in conn.entries:              # brugerne fra Opgave 1
    afd = tekst(entry, "department") or "(ingen afdeling)"
    # TODO: læg 1 til taeller[afd]  (brug taeller.get(afd, 0))
    pass

for afd, antal in sorted(taeller.items()):
    print(f"  {afd:<20} {antal} bruger(e)")
print(f"  Total: {sum(taeller.values())}")


# ── Opgave 3 · Aktive og deaktiverede konti ──────────────

print("\n" + "=" * 65)
print("  Opgave 3 · Aktive og deaktiverede konti")
print("=" * 65)
print("  userAccountControl: 66048 = aktiv, 66050 = deaktiveret")
print("  Forskellen er bit 2 (66050 = 66048 + 2)")

# TODO: skriv conn.search(...) som i Opgave 1, men hent
#       attributterne "sAMAccountName" og "userAccountControl"


# ── Rør ikke herunder ─────────────────────────────────────
if conn.entries and "userAccountControl" in conn.entries[0]:
    aktive = 0
    for entry in conn.entries:
        uac = int(tekst(entry, "userAccountControl"))

        # TODO: sæt deaktiveret til True, hvis bit 2 er sat
        #       Hint: uac & 2 er 2, hvis bitten er sat, ellers 0
        deaktiveret = False

        status = "DEAKTIVERET" if deaktiveret else "aktiv"
        if not deaktiveret:
            aktive += 1
        print(f"  {tekst(entry, 'sAMAccountName'):<26} {uac:<8} {status}")
    print(f"\n  Aktive: {aktive}   Deaktiverede: {len(conn.entries) - aktive}")
else:
    print("  Opgave 3: søgningen mangler eller henter ikke userAccountControl.")


# ── Opgave 4 · Alle attributter for thomas.bjerregaard ───

print("\n" + "=" * 65)
print("  Opgave 4 · Alle attributter for thomas.bjerregaard")
print("=" * 65)

# TODO: skriv conn.search(...) der søger i AD_BASE_DN
#       med filteret  (sAMAccountName=thomas.bjerregaard)
#       og attributes=["*"]   (* = alle attributter)


# ── Rør ikke herunder ─────────────────────────────────────
thomas = [e for e in conn.entries
          if tekst(e, "sAMAccountName") == "thomas.bjerregaard"]
if thomas and "whenCreated" in thomas[0]:
    print(f"  Fuldt DN: {thomas[0].entry_dn}\n")
    for navn, vaerdi in sorted(thomas[0].entry_attributes_as_dict.items()):
        if vaerdi:
            print(f"  {navn:<28} {', '.join(str(v) for v in vaerdi)}")
else:
    print("  Opgave 4: søgningen mangler, eller den henter ikke alle attributter.")


# ── BONUS · Brugere med æ, ø eller å (kør og observér) ───

print("\n" + "=" * 65)
print("  BONUS · Brugere med æ, ø eller å i fuldt navn")
print("=" * 65)

conn.search(BRUGERE_OU, "(objectClass=user)", SUBTREE,
            attributes=["sAMAccountName", "cn"])
for entry in conn.entries:
    navn = tekst(entry, "cn")
    if any(c in navn.lower() for c in "æøå"):
        print(f"  {navn:<28} {tekst(entry, 'sAMAccountName')}")

conn.unbind()


# ============================================================
#  Observationsopgaver
# ============================================================

print("\n" + "=" * 65)
print("  Observationsopgaver - brug output + ADUC til at svare")
print("=" * 65)
print("Opgave 1:")
print("  A. Hvor mange brugere er der? Tæl i ADUC under")
print("     OU=Testdata → OU=Brugere. Stemmer det?")
print("  B. Hvad står der i conn.search() - hvad gør hver parameter?")
print("Opgave 2:")
print("  A. Hvilken afdeling har flest brugere?")
print("  B. Hvem har '(ingen afdeling)'? Er feltet tomt i ADUC?")
print("Opgave 3:")
print("  A. Hvor mange er deaktiverede? Hvem?")
print("  B. Find dem i ADUC → Properties → Account.")
print("     Er 'Account is disabled' markeret?")
print("  C. Kunne du se forskel på aktive og deaktiverede i Opgave 1?")
print("Opgave 4:")
print("  A. Find memberOf - stemmer det med Member Of-fanen i ADUC?")
print("  B. Find whenCreated - hvornår blev kontoen oprettet?")
print("  C. Hvorfor er der langt færre attributter end i AD-skemaet?")
print("BONUS:")
print("  A. Kig på Søndergaard og Thøgersen - hvad er logonnavnet?")
print("     Hvad er reglen for æ, ø og å?")
print("=" * 65)
