from baisc import lirterki, clear, playsound, screen, lirterki_render
import os
class ender_page():
    
    def __init__(self, wygrana, setting):
        clear()
        self.scr = screen()
        self.scr.display_board_from_render(lirterki_render("Koniec", "YELLOW"), 0, 1)
        print()
        if wygrana == True:
            print("Gracz 1:")
            self.scr.display_board_from_render(lirterki_render("Wygrałeś", "GREEN"), 0, 10)
            if bool(setting["sound"]) == True:
                playsound("sounds/Orescue.wav")
        else:
            print("Gracz 1:")
            self.scr.display_board_from_render(lirterki_render("Przegrałeś", "RED"), 0, 11)
            if bool(setting["sound"]) == True:
                playsound("sounds/Burning.wav")
        if os.name != 'nt':
            for x in range(2):
                os.system("pkill -9 aplay" + " > /dev/null 2>&1 &")
        input()
