import os

bestandsnaam = "demotekst.txt"

huidige_map = os.getcwd()

volledige_pad = os.path.join(huidige_map, bestandsnaam)
print("dit bestand gaan we hernoemen: " + volledige_pad)

nieuwe_naam = input("Nieuwe bestandsnaam: ")

if len(nieuwe_naam) > 0:
    nieuwe_volledige_pad = os.path.join(huidige_map, nieuwe_naam)
    print("Bestand wordt hernoemd naar: " + nieuwe_volledige_pad)

    os.rename(volledige_pad, nieuwe_volledige_pad)
    print("Bestand hernoemd")
else:
    ("sorry geen geldige invoer, einde programma")

bestand = input("Welk bestand wil je verwijderen: ")

if len(bestand) > 0:
    if os.path.exists(bestand):
        os.remove(bestand)
        print("Het bestand " + bestand + " is verwijderd. Jammer dan.")
    else:
        print("Dit bestand bestaat niet, sorry")
else:
    print('Geen invoer, script zal stoppen')
