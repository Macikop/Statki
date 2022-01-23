import ender
import starter
import game

if __name__ == '__main__':
    #t1 = multiprocessing.Process(target=radio, daemon= True)
    #t1.start()
    first_page = starter.starter_page()
    setting = first_page.initial_questions()
    gra = game.game()
    wygrana = gra.start(setting)
    del first_page
    #t1.terminate()
    end = ender.ender_page(wygrana)