"""
=============================================================
  MODUL 5  ·  Sprint 3  ·  Ekstraopgaver
  JSON og klasser
=============================================================
Disse opgaver bygger videre på øvelse 3.
Bruger-klassen herunder er en færdig version med de metoder
du implementerede i øvelse 3 — plus et stub til opgave 5.
=============================================================
"""

import json
from pathlib import Path

MAPPE = Path(__file__).parent


class Bruger:
    # __init__, __str__ og til_dict er givet og færdige.
    # Din opgave er at tilføje logonnavn() — se opgave 5 nedenfor.

    def __init__(self, fornavn, efternavn, afdeling):
        self.fornavn   = fornavn
        self.efternavn = efternavn
        self.afdeling  = afdeling

    def __str__(self):
        return f"{self.fornavn} {self.efternavn} ({self.afdeling})"

    def til_dict(self):
        return {
            "fornavn":   self.fornavn,
            "efternavn": self.efternavn,
            "afdeling":  self.afdeling,
        }

    # ── Opgave 5 ──────────────────────────────────────────
    # Tilføj metoden logonnavn(self) til klassen.
    #
    # Den skal returnere "fornavn.efternavn" i lowercase
    # med æ→ae, ø→oe, å→aa (og de store varianter).
    #
    # Eksempler:
    #   Bruger("Maria", "Hansen", "IT")    →  "maria.hansen"
    #   Bruger("Åse", "Dalgaard", "Led")   →  "aase.dalgaard"
    #
    # Hint: definér en lokal def normaliser(s) inde i metoden

    def logonnavn(self):
        # TODO: normaliser fornavn og efternavn (æ/ø/å → ae/oe/aa)
        # TODO: returnér "fornavn.efternavn"
        return ""   # erstat denne linje


# ── Opgave 6 ──────────────────────────────────────────────
# flet_filer(stier, udsti)
#
# Indlæs JSON fra alle filer i listen stier.
# Flet dem til én liste — spring dubletter over.
# En dublet er to poster med samme fornavn OG efternavn.
# Gem den flettede liste til udsti.
# Returnér antal unikke poster.
#
# Hint: fang FileNotFoundError for hver enkelt sti og spring den over
# Hint: brug en liste af sete (fornavn, efternavn)-tupler

def flet_filer(stier, udsti):
    # TODO: gå stier igennem og indlæs JSON fra hver fil
    # TODO: spring over dubletter (samme fornavn + efternavn)
    # TODO: gem den flettede liste til udsti
    # TODO: returnér antal unikke poster
    return 0   # erstat denne linje


# ─────────────────────────────────────────────────────────
def main():
    b1 = Bruger("Maria", "Hansen", "IT")
    b2 = Bruger("Jonas", "Nielsen", "HR")
    b3 = Bruger("Åse", "Dalgaard", "Ledelse")

    print("=== Opgave 5: logonnavn() ===")
    print(b1.logonnavn())   # → maria.hansen
    print(b2.logonnavn())   # → jonas.nielsen
    print(b3.logonnavn())   # → aase.dalgaard

    print("\n=== Opgave 6: flet_filer ===")
    sti_a = MAPPE / "hold_a.json"
    sti_b = MAPPE / "hold_b.json"
    with open(sti_a, "w", encoding="utf-8") as f:
        json.dump([b1.til_dict(), b2.til_dict()], f, indent=2, ensure_ascii=False)
    with open(sti_b, "w", encoding="utf-8") as f:
        json.dump([b2.til_dict(), b3.til_dict()], f, indent=2, ensure_ascii=False)

    n = flet_filer([sti_a, sti_b], MAPPE / "hold_samlet.json")
    print(f"Unikke brugere i flettet fil: {n}")   # → 3

    n_mangler = flet_filer([MAPPE / "mangler.json"], MAPPE / "ud.json")
    print(f"Manglende fil: {n_mangler}")           # → 0


if __name__ == "__main__":
    main()
