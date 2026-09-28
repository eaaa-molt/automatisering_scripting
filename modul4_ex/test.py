PREFIX = "EAA25"
POSTFIX = "BAAAA.dk"

class Studerende:
    def __init__(self, fnavn, enavn, studieretning, brugernavn, årgang="F2026V"):
        self.fornavn = fnavn
        self.efternavn = enavn
        self.fuldt_navn = f"{fnavn} {enavn}"
        self.studieretning = studieretning
        self.brugernavn = brugernavn
        self.email = f"{PREFIX}{brugernavn}@students.{POSTFIX}"
        self.årgang = årgang

stud1 = Studerende("Omar", "Laila", "CSIK", "OMLA")

print(stud1.email)
print(stud1.årgang)
