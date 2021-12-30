from baisc import clear, display, lirterki, wait, key_detect

class starter_page():
    settings = {
        "music" : 1,
        "small_ship_num": 4,
        "mid_ship_num": 3,
        "large_ship_num" : 2,
        "huge_ship_num" : 1,
        "map_x" : 10,
        "map_y" : 10,
        "mode" : "s",               #s - singleplayer (against computer), m - local multiplayer, o - online multiplayer,
        "auto_placement" : True,

    }
    
    def __init__(self):
        clear()
        lirterki("Statki")
        print("\n", "")
        #self.settings_handler()
        wait(10)
        #display("Ustawienie statków: ")
        #display("1. Automatyczne")
        #display("2. Ręczne")
        #ship_placement = self.setting_choice(1,2)
        #display("Ustawienia?")
        #display("1. Tak, poproszę")
        #display("2. Nie, dziękuje")
        #settings = self.setting_choice(1,2)

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
                self.settings[n[0].strip()] = n[1].strip()
            #print(self.settings)

    def settings_save(self):
        with open("settings.txt", "w") as f:
            settings_list = list(self.settings)
            settings_list.remove("mode")
            settings_list.remove("auto_placement")
            for setting in settings_list:
                f.write(setting + " = " + str(self.settings[setting]) + "\n")

    def settings_handler(self):
        setter = True
        self.settings_load()
        settings_list = list(self.settings)
        settings_list.remove("mode")
        settings_list.remove("auto_placement")
        for setting in settings_list:
            display(setting + " = " + str(self.settings[setting]))
        print("")
        #wej = input()
        while setter == True:
            exit_words = ["quit", "exit", "wyjdź", "wyjście"]
            help_words = ["help", "pomoc", "?"]
            wej = input()
            splited = wej.split("=")
            for l in range(len(splited)):
                splited[l] = splited[l].strip()
            l_settings = list(self.settings)
            l_settings.remove("mode")
            l_settings.remove("auto_placement")
            if any(ext in wej for ext in exit_words):
                setter = False
            elif any(ext in wej for ext in help_words):
                print("Aby zmienić ustawienie wpisz: ustawienie = wartość")
                print("Aby zamknąć ustawienia wpisz: wyjdź")
                settings_list =+ [[],[]]
            else:
                if splited[0] in l_settings:
                    self.settings[splited[0]] = int(splited[1])
                else:
                    display("Nie ma takiego parametru!", "RED")
                    settings_list = settings_list + []
            for setting in settings_list + [[],[],[]]:
                print ("\033[A                             \033[A")
            for setting in settings_list:
                display(setting + " = " + str(self.settings[setting]))
            print("")
            
        while True:
            display("Czy zapisać? (y/n)")
            decision = key_detect()
            if decision == "y" or decision == "Y":
                self.settings_save()
                break
            elif decision == "n" or decision == "N":
                break