import os

huidige_map = os.getcwd()
alle_bestanden = os.scandir(huidige_map)

print("Inhoudsopgave van de map: " + huidige_map)
for bestand in alle_bestanden:

    if bestand.is_file():
        print(bestand.name + " (BESTAND)")
    elif bestand.is_dir():
        print(bestand.name + " (MAP)")
    else:
        print(bestand.name + " (ONBEKEND TYPE")