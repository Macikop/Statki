import baisc
import ender
import starter
import game
import threading

def radio():
    while True:
        baisc.playsound("nave.wav")
        baisc.playsound("escape.wav")

if __name__ == '__main__':
    t1 = threading.Thread(target=radio, daemon=True)
    t1.start()
    prosses = starter.starter_page()
    gra = game.game()
    end = ender.ender_page()