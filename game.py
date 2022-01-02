from baisc import clear, display, key_detect, display_at
import random

class board():
    size_x = 10
    size_y = 10
    
    def __init__(self):
        self.plansza = []
        for x in range(self.size_y):
            self.plansza.append([])
            for y in range(self.size_x):
                self.plansza[x].append([0])

    def print_board(self):
        for n in self.plansza:
            print(n)

    def render_board(self, fleet):
        water = '▓'
        pla = []
        pla.append([["    A B C D E F G H I J", "WHITE"]])
        pla.append([["  ╔═════════════════════╗", "WHITE"]])
        index = 0
        for n in self.plansza:
            i = 0
            line =[]
            for u in n:
                try:
                    if u[0] != 0:
                            tile = str(u[0])
                            position = fleet[u[0]-1].dir
                    else:
                        tile = water
                except:
                    if u[0] == 'x':
                        tile = 'x'
                        col = "RED"
                    else:
                        tile = 'o'
                        col = "PURPLE"
                if i == 0:
                    index = index + 1
                    if index < 10:
                        num = " " + str(index)
                    else:
                        num = str(index)
                    line.append([num + "║", "WHITE" ])
                    #line.append([water, "BLUE"])
                if tile != water:
                    try:
                        if u[0] >= 7 and u[0] <= 10:
                            line.append([water, "BLUE"])
                            line.append(["■", "YELLOW"])

                        elif position == True:
                            line.append([water, "BLUE"])
                            line.append(["█", "YELLOW"])
                        else:
                            line.append(["▬", "YELLOW"])
                            line.append(["▬", "YELLOW"])
                    except:
                        line.append([water,"BLUE"])
                        line.append([tile, col])
                else:
                    line.append([water,"BLUE"])
                    line.append([tile, "BLUE"])
                if i == self.size_x -1:
                    line.append([water, "BLUE"])
                    line.append(["║", "WHITE"])
                    pla.append(line)
                i = i + 1
        pla.append([["  ╚═════════════════════╝","WHITE"]])
        #print(pla)
        return pla

    def place_ship(self, x, y, dir, length, ship_num):
        if dir == False:
            if self.size_x - 1 >= x + (length - 1) and self.size_y - 1 >= y:
                for n in range(x, x+length):
                    self.plansza[y][n] = [ship_num]
        else:
            if self.size_y - 1 >= y + (length - 1) and self.size_x - 1 >= x:
                for n in range(y, y+length):
                    self.plansza[n][x] = [ship_num]

    def check_ships(self,x, y, dir, size):
        returner = True
        tile =[]
        if dir == True:
            for n in range(-1,2):
                for l in range(-1, size + 1):
                    try:
                        tile.append(self.plansza[(y+l)][x+n])
                    except:
                        pass
        else:
            for n in range(-1,2):
                for l in range(-1, size + 1):
                    try:
                        tile.append(self.plansza[y+n][(x+l)])
                    except:
                        pass
        for n in tile:
            if n[0] != 0:
                returner = True
                return returner
            else:
                returner = False
        return returner

class ship():
    size = 1        #sieze:         1 - 4
    pos_x = 1       #position x:    0 - 9
    pos_y = 1       #position y:    0 - 9
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
    cursor_x_offset = 2
    cursor_y_offset= 2
    cursor_x = 0
    cursor_y = 0
    cursor_char = 'X' 
    number_of_ships = frigate_num + destroyer_num + cruiser_num + battleship_num

    def __init__(self):
        clear()
        self.team_a_fleet = self.create_fleet(self.number_of_ships)
        self.team_b_fleet = self.create_fleet(self.number_of_ships)
        self.plansza_a = board()
        self.random_ship_placement(self.plansza_a, self.team_a_fleet)
        #self.plansza_a.print_board()
        #self.plansza_a.print_board()
        #print("")
        #self.plansza_b = board()
        #self.plansza_b.print_board()
        #self.plansza_a.place_ship(3, 2, False, 3, 1)
        #clear()
        #self.plansza_a.print_board()
        render = self.plansza_a.render_board(self.team_a_fleet)
        while True:
            self.display_board_from_render(render)
            render = self.plansza_a.render_board(self.team_a_fleet)
            self.cursor_move(render)
            

    def create_fleet (self, n):
        returner = []
        for _ in range(n):
            returner.append(ship())
        return returner

    def random_ship_placement(self, board_obj, fleet_obj):
        n = 0
        miss = True
        for _ in range(self.battleship_num):
            size = 4
            miss = True
            while miss == True:
                direction = bool(random.getrandbits(1))
                if direction == False:
                    x = random.randrange(0, (board.size_x+1) - size)
                    y = random.randrange(0,9)
                else:
                    x = random.randrange(0, 9)
                    y = random.randrange(0, (board.size_y+1) - size)
                miss = board_obj.check_ships(x, y, direction, size)
            board_obj.place_ship(x, y, direction, size, n+1)
            fleet_obj[n].set_place(x, y, size, direction)
            n = n + 1
        
        for _ in range(self.cruiser_num):
            miss = True
            size = 3
            while miss == True:
                direction = bool(random.getrandbits(1))
                if direction == False:
                    x = random.randrange(0, (board.size_x+1) - size)
                    y = random.randrange(0,9)
                else:
                    x = random.randrange(0, 9)
                    y = random.randrange(0, (board.size_y+1) - size)
                miss = board_obj.check_ships(x, y, direction, size)
            board_obj.place_ship(x, y, direction, size, n+1)
            fleet_obj[n].set_place(x, y, size, direction)
            n = n + 1

        for _ in range(self.destroyer_num):
            miss = True
            size = 2
            while miss == True:
                direction = bool(random.getrandbits(1))
                if direction == False:
                    x = random.randrange(0, (board.size_x+1) - size)
                    y = random.randrange(0,9)
                else:
                    x = random.randrange(0, 9)
                    y = random.randrange(0, (board.size_y+1) - size)
                miss = board_obj.check_ships(x, y, direction, size)
            board_obj.place_ship(x, y, direction, size, n+1)
            fleet_obj[n].set_place(x, y, size, direction)
            n = n + 1

        for _ in range(self.frigate_num):
            miss = True
            size = 1
            while miss == True:
                direction = bool(random.getrandbits(1))
                if direction == False:
                    x = random.randrange(0, (board.size_x+1) - size)
                    y = random.randrange(0,9)
                else:
                    x = random.randrange(0, 9)
                    y = random.randrange(0, (board.size_y+1) - size)
                miss = board_obj.check_ships(x, y, direction, size)
            board_obj.place_ship(x, y, direction, size, n+1)
            fleet_obj[n].set_place(x, y, size, direction)
            n = n + 1
    def cursor_move(self, render):
        #print(f'\033[{self.cursor_y_offset + self.cursor_y+1};{self.cursor_x_offset + self.cursor_x+1}H'+ self.cursor_char + f'\033[;{-1}H', end='')
        self.cursor_char = "X"
        key = key_detect()
        if key == "right":
            self.cursor_x = self.cursor_x + 2
        if key == "left":
            self.cursor_x = self.cursor_x - 2
        if key == "up":
            self.cursor_y = self.cursor_y - 1
        if key == "down":
            self.cursor_y = self.cursor_y + 1

        if self.cursor_y < 0:
            self.cursor_y = 0
        if self.cursor_x < 0:
            self.cursor_x = 0
        if self.cursor_y > board.size_y-1:
            self.cursor_y = board.size_y-1
        if self.cursor_x > 2*board.size_x-2:
            self.cursor_x = 2*board.size_x-2
        self.apply_mask_to_render(render, 'X', "WHITE", self.cursor_x + self.cursor_x_offset, self.cursor_y + self.cursor_y_offset)

        if key == " ":
            self.cursor_char = "O"
            self.shoot(self.cursor_x, self.cursor_y, self.plansza_a, self.team_a_fleet)
            #self.apply_mask_to_render(render, 'X', "RED", self.cursor_x + self.cursor_x_offset, self.cursor_y + self.cursor_y_offset)
        
    def display_board_from_render(self, render):
        #clear()
        y = 0
        x = 0
        for line in render:
            x = 0
            for word in line:
                if word != line[-1]:
                    display_at(x + 1, y+1, word[0], word[1], False)
                else:
                    display_at(x + 1, y+1, word[0], word[1], True)
                x = x + len(word[0]) 
            y = y + 1

    def apply_mask_to_render(self, render, mod, color, x, y):
        render[y][x][0] = mod
        render[y][x][1] = color       
            
    def shoot(self, x, y, board_obj, fleet):
        i = board_obj.plansza[y][int(x/2)]
        if  i != [0] and i != ['o']:
            board_obj.plansza[y][int(x/2)] = ['x']
        if i == [0]:
            board_obj.plansza[y][int(x/2)] = ['o']