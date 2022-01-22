from baisc import lirterki, clear
import os
class ender_page():
    
    def __init__(self, wygrana):
        clear()
        #lirterki("Koniec")
        #print("\n")
        if wygrana == True:
            lirterki("Wygrales")
        else:
            lirterki("Przegrales")
        if os.name != 'nt':
            for x in range(2):
                os.system("pkill -9 aplay")
        #lirterki("Koniec")
