from asyncio.base_tasks import _task_get_stack
import io
import os
import time
bestand = open("klasgenoten.txt", "r")

tekst_regel = bestand.readline()

while tekst_regel:
    tekst_regel = tekst_regel.strip()
    print(tekst_regel)
    
    
    lengte_mapnaam = len(tekst_regel)

    if lengte_mapnaam > 0:
        os.mkdir(tekst_regel)
    tekst_regel = bestand.readline()