import io
import time
bestand = open("klasgenoten.txt", "r")

tekst_regel = bestand.readline()

while tekst_regel:
    tekst_regel = tekst_regel.strip()
    
    print(tekst_regel)

    tekst_regel = bestand.readline()
    time.sleep(0.5)
