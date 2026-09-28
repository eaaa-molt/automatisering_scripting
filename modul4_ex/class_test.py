import subprocess
subprocess.run('clear', shell=True)

studerende = []
class Studerende:
    def __init__(self, fornavn, efternavn, studieretning="CSIK", årgang="F2026V", aktiv=True):
        self.fornavn = fornavn
        self.efternavn = efternavn
        self.fuldtnavn = f"{fornavn} {efternavn}"
        self.studieretning = studieretning
        self.årgang = årgang
        self.aktiv = aktiv

    def __str__(self):
        er_aktiv = "Ja" if self.aktiv else "Nej"
        indent = 15
        return(f"\n==== INFO ====" + 
               f"\n{"Fornavn:":<{indent}}{self.fornavn}" + 
               f"\n{"Efternavn:":<{indent}}{self.efternavn}" +
               f"\n{"Studieretning:":<{indent}}{self.studieretning}" + 
               f"\n{"Årgang:":<{indent}}{self.årgang}" + 
               f"\n{"Aktiv:":<{indent}}{er_aktiv}")

    def tilføj_til_studerende_liste(self):
        studerende.append(self)
    
    def skiftstudieretning(self, ny_studieretning):
        gammel_studieretning = self.studieretning
        self.studieretning = ny_studieretning
        print(f"\n==== SKIFT STUDIERETNING ====" + 
              f"\n{self.fuldtnavn} er nu skiftet fra {gammel_studieretning} til {self.studieretning}")

    def deaktiver_studerende(self):
        if not self.aktiv:
            print(f"{self.fuldtnavn} er allerede deaktiveret!")
            return
        else:
            self.aktiv = False
            print(f"{self.fuldtnavn} er nu deaktiveret")


def opret_studerende():
    fornavn = input("Fornavn: ")
    efternavn = input("Efternavn: ")
    studieretning = input("Studieretning: ")
    årgang = input("Årgang: ")

    kwargs = {}
    if studieretning:
        kwargs["studieretning"] = studieretning
    if årgang:
        kwargs["årgang"] = årgang

    studerende.append(Studerende(fornavn, efternavn, **kwargs))
    print(f"\n==== STUDERENDE OPRETTET ====" + 
          f"\n{fornavn} {efternavn}")

def print_studerende():
    if studerende:
        for stud in studerende:
            print(stud)
    else:
        print("Ingen studerende i listen!")
    
def skift_studieretning():
    if studerende:
        for n, stud in enumerate(studerende, start=1):
            print(n, stud.fuldtnavn)
    else:
        print("Ingen studerende i listen!")


MENU = [
    ("Vis alle studerende", print_studerende),
    ("Opret studerende", opret_studerende),
    ("Skift studieretning", skift_studieretning),
]


def vis_menu():
    print("\n--- Hovedmenu ---")
    for i, (tekst, _) in enumerate(MENU, start=1):
        print(f"  {i}. {tekst}")
    print("  0. Afslut")


def kør_menu():
    while True:
        vis_menu()
        valg = input("\nVælg: ").strip()

        if valg == "0":
            print("Afslutter.")
            break

        if valg.isdigit() and 1 <= int(valg) <= len(MENU):
            _, funktion = MENU[int(valg) - 1]
            funktion()
        else:
            print(f"Ugyldigt valg - indtast 0-{len(MENU)}.")






def main():
    kør_menu()

main()