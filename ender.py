from baisc import lirterki, clear
import os
class ender_page():
    
    def __init__(self):
        clear()
        if os.name != 'nt':
            for x in range(2):
                os.system("pkill -9 aplay")
        lirterki("Koniec")