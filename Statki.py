from baisc import clear, lirterki, wait, colors, display, playsound
import starter
import game
import threading

def radio():
    while True:
        playsound("nave.wav")
        playsound("escape.wav")


if __name__ == '__main__':
    #playsound("nave.wav")
    t1 = threading.Thread(target=radio, daemon=True)
    t1.start()
    prosses = starter.starter_page()
    #gra = game.game() 
        
