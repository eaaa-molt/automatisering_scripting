# ============================================================
#  LEKTION 7  ·  Sprint 4  ·  Øvelse 4 · LØSNINGSFORSLAG
#  Grupper - member og memberOf
# ============================================================
#
#  To spørgsmål går igen hele tiden i det virkelige AD-liv:
#
#    A) Hvem er MED i en gruppe?    → member   (læses på gruppen)
#    B) Hvilke grupper er nogen i?  → memberOf (læses på brugeren)
#
#  Kræver: config_ad.json i samme mappe (kopiér template-filen)
#  Forbindelsen klares af ad_hjaelp.py - den skal du ikke røre.
#
#  DIN OPGAVE:
#    Opgave 1  kør og observér - alle grupper
#    Opgave 2  skriv søgningen efter member på GRP_IT_Admins
#    Opgave 3  skriv søgningen efter memberOf på thomas.bjerregaard
#    Opgave 4  skriv filter + attribut for nanna.vestergaard
#    BONUS     kør og observér
#    Svar på observationsopgaverne i bunden af output.
#
# ============================================================

from ldap3 import SUBTREE, BASE
from ad_hjaelp import forbind, tekst, kort_navn

conn, AD_BASE_DN = forbind()
GRUPPER_OU = f"OU=Grupper,OU=Testdata,{AD_BASE_DN}"


def medlemmer(entry, attribut):
    """Returnér en liste af DN'er fra member eller memberOf."""
    if attribut in entry and entry[attribut].values:
        return list(entry[attribut].values)
    return []


# ── Opgave 1 · Alle grupper (eksempel - kør og observér) ─

print("=" * 65)
print("  Opgave 1 · Alle grupper i Testdata")
print("=" * 65)

conn.search(
    search_base   = GRUPPER_OU,
    search_filter = "(objectClass=group)",
    search_scope  = SUBTREE,
    attributes    = ["cn", "groupType", "member"],
)

print(f"  {'Gruppenavn':<26} {'Type':<14} {'groupType':<13} Medlemmer")
for grp in conn.entries:
    gt = int(tekst(grp, "groupType"))
    # Bit 0x80000000 = sikkerhedsgruppe. Er den sat, er tallet negativt.
    gruppetype = "Security" if gt < 0 else "Distribution"
    print(f"  {tekst(grp, 'cn'):<26} {gruppetype:<14} {gt:<13} "
          f"{len(medlemmer(grp, 'member'))}")


# ── Opgave 2 · member: hvem er med i GRP_IT_Admins? ──────

print("\n" + "=" * 65)
print("  Opgave 2 · member - hvem er med i GRP_IT_Admins?")
print("=" * 65)

conn.search(
    search_base   = GRUPPER_OU,
    search_filter = "(cn=GRP_IT_Admins)",
    search_scope  = SUBTREE,
    attributes    = ["member"],
)


# ── Rør ikke herunder ─────────────────────────────────────
grp = [e for e in conn.entries if e.entry_dn.startswith("CN=GRP_IT_Admins,")]
if len(conn.entries) == 1 and grp:
    for dn in sorted(medlemmer(grp[0], "member")):
        print(f"  · {kort_navn(dn):<24} {dn}")
else:
    print("  Opgave 2: søgningen mangler eller finder ikke kun GRP_IT_Admins.")


# ── Opgave 3 · memberOf: hvilke grupper er thomas i? ─────

print("\n" + "=" * 65)
print("  Opgave 3 · memberOf - thomas.bjerregaards grupper")
print("=" * 65)

conn.search(
    search_base   = AD_BASE_DN,
    search_filter = "(sAMAccountName=thomas.bjerregaard)",
    search_scope  = SUBTREE,
    attributes    = ["memberOf"],
)


# ── Rør ikke herunder ─────────────────────────────────────
thomas_grupper = set()
if conn.entries and conn.entries[0].entry_dn.startswith("CN=Thomas Bjerregaard,"):
    thomas_grupper = {kort_navn(dn) for dn in medlemmer(conn.entries[0], "memberOf")}
    for g in sorted(thomas_grupper):
        print(f"  · {g}")
else:
    print("  Opgave 3: søgningen mangler eller finder ikke thomas.bjerregaard.")


# ── Opgave 4 · Din tur: nanna.vestergaards grupper ───────

print("\n" + "=" * 65)
print("  Opgave 4 · nanna.vestergaards grupper")
print("=" * 65)

bruger_filter = "(sAMAccountName=nanna.vestergaard)"

bruger_attr = "memberOf"


# ── Rør ikke herunder ─────────────────────────────────────
if bruger_filter and bruger_attr:
    conn.search(AD_BASE_DN, bruger_filter, SUBTREE, attributes=[bruger_attr])
    if conn.entries:
        nanna = {kort_navn(dn) for dn in medlemmer(conn.entries[0], bruger_attr)}
        for g in sorted(nanna):
            print(f"  · {g}")
        print(f"\n  Begge er med i  : {', '.join(sorted(nanna & thomas_grupper)) or '-'}")
        print(f"  Kun Nanna       : {', '.join(sorted(nanna - thomas_grupper)) or '-'}")
        print(f"  Kun Thomas      : {', '.join(sorted(thomas_grupper - nanna)) or '-'}")
    else:
        print("  Ingen bruger fundet - tjek filteret.")
else:
    print("  Opgave 4: bruger_filter og/eller bruger_attr er ikke udfyldt.")


# ── BONUS · GRP_Projekt_Alpha på tværs af afdelinger ─────

print("\n" + "=" * 65)
print("  BONUS · GRP_Projekt_Alpha - fra hvilke afdelinger?")
print("=" * 65)

conn.search(GRUPPER_OU, "(cn=GRP_Projekt_Alpha)", SUBTREE, attributes=["member"])
projekt_dns = medlemmer(conn.entries[0], "member") if conn.entries else []
for dn in sorted(projekt_dns):
    # Slå hver bruger op via sit DN for at se afdelingen
    conn.search(dn, "(objectClass=user)", attributes=["sAMAccountName", "department"],
                search_scope=BASE)
    if conn.entries:
        u = conn.entries[0]
        print(f"  · {tekst(u, 'sAMAccountName'):<26} {tekst(u, 'department') or '(ingen)'}")

conn.unbind()


# ============================================================
#  Observationsopgaver
# ============================================================

print("\n" + "=" * 65)
print("  Observationsopgaver - sammenlign med ADUC")
print("=" * 65)
print("Opgave 1:")
print("  A. Ser du det samme antal grupper i ADUC → OU=Grupper?")
print("  B. Hvad er groupType for GRP_IT og for DL_IT?")
print("     Hvorfor er det ene tal negativt?")
print("  C. GRP_IT og DL_IT har samme medlemmer. Hvad kan GRP_IT")
print("     bruges til, som DL_IT ikke kan?")
print("Opgave 2:")
print("  A. Åbn GRP_IT_Admins → Members. Stemmer listen?")
print("Opgave 3:")
print("  A. Åbn thomas.bjerregaard → Member Of. Stemmer listen?")
print("  B. member og memberOf er to sider af samme sag.")
print("     Hvornår vil du bruge det ene frem for det andet?")
print("Opgave 4:")
print("  A. Hvilke grupper har Nanna, som Thomas ikke har?")
print("     Hvad fortæller det om deres roller?")
print("  B. Prøv en anden bruger, fx rikke.svenningsen.")
print("     Er deaktiverede konti stadig med i grupper?")
print("BONUS:")
print("  A. Er GRP_Projekt_Alpha sammensat på tværs af afdelinger?")
print("=" * 65)
