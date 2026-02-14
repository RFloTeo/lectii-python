import json # necesar pentru a lucra cu json

f = open('lista.json') # deschidem fisier pentru citire
# f contine un obiect care reprezinta un fisier
produse = json.load(f) # f.read() in loc de json.load(f) daca citim doar text din fisier
f.close() # Metoda close inchide fisierul si este necesara dupa un open

total = 0 # aici tinem suma valorilor

for i in produse: # i va lua, pe rand, valoarea fiecarui dictionar din produse
    total += i['cantitate'] * i["pret"]
    # adaugam la total produsul din valorile "cantitate" si "pret" din dictionarul continut de i


print(total)
