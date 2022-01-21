from baisc import lirterki, clear

class ender_page():
    
    def __init__(self, wygrana):
        clear()
        lirterki("Koniec")
        print("\n")
        if wygrana == True:
            print("Wygrałeś")
        else:
            print("Przegrałeś")