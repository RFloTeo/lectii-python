# Declaram o clasa, ii dam numele:
class Persoana:

  # Constructorul, trebuie sa aiba exact numele asta
  # _ _ init _ _ (fara spatii, doua linii jos inainte si doua dupa)
  def __init__(self, nume, varsta, inaltime):
    # Accesam pentru a modifica sau citi atributele cu self. in interiorul clasei
    self.nume = nume
    self.varsta = varsta
    self.inaltime = inaltime
    self.campionate = 0


  # metodele si constructorul trebuie sa contina self ca primul argument
  def intro(self):
    print(f'Ma numesc {self.nume}, am {self.varsta} ani si inaltimea de {self.inaltime} cm.')
  
  def creste(self):
    self.inaltime += 5

  def win(self):
    self.campionate += 1

nume = input("Cum te cheama? ")
varsta = input("varsta? ")
inaltime = int(input("Inaltime? "))
# cream un obiect cu numele clasei, urmat de paranteze si argumentele constructorului, in afara de self
persoana = Persoana(nume, varsta, inaltime)

persoane = []
persoane.append(persoana)

for aux in range(10):
  nume = input("Cum te cheama? ")
  varsta = input("varsta? ")
  inaltime = int(input("Inaltime? "))
  # cream un obiect cu numele clasei, urmat de paranteze si argumentele constructorului, in afara de self
  persoana = Persoana(nume, varsta, inaltime)

for persoana in persoane:
  # apelam metoda unei clase asupra unui obiect cu punct (.) si numele metodei, urmat de paranteze
  persoana.intro()

