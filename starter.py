from baisc import clear, lirterki, bcolors, wait

class starter_page():
    
    def __init__(self):
        clear()
        lirterki("Statki")
        print("\n", "")
        wait(10)
        print("Ustawienie statków: ")
        print("1. Automatyczne")
        print("2. Ręczne")
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
