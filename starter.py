from timeit import repeat
from baisc import clear, display, lirterki, wait, key_detect, print_image, playsound
import multiprocessing

class starter_page():
    settings = {
        "music" : 1,
        "mode" : 1,               #1 - singleplayer (against computer), 2 - local multiplayer, 3 - online multiplayer,
        "auto_placement" : True,
        #"small_ship_num": 4,
        #"mid_ship_num": 3,
        #"large_ship_num" : 2,
        #"huge_ship_num" : 1,
        #"map_x" : 10,
        #"map_y" : 10,
    }
    
    def __init__(self):
        clear()
        lirterki("Statki")
        print("\n", "")
        print_image("Statek.txt")
        self.settings_load()
        self.radio = multiprocessing.Process(target=self.play_music, daemon= True)
        if self.settings["music"] != 0:
            self.radio.start()
        #self.settings_handler()
        #self.initial_questions()
        #wait(10)
        #display("Ustawienie statków: ")
        #display("1. Automatyczne")
        #display("2. Ręczne")
        #ship_placement = self.setting_choice(1,2)
        #display("Ustawienia?")
        #display("1. Tak, poproszę")
        #display("2. Nie, dziękuje")
        #settings = self.setting_choice(1,2)

    def initial_questions(self):
        onec_again = True
        display("Wybierz tryb gry:")
        display("1. Gracz vs Komputer    2. Gracz vs Gracz", newline=False)
        display("    3. On-line (jeszcze nie działa)", color= "RED")
        while onec_again == True:
            self.settings['mode'] = self.setting_choice(max=3)
            if self.settings['mode'] == 3:
                display("Przeież jest napisane, że jeszcze nie działa", "RED")
            else:
                onec_again = False
        display("Wybierz tryb ustawiania statków:")
        display("1. Automatyczny    2. Ręczny")
        self.settings['auto_placement'] = int(self.setting_choice(max=2))
        if self.settings['auto_placement'] == 2:
            self.settings['auto_placement'] = False
        else:
            self.settings['auto_placement'] = True
        last_music = self.settings['music']
        display("Ustawienia: ")
        #self.settinger()
        if last_music == 0:
            if self.settings["music"] == 1:
                self.radio.start()
        else:
            if self.settings["music"] == 0:
                self.radio.terminate()
        return self.settings

    def play_music(self):
        while True:
            playsound("nave.wav")
            playsound("escape.wav")
            

    def settinger(self):
        setter = True
        self.settings_load()
        settings_list = list(self.settings)
        settings_list.remove("mode")
        settings_list.remove("auto_placement")
        #for setting in settings_list:
        #    display(setting + " = " + str(self.settings[setting]))
        #print("")
        #wej = input()
        while setter == True:
            exit_words = ["quit", "exit", "wyjdź", "wyjście"]
            help_words = ["help", "pomoc", "?"]
            wej = input()
            splited = wej.split("=")
            for l in range(len(splited)):
                splited[l] = splited[l].strip()
            settings_list = list(self.settings)
            settings_list.remove("mode")
            settings_list.remove("auto_placement")
            if any(ext in wej for ext in exit_words):
                setter = False
            elif any(ext in wej for ext in help_words):
                print("Dostępne ustawienia:")
                for setting in settings_list:
                    display(setting + " = " + str(self.settings[setting]))
                print("Aby zmienić ustawienie wpisz: *ustawienie* = *wartość*")
                print("Aby zamknąć ustawienia wpisz: wyjdź")
                print("Ustawienia zadziałają dopiero po zapisaniu")
                #print(self.settings)
                #settings_list = settings_list + [[],[]]
                #input()
            else:
                if splited[0] in settings_list:
                    try:
                        self.settings[splited[0]] = int(splited[1])
                    except:
                        display("Niepoprawna wartość", color="RED")
                    #print("")
                    #settings_list = settings_list + [[], []]
                else:
                    display("Nie ma takiego parametru!", "RED")
                    #settings_list = settings_list + []
                    #input()
            #for setting in settings_list + [[],[],[]]:
            #    print ("\033[A                             \033[A")
            #for setting in settings_list:
                #display(setting + " = " + str(self.settings[setting]))
            #print("")
            
        while True:
            display("Czy zapisać? (y/n)")
            decision = key_detect()
            if decision == "y" or decision == "Y":
                self.settings_save()
                break
            elif decision == "n" or decision == "N":
                break

    def setting_choice (self, min = 1, max = 10):
        while True:
            try:
                wej = int(input("Podaj liczbę od " + str(min) + " do " + str(max) + ": "))
                if wej >= min and wej <= max:
                    return wej
                else:
                    print("Możesz wpisywać tylko liczby całkowite z przedziału", min, max)
            except:
                print("Możesz wpisywać tylko liczby całkowite z przedziału", min, max)

    def settings_load(self):
        with open("settings.txt", "r") as f:
            lines = f.readlines()
            for l in lines:
                n = l.split("=")
                self.settings[n[0].strip()] = int(n[1].strip())

    def settings_save(self):
        with open("settings.txt", "w") as f:
            settings_list = list(self.settings)
            settings_list.remove("mode")
            settings_list.remove("auto_placement")
            for setting in settings_list:
                f.write(setting + " = " + str(self.settings[setting]) + "\n")

    def __del__(self):
        if self.radio.is_alive() == True:
            self.radio.terminate()