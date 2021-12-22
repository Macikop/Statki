from os import system, name
from time import sleep
import sys
import random

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def wait(time):
        animation = "|/-\\"
        for i in range(time):
            sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print ("End!")
        print ("\033[A                             \033[A")

def clear():
    if name == 'nt':
        _ = system('cls')   #windows
    else:
        _ = system('clear') #linux

def lirterki(word):
    word = word.upper()
    with open("Literki.txt") as file:
        big_letters = file.read()
        big_letters = big_letters.split('%')
        napis = []
        index = 0 
        for letter in word:
            order_num = ord(letter)-65
            lines = big_letters[order_num].splitlines()
            for line in range(9):
                if index == 0:
                    napis.append(lines[line])
                elif index !=0:
                    napis[line] = napis[line] + lines[line]
            index = index + 1
            returner = ""    
            for n in napis:
                returner = returner + "\n" + n

        sys.stdout.write(returner)
        sys.stdout.flush()
        sleep(0.1)

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

class board():
    size_x = 10
    size_y = 10
    

    def print_board(self):
        for n in self.plansza:
            print(n)

    def display_board(self):
        water = '▓'
        print("╔═════════════════════╗"+ bcolors.OKBLUE)
        for n in self.plansza:
            i = 0
            for u in n:
                if u[0] == 0:
                    s = water
                else:
                    #s = str(u[0])
                    s = "■"
                if i == 0:
                    sys.stdout.write("║" + bcolors.OKBLUE)
                #for i in range(self.size_x):
                if s != water:
                    sys.stdout.write(water + bcolors.WARNING)
                    sys.stdout.write(s + bcolors.OKBLUE)
                else:
                    sys.stdout.write(water + bcolors.OKBLUE)
                    sys.stdout.write(s + bcolors.OKBLUE)
                if i == self.size_x -1:
                    sys.stdout.write(water + "║\n"+ bcolors.OKBLUE)
                i = i + 1
        #print(pla)
        print("╚═════════════════════╝"+ bcolors.OKBLUE)

    def __init__(self):
        self.plansza = []
        for y in range(self.size_y):
            self.plansza.append([])
            for x in range(self.size_x):
                self.plansza[y].append([0])

    def place_ship(self, x, y, dir, length, ship_num):
        if dir == False:
            if self.size_x - 1 >= x + (length - 1) and self.size_y - 1 >= y:
                for n in range(x, x+length):
                    self.plansza[y][n] = [ship_num]
        else:
            if self.size_y - 1 >= y + (length - 1) and self.size_x - 1 >= x:
                for n in range(y, y+length):
                    self.plansza[n][x] = [ship_num]

    def check_ship(x, y, dir, size):
        n=1

class ship():
    size = 1        #sieze:         1 - 4
    pos_x = 1       #position x:    1 - 10
    pos_y = 1       #position y:    1 - 10
    dir = True      #direction:     True - vertical, False - horizontal
    damage = []     #damage:        [[True],[False]]
    status = True   #status:        True - alive, False - destroyed

    def set_place(self, x, y, size, direction):
        self.dir = direction
        self.size = size
        if direction == False:
            if board.size_x - 1 >= x + (size - 1) and board.size_y - 1 >= y:
                self.pos_x = x
                self.pos_y = y
        else:
            if board.size_y - 1 >= y + (size - 1) and board.size_x - 1 >= x:
                self.pos_y = y
                self.pos_x = x

class game():
    turns = 0
    frigate_num = 4
    destroyer_num = 3
    cruiser_num = 2
    battleship_num = 1

    number_of_ships = frigate_num + destroyer_num + cruiser_num + battleship_num

    def __init__(self):
        #clear()
        self.team_a_ships = self.fleet(self.number_of_ships)
        self.team_b_ships = self.fleet(self.number_of_ships)
        self.plansza_a = board()
        self.random_ship_placement()
        #self.plansza_a.print_board()
        #print("")
        #self.plansza_b = board()
        #self.plansza_b.print_board()
        #self.plansza_a.place_ship(3, 2, False, 3, 1)
        #clear()
        #self.plansza_a.print_board()

    def fleet (self, n):
        returner = []
        for _ in range(n):
            returner.append(ship())
        return returner

    def random_ship_placement(self):
        n = 0
        for _ in range(self.frigate_num):
            size = 1
            direction = bool(random.getrandbits(1))

            if direction == False:
                self.plansza_a.place_ship(random.randrange(0, (board.size_x + 1) - size), random.randrange(0,9), direction, size, n+1)
            else:
                self.plansza_a.place_ship(random.randrange(0, 9), random.randrange(0, (board.size_y + 1) - size), direction, size, n+1)
            n = n + 1
        
        for _ in range(self.destroyer_num):
            size = 2
            direction = bool(random.getrandbits(1))

            if direction == False:
                self.plansza_a.place_ship(random.randrange(0, (board.size_x + 1) - size), random.randrange(0,9), direction, size, n+1)
            else:
                self.plansza_a.place_ship(random.randrange(0, 9), random.randrange(0, (board.size_y + 1) - size), direction, size, n+1)
            n = n + 1

        for _ in range(self.cruiser_num):
            size = 3
            direction = bool(random.getrandbits(1))

            if direction == False:
                self.plansza_a.place_ship(random.randrange(0, (board.size_x + 1) - size), random.randrange(0,9), direction, size, n+1)
            else:
                self.plansza_a.place_ship(random.randrange(0, 9), random.randrange(0, (board.size_y + 1) - size), direction, size, n+1)
            n = n + 1

        for _ in range(self.battleship_num):
            size = 4
            direction = bool(random.getrandbits(1))

            if direction == False:
                self.plansza_a.place_ship(random.randrange(0, (board.size_x + 1) - size), random.randrange(0,9), direction, size, n+1)
            else:
                self.plansza_a.place_ship(random.randrange(0, 9), random.randrange(0, (board.size_y + 1) - size), direction, size, n+1)
            n = n + 1
        
        self.plansza_a.print_board()
        self.plansza_a.display_board()




            

prosses = starter_page()


gra = game()        
