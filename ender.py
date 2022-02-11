from baisc import lirterki, clear, screen, lirterki_render
import os
class ender_page():
    
    def __init__(self, wygrana):
        clear()
        self.scr = screen()
        self.scr.display_board_from_render(lirterki_render("Koniec", "YELLOW"), 0, 1)
        print()
        if wygrana == True:
            print("Gracz 1:")
            self.scr.display_board_from_render(lirterki_render("Wygrałeś", "GREEN"), 0, 10)
        else:
            print("Gracz 1:")
            self.scr.display_board_from_render(lirterki_render("Przegrałeś", "RED"), 0, 11)
        if os.name != 'nt':
            for x in range(2):
                os.system("pkill -9 aplay")
        input()
