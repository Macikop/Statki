from baisc import clear, display, key_detect, display_at, multi_playsound, playsound, wait, screen
import random
import time

class board():
    size_x = 10
    size_y = 10
    visibility = False
    cursor_limit_x = 2*size_x-2
    cursor_limit_y = size_y-1

    def __init__(self):
        self.plansza = []
        for x in range(self.size_y):
            self.plansza.append([])
            for y in range(self.size_x):
                self.plansza[x].append([0])

    def restore_cursor_limit(self):
        self.cursor_limit_x = 2*board.size_x-2
        self.cursor_limit_y = board.size_y-1

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
        damage = True
        for n in self.damage:
            if n == False:
                damage = False
        if damage == True:
            self.status = False

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

    def start(self, settings):
        clear()
        bot = enemy()
        self.team_a_fleet = self.create_fleet(self.number_of_ships)
        self.team_b_fleet = self.create_fleet(self.number_of_ships)
        self.plansza_a = board()
        self.plansza_b = board()
        self.place = settings["auto_placement"]
        self.mode = settings["mode"]
        self.cursor_a = cursor(True)
        self.cursor_b = cursor(True)
        if self.place == True:
            self.random_ship_placement(self.plansza_a, self.team_a_fleet)
            self.random_ship_placement(self.plansza_b, self.team_b_fleet)
        else:
            if settings["mode"] == 2:
                self.actual_player = True
                if self.actual_player == True:
                    self.manual_ship_placement(self.plansza_a, self.team_a_fleet)
                    self.actual_player = False
                if self.actual_player == False:
                    self.manual_ship_placement(self.plansza_b, self.team_b_fleet)
                self.place = True
            else:
                self.actual_player = True
                if self.actual_player == True:
                    self.manual_ship_placement(self.plansza_a, self.team_a_fleet)
                    self.actual_player = False
                self.random_ship_placement(self.plansza_b, self.team_b_fleet)
                self.place = True
        clear()
        if settings["mode"] == 1:
            render_a = self.plansza_a.render_board(self.team_a_fleet, True)
            render_b = self.plansza_b.render_board(self.team_b_fleet, False)
        elif settings["mode"] == 2:
            display_at(0, 1, "Gracz 1")
            display_at(0, 2, "Naciśnij ENTER")
            key_detect()
            render_a = self.plansza_a.render_board(self.team_a_fleet, True)
            render_b = self.plansza_b.render_board(self.team_b_fleet, False)
        self.actual_player = False
        last_player = False
        end = True
        while end == True:
            if settings["mode"] == 2:
                if last_player == True and self.actual_player == False:
                    render_a = self.plansza_a.render_board(self.team_a_fleet, False)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, True)
                    self.scr.display_board_from_render(render_a, 0, 0)
                    self.scr.display_board_from_render(render_b, 40, 0)
                    render_a = self.plansza_a.render_board(self.team_a_fleet, True)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, False)
                    time.sleep(1)
                    clear()
                    display_at(0, 1, "Gracz 1")
                    display_at(0, 2, "Naciśnij ENTER")
                    key_detect()
                elif last_player == False and self.actual_player == True:
                    render_a = self.plansza_a.render_board(self.team_a_fleet, True)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, False)
                    self.scr.display_board_from_render(render_a, 0, 0)
                    self.scr.display_board_from_render(render_b, 40, 0)
                    render_a = self.plansza_a.render_board(self.team_a_fleet, False)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, True)
                    time.sleep(1)
                    clear()
                    display_at(0, 1, "Gracz 2")
                    display_at(0, 2, "Naciśnij ENTER")
                    key_detect()
            self.scr.display_board_from_render(render_a, 0, 0)
            self.scr.display_board_from_render(render_b, 40, 0)
            if settings["mode"] == 1:
                render_a = self.plansza_a.render_board(self.team_a_fleet, True)
                render_b = self.plansza_b.render_board(self.team_b_fleet, False)
                if self.actual_player == True:
                    bot.easy_bot(self.plansza_a)
                    self.change_player()
                else:
                    self.cursor_b.cursor_move(self.scr, render_b, self.plansza_b, self.team_b_fleet)
                    if self.cursor_b.next_player() == True:
                        self.change_player()
            elif settings["mode"] == 2:
                if self.actual_player == True:
                    render_a = self.plansza_a.render_board(self.team_a_fleet, False)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, True)
                else:
                    render_a = self.plansza_a.render_board(self.team_a_fleet, True)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, False)
                if self.actual_player == True:
                    self.cursor_a.cursor_move(self.scr, render_a, self.plansza_a, self.team_a_fleet)
                    if self.cursor_a.next_player() == True:
                        self.change_player()
                    last_player = True
                else:
                    self.cursor_b.cursor_move(self.scr, render_b, self.plansza_b, self.team_a_fleet)
                    if self.cursor_b.next_player() == True:
                        self.change_player()
                    last_player = False
            end_a = self.plansza_a.check_end()
            end_b = self.plansza_b.check_end()
            if end_a == False or end_b == False:
                end = False
        del self.scr
        if end_a == False:
            return False
        else:
            return True
        
    def create_fleet (self, n):
        returner = []
        for _ in range(n):
            returner.append(ship())
        return returner

    def manual_ship_placement(self, board_obj, fleet_obj):
        common_cursor = cursor(False)
        n = 0
        miss = True
        direction = True
        render = board_obj.render_board(fleet_obj, True)
        for _ in range(self.battleship_num):
            self.scr.display_board_from_render(render, 0, 0)
            render = board_obj.render_board(fleet_obj, True)
            size = 4
            miss = True
            board_obj.restore_cursor_limit()
            board_obj.cursor_limit_y = board_obj.cursor_limit_y - (size-1)
            while miss == True:
                self.scr.display_board_from_render(render, 0, 0)
                render = board_obj.render_board(fleet_obj, True)
                cursor_response = common_cursor.cursor_move(self.scr, render, board_obj, None, size, direction)
                if str(type(cursor_response)) == "<class 'list'>" :
                    if cursor_response != ["dir_change"]:
                        x = int(cursor_response[0]/2)
                        y = cursor_response[1]
                        miss = board_obj.check_ships(x, y, direction, size)
                    else:
                        if direction == True:
                            direction = False
                            board_obj.restore_cursor_limit()
                            board_obj.cursor_limit_x = board_obj.cursor_limit_x - ((2*size)-2)
                        else:
                            direction = True
                            board_obj.restore_cursor_limit()
                            board_obj.cursor_limit_y = board_obj.cursor_limit_y - (size-1)
            board_obj.place_ship(x, y, direction, size, n+1)
            fleet_obj[n].set_place(x, y, size, direction)
            n = n + 1

        for _ in range(self.cruiser_num):
            self.scr.display_board_from_render(render, 0, 0)
            render = board_obj.render_board(fleet_obj, True)
            size = 3
            miss = True
            board_obj.restore_cursor_limit()
            board_obj.cursor_limit_y = board_obj.cursor_limit_y - (size-1)
            while miss == True:
                self.scr.display_board_from_render(render, 0, 0)
                render = board_obj.render_board(fleet_obj, True)
                cursor_response = common_cursor.cursor_move(self.scr, render, board_obj, None, size, direction)
                if str(type(cursor_response)) == "<class 'list'>" :
                    if cursor_response != ["dir_change"]:
                        x = int(cursor_response[0]/2)
                        y = cursor_response[1]
                        miss = board_obj.check_ships(x, y, direction, size)
                    else:
                        if direction == True:
                            direction = False
                            board_obj.restore_cursor_limit()
                            board_obj.cursor_limit_x = board_obj.cursor_limit_x - (2*size-2)
                        else:
                            direction = True
                            board_obj.restore_cursor_limit()
                            board_obj.cursor_limit_y = board_obj.cursor_limit_y - (size-1)
            board_obj.place_ship(x, y, direction, size, n+1)
            fleet_obj[n].set_place(x, y, size, direction)
            n = n + 1

        for _ in range(self.destroyer_num):
            self.scr.display_board_from_render(render, 0, 0)
            render = board_obj.render_board(fleet_obj, True)
            size = 2
            miss = True
            board_obj.restore_cursor_limit()
            board_obj.cursor_limit_y = board_obj.cursor_limit_y - (size-1)
            while miss == True:
                self.scr.display_board_from_render(render, 0, 0)
                render = board_obj.render_board(fleet_obj, True)
                cursor_response = common_cursor.cursor_move(self.scr, render, board_obj, None, size, direction)
                if str(type(cursor_response)) == "<class 'list'>" :
                    if cursor_response != ["dir_change"]:
                        x = int(cursor_response[0]/2)
                        y = cursor_response[1]
                        miss = board_obj.check_ships(x, y, direction, size)
                    else:
                        if direction == True:
                            direction = False
                            board_obj.restore_cursor_limit()
                            board_obj.cursor_limit_x = board_obj.cursor_limit_x - (2*size-2)
                        else:
                            direction = True
                            board_obj.restore_cursor_limit()
                            board_obj.cursor_limit_y = board_obj.cursor_limit_y - (size-1)
            board_obj.place_ship(x, y, direction, size, n+1)
            fleet_obj[n].set_place(x, y, size, direction)
            n = n + 1

        for _ in range(self.frigate_num):
            self.scr.display_board_from_render(render, 0, 0)
            render = board_obj.render_board(fleet_obj, True)
            size = 1
            miss = True
            board_obj.restore_cursor_limit()
            board_obj.cursor_limit_y = board_obj.cursor_limit_y - (size-1)
            while miss == True:
                self.scr.display_board_from_render(render, 0, 0)
                render = board_obj.render_board(fleet_obj, True)
                cursor_response = common_cursor.cursor_move(self.scr, render, board_obj, None, size, direction)
                if str(type(cursor_response)) == "<class 'list'>" :
                    if cursor_response != ["dir_change"]:
                        x = int(cursor_response[0]/2)
                        y = cursor_response[1]
                        miss = board_obj.check_ships(x, y, direction, size)
                    else:
                        if direction == True:
                            direction = False
                            board_obj.restore_cursor_limit()
                            board_obj.cursor_limit_x = board_obj.cursor_limit_x - (2*size-2)
                        else:
                            direction = True
                            board_obj.restore_cursor_limit()
                            board_obj.cursor_limit_y = board_obj.cursor_limit_y - (size-1)
            board_obj.place_ship(x, y, direction, size, n+1)
            fleet_obj[n].set_place(x, y, size, direction)
            n = n + 1

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
                    
    def change_player(self):
        if self.actual_player == True:
            self.actual_player = False
        else:
            self.actual_player = True

class cursor():
    cursor_x_offset = 2
    cursor_y_offset= 2
    cursor_x = 0
    cursor_y = 0
    cursor_char = 'X' 
    shooted = False
    
    def __init__(self, place):
        self.place = place

    def cursor_move(self, screen, render, board_obj, fleet_obj = None, size = 1, dir = True):
        if self.cursor_y < 0:
            self.cursor_y = 0
        if self.cursor_x < 0:
            self.cursor_x = 0
        if self.cursor_y > board_obj.cursor_limit_y:
            self.cursor_y = board_obj.cursor_limit_y
        if self.cursor_x > board_obj.cursor_limit_x:
            self.cursor_x = board_obj.cursor_limit_x

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
        if self.cursor_y > board_obj.cursor_limit_y:
            self.cursor_y = board_obj.cursor_limit_y
        if self.cursor_x > board_obj.cursor_limit_x:
            self.cursor_x = board_obj.cursor_limit_x
        if self.place == True:
            screen.apply_mask_to_render(render, 'X', "WHITE", self.cursor_x + self.cursor_x_offset, self.cursor_y + self.cursor_y_offset)
        else:
            if size != 1:
                if dir == True:
                    for n in range(size):
                        screen.apply_mask_to_render(render, '█', "YELLOW", self.cursor_x + self.cursor_x_offset, self.cursor_y + self.cursor_y_offset + n)
                else:
                    for n in range(size*2):
                        screen.apply_mask_to_render(render, '▬', "YELLOW", self.cursor_x + self.cursor_x_offset + n - 1, self.cursor_y + self.cursor_y_offset)
            else:
                screen.apply_mask_to_render(render, '■', "YELLOW", self.cursor_x + self.cursor_x_offset, self.cursor_y + self.cursor_y_offset)

        if key == " ":
            if self.place == True:
                self.cursor_char = "O"
                self.shoot(self.cursor_x, self.cursor_y, board_obj, fleet_obj)
                self.shooted = True
            else:
                return [self.cursor_x, self.cursor_y]
        else:
            self.shooted = False
        if key == "r" or key == "R":
            if self.place == False:
                return ["dir_change"]

    def shoot(self, x, y, board_obj, fleet):
        #playsound("sounds/Catapult.wav")
        multi_playsound("sounds/Catapult.wav")
        i = board_obj.plansza[y][int(x/2)]
        if  i != [0] and i != ['o'] and i != ['x']:
            board_obj.plansza[y][int(x/2)] = ['x']
            fleet[i[0]-1].damage_ship(i[1])
            #playsound("sounds/Explode.wav")
        if i == [0]:
            board_obj.plansza[y][int(x/2)] = ['o']
            #playsound("sounds/Oilplat.wav")

    def next_player(self):
        return self.shooted

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