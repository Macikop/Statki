from baisc import clear, display, lirterki, lirterki_render, wait, key_detect, print_image, playsound, screen, image_to_render
import multiprocessing
import network
import os
import sys

class starter_page():
    settings = {
        "music" : 1,
        "sound" : 1,
        "mode" : 1,               #1 - singleplayer (against computer), 2 - local multiplayer, 3 - online multiplayer,
        "auto_placement" : True,
        "server_ip" : "192.168.22.01"
    }
    
    def __init__(self):
        clear()
        self.scr = screen()
        self.scr.display_board_from_render(lirterki_render("Statki", "RAINBOW"), 1, 5)
        #lirterki("Statki")
        #print("\n", "")
        self.scr.display_board_from_render(image_to_render("Statek.txt", "WHITE"), 70, 1)
        print("\n", "")
        #print_image("Statek.txt")
        self.settings_load()
        self.radio = multiprocessing.Process(target=self.play_music, daemon= True)
        if self.settings["music"] != 0:
            self.radio.start()

    def initial_questions(self):
        onec_again = True
        display("Wybierz tryb gry:")
        display("1. Gracz vs Komputer    2. Gracz vs Gracz", newline=False)
        display("    3. On-line", color= "WHITE")
        while onec_again == True:
            self.settings['mode'] = self.setting_choice(max=3)
            if self.settings['mode'] == 3:
                #display("Przeież jest napisane, że jeszcze nie działa", "RED")
                display("Podaj adres IP serwera: ", "WHITE", False)
                self.settings["server_ip"] = input()
                #self.multidebug()
                onec_again = False
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
        display("Czy chcesz włączyć ustawienia?")
        display("1. Tak     2. Nie")
        ustawienia = int(self.setting_choice(max=2))
        if ustawienia == 1:
            display("Ustawienia: ")
            display("Dostępne ustawienia:")
            settings_list = list(self.settings)
            settings_list.remove("mode")
            settings_list.remove("auto_placement")
            settings_list.remove("server_ip")
            for setting in settings_list:
                display(setting + " = " + str(self.settings[setting]))
            display("Aby zmienić ustawienie wpisz: *ustawienie* = *wartość*")
            display("Aby zamknąć ustawienia wpisz: wyjdź")
            display("Ustawienia zadziałają dopiero po zapisaniu")
            self.settinger()
        if last_music == 0:
            if self.settings["music"] == 1:
                self.radio.start()
        else:
            if self.settings["music"] == 0:
                self.radio.terminate()
        return self.settings

    def play_music(self):
        while True:
            playsound("music/nave.wav")
            playsound("music/escape.wav")
            

    def settinger(self):
        setter = True
        self.settings_load()
        settings_list = list(self.settings)
        settings_list.remove("mode")
        settings_list.remove("auto_placement")
        settings_list.remove("server_ip")
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
            settings_list.remove("server_ip")
            if any(ext in wej for ext in exit_words):
                setter = False
            elif any(ext in wej for ext in help_words):
                print("Dostępne ustawienia:")
                for setting in settings_list:
                    display(setting + " = " + str(self.settings[setting]))
                print("Aby zmienić ustawienie wpisz: *ustawienie* = *wartość*")
                print("Aby zamknąć ustawienia wpisz: wyjdź")
                print("Ustawienia zadziałają dopiero po zapisaniu")
            else:
                if splited[0] in settings_list:
                    try:
                        self.settings[splited[0]] = int(splited[1])
                    except:
                        display("Niepoprawna wartość", color="RED")
                else:
                    display("Nie ma takiego parametru!", "RED")
            
        while True:
            display("Czy zapisać? (y/n)")
            decision = key_detect()
            if decision == "y" or decision == "Y":
                self.settings_save()
                break
            elif decision == "n" or decision == "N":
                break
        self.settings_load()

    def multidebug(self):
        n = network.Network()
        send = ""
        while send != "quit":
            send = input()
            recive = n.send(send)
            print(recive)


    def setting_choice (self, min = 1, max = 10):
        while True:
            try:
                wej = int(input("Podaj liczbę od " + str(min) + " do " + str(max) + ": "))
                if wej >= min and wej <= max:
                    return wej
                else:
                    print("Możesz wpisywać tylko liczby całkowite z przedziału", min, "do", max)
            except:
                print("Możesz wpisywać tylko liczby całkowite z przedziału", min, "do", max)

    def settings_load(self):
        with open(os.path.join(sys.path[0],"settings.txt"), "r", encoding= "utf-8") as f:
            lines = f.readlines()
            for l in lines:
                n = l.split("=")
                self.settings[n[0].strip()] = int(n[1].strip())

    def settings_save(self):
        with open(os.path.join(sys.path[0],"settings.txt"), "w", encoding= "utf-8") as f:
            settings_list = list(self.settings)
            settings_list.remove("mode")
            settings_list.remove("auto_placement")
            settings_list.remove("server_ip")
            for setting in settings_list:
                f.write(setting + " = " + str(self.settings[setting]) + "\n")

    def __del__(self):
        if self.radio.is_alive() == True:
            self.radio.terminate()