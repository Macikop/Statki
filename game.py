from baisc import clear, display, key_detect, display_at, wait
import random

class board():
    size_x = 10
    size_y = 10
    visibility = False
    
    def __init__(self):
        self.plansza = []
        for x in range(self.size_y):
            self.plansza.append([])
            for y in range(self.size_x):
                self.plansza[x].append([0])

    def print_board(self):
        for n in self.plansza:
            print(n)

    def render_board(self, fleet, vis):
        self.visibility = vis
        if self.visibility == True:
            water = '█'
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
        else:
            water = "█"
            pla = []
            pla.append([["    A B C D E F G H I J", "WHITE"]])
            pla.append([["  ╔═════════════════════╗", "WHITE"]])
            index = 0
            for n in self.plansza:
                i = 0
                line =[]
                for u in n:
                    if str(type(u[0])) != "<class 'int'>": 
                        if u[0] == 'x':
                            tile = 'x'
                            col = "RED"
                        elif u[0] == 'o':
                            tile = 'o'
                            col = "PURPLE"
                    else:
                        tile = "█"
                        water = "█"
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
                f = 0
                for n in range(x, x+length):
                    self.plansza[y][n] = [ship_num, f]
                    f = f + 1
        else:
            if self.size_y - 1 >= y + (length - 1) and self.size_x - 1 >= x:
                f = 0
                for n in range(y, y+length):
                    self.plansza[n][x] = [ship_num, f]
                    f = f + 1

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
    
    def check_end(self):
        returner = True
        for line in self.plansza:
            for word in line:
                if word == [0] or word == ['x'] or word == ['o']:
                    returner = False
                else:
                    return True
        return returner

class ship():
    size = 1        #sieze:         1 - 4
    pos_x = 1       #position x:    0 - 9
    pos_y = 1       #position y:    0 - 9
    dir = True      #direction:     True - vertical, False - horizontal
    damage = []     #damage:        [[True],[False]]
    status = True   #status:        True - alive, False - destroyed

    def __init__(self):
        self.damage = []

    def set_place(self, x, y, size, direction):
        self.dir = direction
        self.damage = []
        self.size = size
        if direction == False:
            if board.size_x - 1 >= x + (size - 1) and board.size_y - 1 >= y:
                self.pos_x = x
                self.pos_y = y
        else:
            if board.size_y - 1 >= y + (size - 1) and board.size_x - 1 >= x:
                self.pos_y = y
                self.pos_x = x
        for pole in range(size):
            self.damage.append(False)

    def damage_ship(self, destroyed_part):
        self.damage[destroyed_part] = True

class game():

    def __init__(self):
        self.turns = 0
        self.frigate_num = 4
        self.destroyer_num = 3
        self.cruiser_num = 2
        self.battleship_num = 1
        self.number_of_ships = self.frigate_num + self.destroyer_num + self.cruiser_num + self.battleship_num
        self.actual_player = True
        self.scr = screen()
        self.cursor_x_offset = 2
        self.cursor_y_offset= 2
        self.cursor_x = 0
        self.cursor_y = 0
        self.cursor_char = 'X' 

    def start(self):
        clear()
        bot = enemy()
        self.team_a_fleet = self.create_fleet(self.number_of_ships)
        self.team_b_fleet = self.create_fleet(self.number_of_ships)
        self.plansza_a = board()
        self.random_ship_placement(self.plansza_a, self.team_a_fleet)
        self.plansza_b = board()
        self.random_ship_placement(self.plansza_b, self.team_b_fleet)
        render_a = self.plansza_a.render_board(self.team_a_fleet, True)
        render_b = self.plansza_b.render_board(self.team_b_fleet, False)
        #render_ship_a = self.render_fleet_status(self.team_a_fleet)
        #render_ship_b = self.render_fleet_status(self.team_b_fleet)
        #wind = window()
        #wait(100)
        end = True
        while end == True:
            self.scr.display_board_from_render(render_a, 0, 0)
            self.scr.display_board_from_render(render_b, 40, 0)
            #self.scr.display_board_from_render(render_ship_a, 40, 0)
            #self.scr.display_board_from_render(render_ship_b, 120, 0)
            render_a = self.plansza_a.render_board(self.team_a_fleet, True)
            render_b = self.plansza_b.render_board(self.team_b_fleet, True)
            #render_ship_a = self.render_fleet_status(self.team_a_fleet)
            #render_ship_b = self.render_fleet_status(self.team_b_fleet)
            if self.actual_player == True:
                #self.cursor_move(render_a)
                bot.easy_bot(self.plansza_a)
                self.change_player()
            else:
                self.cursor_move(render_b)
                #self.change_player()
            end_a = self.plansza_a.check_end()
            end_b = self.plansza_b.check_end()
            if end_a == False or end_b == False:
                end = False
        if end_a == False:
            return False
        else:
            return True
        
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
        self.scr.apply_mask_to_render(render, 'X', "WHITE", self.cursor_x + self.cursor_x_offset, self.cursor_y + self.cursor_y_offset)

        if key == " ":
            self.cursor_char = "O"
            if self.actual_player == True:
                self.shoot(self.cursor_x, self.cursor_y, self.plansza_a, self.team_a_fleet)
            else:
                self.shoot(self.cursor_x, self.cursor_y, self.plansza_b, self.team_b_fleet)
            self.change_player()

    def shoot(self, x, y, board_obj, fleet):
        i = board_obj.plansza[y][int(x/2)]
        if  i != [0] and i != ['o'] and i != ['x']:
            board_obj.plansza[y][int(x/2)] = ['x']
            fleet[i[0]-1].damage_ship(i[1])
        if i == [0]:
            board_obj.plansza[y][int(x/2)] = ['o']
                    
    def change_player(self):
            if self.actual_player == True:
                self.actual_player = False
                self.cursor_x = 0 
                self.cursor_y = 0
            else:
                self.actual_player = True
                self.cursor_x = 0
                self.cursor_y = 0

class enemy():
    def __init__(self):
        self.known_board = []
        self.past_moves = []

    def easy_bot(self, enemy_board):
        repeat = False
        while repeat == False:
            x = random.randint(0, board.size_x-1)
            y = random.randint(0, board.size_y-1)
            if [x, y] in self.past_moves:
                repeat = False
            else:
                repeat = True
                self.past_moves.append([x, y])
                i = enemy_board.plansza[y][int(x)]
                if  i != [0] and i != ['o']:
                    enemy_board.plansza[y][int(x)] = ['x']
                if i == [0]:
                    enemy_board.plansza[y][int(x)] = ['o']

class screen():
    def display_board_from_render(self, render, x, y):
        #clear()
        a_y = y
        a_x = x
        for line in render:
            a_x = x
            for word in line:
                if word != line[-1]:
                    display_at(a_x + 1, a_y+1, word[0], word[1], False)
                else:
                    display_at(a_x + 1, a_y+1, word[0], word[1], True)
                a_x = a_x + len(word[0]) 
            a_y = a_y + 1
             
    def render_fleet_status(self, fleet):
        pla = []
        size_x = 6
        size_y = 10
        ship_num = 0
        pla.append([["╔══════╗", "WHITE"]])
        for y in range(size_y):
            line = []
            for x in range(size_x):
                if y % 2 == 0:
                    if x == 0 or x == size_x - 1:
                        line.append(["║", "WHITE"])
                    else:
                        line.append([" ", "WHITE"])
                else:
                    if x == 0 or x == size_x - 1:
                        line.append(["║", "WHITE"])
                    else:
                        for part in range(fleet[ship_num].size):
                            if fleet[ship_num].damage[part] == True:
                                line.append(["x", "RED"])
                            else: 
                                line.append(["▬", "YELLOW"])
                        #ship_num = ship_num + 1
            pla.append(line)
        pla.append([["╔══════╗", "WHITE"]])
        return pla
    
    def apply_mask_to_render(self, render, mod, color, x, y):
        render[y][x][0] = mod
        render[y][x][1] = color

#class window():
#    size_x = 10
#    size_y = 10
#    win =[]
#    
#    def write(self):
#        for y in range(self.size_y):
#            for x in  range(self.size_x):
#                if y == 0:
#                    if x == 0:
#                        self.win.append(["╔", "WHITE"])
#                    elif x == self.size_x - 1:
#                        self.win.append(["╗", "WHITE"])
#                    else:
#                        self.win.append(["═", "WHITE"])
#                elif y == self.size_y - 1:
#                    if x == 0:
#                        self.win.append(["╔", "WHITE"])
#                    elif x == self.size_x - 1:
#                        self.win.append(["╗", "WHITE"])
#                    else:
#                        self.win.append(["═", "WHITE"])
#                else:
#                    self.win.append(["║", "WHITE"])
#        return self.win