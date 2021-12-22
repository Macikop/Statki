from baisc import clear, lirterki, bcolors, wait
import sys
import random

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
        
        #self.plansza_a.print_board()
        self.plansza_a.display_board()