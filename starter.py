from baisc import clear, display, lirterki, wait

class starter_page():
    
    def __init__(self):
        clear()
        self.settings_load()
        lirterki("Statki")
        print("\n", "")
        #wait(10)
        display("Ustawienie statków: ")
        display("1. Automatyczne")
        display("2. Ręczne")
        self.setting_choice(1,2)

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

    def settings_save(self, sound):
        x=1

    def settings_load(self):
        with open("settings.txt", "w") as f:
            f.write("hej")

