import baisc
import ender
import starter    
import game
import multiprocessing

def radio():
    while True:
        baisc.playsound("escape.wav")
        baisc.playsound("nave.wav")


if __name__ == '__main__':
    t1 = multiprocessing.Process(target=radio, daemon= True)
    t1.start()
    prosses = starter.starter_page()
    gra = game.game()
    wygrana = gra.start()
    t1.terminate()
    end = ender.ender_page(wygrana)