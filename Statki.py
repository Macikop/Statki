import starter
import game
import ender

if __name__ == '__main__':
    first_page = starter.starter_page()
    setting = first_page.initial_questions()
    gra = game.game()
    wygrana = gra.start(setting)
    del first_page
    end = ender.ender_page(wygrana, setting)