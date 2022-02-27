from baisc import clear, display, key_detect, display_at, playsound, wait, screen
import network
import random
import time
import multiprocessing

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
                            col = "RED_ON_BLUE"
                        elif u[0] == 'd':
                            tile = '●'
                            col = "WHITE_ON_BLUE"
                        else:
                            tile = 'o'
                            col = "PURPLE_ON_BLUE"
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
                                line.append(["■", "YELLOW_ON_BLUE"])

                            elif position == True:
                                line.append([water, "BLUE"])
                                line.append(["█", "YELLOW_ON_BLUE"])
                            else:
                                line.append(["▬", "YELLOW_ON_BLUE"])
                                line.append(["▬", "YELLOW_ON_BLUE"])
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
                            col = "RED_ON_BLUE"
                        elif u[0] == 'o':
                            tile = 'o'
                            col = "PURPLE_ON_BLUE"
                        elif u[0] == 'd':
                            tile = '●'
                            col = "WHITE_ON_BLUE"
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
                                line.append(["■", "YELLOW_ON_BLUE"])
                            else:
                                line.append(["▬", "YELLOW_ON_BLUE"])
                                line.append(["▬", "YELLOW_ON_BLUE"])
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
                if word == [0] or word == ['x'] or word == ['o'] or word ==['d']:
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
    ship_char = "█"

    def __init__(self, sound, size=1):
        self.damage = []
        self.allow_sound = sound
        self.size = size

    def set_place(self, x, y, size, direction):
        self.sound = None
        self.dir = direction
        self.damage = []
        self.size = size
        if self.size == 1:
            self.ship_char = "■"
        else:
            if self.dir == True:
                self.ship_char = "█"
            else:
                self.set_char = "▬"
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
            self.sound = None
            self.status = False
            self.sound = None
            if self.allow_sound == True:
                self.sound = multiprocessing.Process(target= self.multisound, args=("sounds/Shipsink.wav",), daemon= True)
                self.sound.start()
            self.ship_char = "x"
            return True
        return False

    def destroy(self):
        self.status = False

    def multisound(self, sound):
        time.sleep(1)
        playsound(sound)

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
        allow_sound = bool(settings['sound'])
        self.team_a_fleet = self.create_fleet(self.number_of_ships, allow_sound)
        self.team_b_fleet = self.create_fleet(self.number_of_ships, allow_sound)
        self.plansza_a = board()
        self.plansza_b = board()
        self.place = settings["auto_placement"]
        self.mode = settings["mode"]
        self.cursor_a = cursor(True, allow_sound, self.mode)
        self.cursor_b = cursor(True, allow_sound, self.mode)
        if settings["mode"] == 3:
            self.opponent = remote_player(settings["server_ip"], allow_sound)
        if self.place == True:
            if settings["mode"] != 3:
                self.random_ship_placement(self.plansza_a, self.team_a_fleet)
                self.random_ship_placement(self.plansza_b, self.team_b_fleet)
            else:
                self.random_ship_placement(self.plansza_a, self.team_a_fleet)
        else:
            if settings["mode"] == 2:
                self.actual_player = True
                if self.actual_player == True:
                    self.manual_ship_placement(self.plansza_a, self.team_a_fleet)
                    self.actual_player = False
                if self.actual_player == False:
                    self.manual_ship_placement(self.plansza_b, self.team_b_fleet)
                self.place = True
            elif settings["mode"] == 1:
                self.actual_player = True
                if self.actual_player == True:
                    self.manual_ship_placement(self.plansza_a, self.team_a_fleet)
                    self.actual_player = False
                self.random_ship_placement(self.plansza_b, self.team_b_fleet)
                self.place = True
            else:
                self.actual_player = True
                if self.actual_player == True:
                    self.manual_ship_placement(self.plansza_a, self.team_a_fleet)
                    self.actual_player = False
                self.place = True
        clear()
        display_at(70, 10, "strzałki - przesuwanie statku")
        display_at(70, 11, "spacja - strzał")
        if settings["mode"] == 1:
            render_a = self.plansza_a.render_board(self.team_a_fleet, True)
            render_b = self.plansza_b.render_board(self.team_b_fleet, False)
            fleet_a_render = self.fleet_status_render(self.team_a_fleet)
            fleet_b_render = self.fleet_status_render(self.team_b_fleet)
        elif settings["mode"] == 2:
            display_at(0, 1, "Gracz 1")
            display_at(0, 2, "Naciśnij ENTER")
            key_detect()
            render_a = self.plansza_a.render_board(self.team_a_fleet, True)
            render_b = self.plansza_b.render_board(self.team_b_fleet, False)
            fleet_a_render = self.fleet_status_render(self.team_a_fleet)
            fleet_b_render = self.fleet_status_render(self.team_b_fleet)
        else:
            self.first = int(self.opponent.ready())
            render_a = self.plansza_a.render_board(self.team_a_fleet, True)
            render_b = self.plansza_b.render_board(self.team_b_fleet, False)
            fleet_a_render = self.fleet_status_render(self.team_a_fleet)
            fleet_b_render = self.fleet_status_render(self.team_b_fleet)
        self.actual_player = False
        last_player = False
        end = True
        if settings["mode"] == 3:
            if self.first == 1:
                self.actual_player = True
            else:
                self.actual_player = False
        while end == True:
            if settings["mode"] == 2:
                if last_player == True and self.actual_player == False:
                    render_a = self.plansza_a.render_board(self.team_a_fleet, False)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, True)
                    fleet_a_render = self.fleet_status_render(self.team_a_fleet)
                    fleet_b_render = self.fleet_status_render(self.team_b_fleet)
                    self.scr.display_board_from_render(render_a, 0, 0)
                    self.scr.display_board_from_render(render_b, 40, 0)
                    self.scr.display_board_from_render(fleet_a_render, 25, 0)
                    self.scr.display_board_from_render(fleet_b_render, 65, 0)
                    render_a = self.plansza_a.render_board(self.team_a_fleet, True)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, False)
                    fleet_a_render = self.fleet_status_render(self.team_a_fleet)
                    fleet_b_render = self.fleet_status_render(self.team_b_fleet)
                    time.sleep(1)
                    clear()
                    display_at(0, 1, "Gracz 1")
                    display_at(0, 2, "Naciśnij ENTER")
                    key_detect()
                elif last_player == False and self.actual_player == True:
                    render_a = self.plansza_a.render_board(self.team_a_fleet, True)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, False)
                    fleet_a_render = self.fleet_status_render(self.team_a_fleet)
                    fleet_b_render = self.fleet_status_render(self.team_b_fleet)
                    self.scr.display_board_from_render(render_a, 0, 0)
                    self.scr.display_board_from_render(render_b, 40, 0)
                    self.scr.display_board_from_render(fleet_a_render, 25, 0)
                    self.scr.display_board_from_render(fleet_b_render, 65, 0)
                    render_a = self.plansza_a.render_board(self.team_a_fleet, False)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, True)
                    fleet_a_render = self.fleet_status_render(self.team_a_fleet)
                    fleet_b_render = self.fleet_status_render(self.team_b_fleet)
                    time.sleep(1)
                    clear()
                    display_at(0, 1, "Gracz 2")
                    display_at(0, 2, "Naciśnij ENTER")
                    key_detect()
            self.scr.display_board_from_render(render_a, 0, 0)
            self.scr.display_board_from_render(render_b, 40, 0)
            self.scr.display_board_from_render(fleet_a_render, 25, 0)
            self.scr.display_board_from_render(fleet_b_render, 65, 0)
            if settings["mode"] == 1:
                render_a = self.plansza_a.render_board(self.team_a_fleet, True)
                render_b = self.plansza_b.render_board(self.team_b_fleet, False)
                fleet_a_render = self.fleet_status_render(self.team_a_fleet)
                fleet_b_render = self.fleet_status_render(self.team_b_fleet)
                if self.actual_player == True:
                    bot.easy_bot(self.plansza_a, self.team_a_fleet)
                    self.change_player()
                else:
                    self.cursor_b.cursor_move(self.scr, render_b, self.plansza_b, self.team_b_fleet)
                    if self.cursor_b.next_player() == True:
                        self.change_player()

            elif settings["mode"] == 2:
                if self.actual_player == True:
                    render_a = self.plansza_a.render_board(self.team_a_fleet, False)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, True)
                    fleet_a_render = self.fleet_status_render(self.team_a_fleet)
                    fleet_b_render = self.fleet_status_render(self.team_b_fleet)
                else:
                    render_a = self.plansza_a.render_board(self.team_a_fleet, True)
                    render_b = self.plansza_b.render_board(self.team_b_fleet, False)
                    fleet_a_render = self.fleet_status_render(self.team_a_fleet)
                    fleet_b_render = self.fleet_status_render(self.team_b_fleet)
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

            elif settings["mode"] == 3:
                render_a = self.plansza_a.render_board(self.team_a_fleet, True)
                render_b = self.plansza_b.render_board(self.team_b_fleet, False)
                fleet_a_render = self.fleet_status_render(self.team_a_fleet)
                fleet_b_render = self.fleet_status_render(self.team_b_fleet)

                if self.actual_player == False:
                    pos = self.cursor_b.cursor_move(self.scr, render_b, self.plansza_b, self.team_b_fleet)
                    if pos != None:
                        self.opponent.push(int(pos[0]/2), pos[1], self.plansza_b, self.team_b_fleet)
                    if self.cursor_b.next_player() == True:
                        self.change_player()
                        render_a = self.plansza_a.render_board(self.team_a_fleet, True)
                        render_b = self.plansza_b.render_board(self.team_b_fleet, False)
                        fleet_a_render = self.fleet_status_render(self.team_a_fleet)
                        fleet_b_render = self.fleet_status_render(self.team_b_fleet)
                else:
                    display_at(40, 15, "Czekanie na ruch przeciwnika")
                    self.opponent.get(self.plansza_a, self.team_a_fleet)
                    self.change_player()
                    display_at(40, 15, "                            ")
            if settings["mode"] != 3:
                end_a = self.plansza_a.check_end()
                end_b = self.plansza_b.check_end()
            else:
                end_a = self.fleet_check_end(self.team_a_fleet)
                end_b = self.fleet_check_end(self.team_b_fleet)
            if end_a == False or end_b == False:
                end = False
        del self.scr
        if end_a == False:
            return False
        else:
            return True
        
    def create_fleet (self, n, sound):
        returner = []
        i = 4
        counter = 0
        for _ in range(n):
            returner.append(ship(sound, i))
            counter = counter + 1
            if i == 4 and counter == 1:
                i = i - 1
            elif i == 3 and counter == 3:
                i = i - 1
            elif i == 2 and counter == 6:
                i = i - 1
        return returner
    
    def fleet_check_end(self, fleet):
        returner = True
        for ship in fleet:
            if ship.status == True:
                return True
            else:
                returner = False
        return returner

    def manual_ship_placement(self, board_obj, fleet_obj):
        common_cursor = cursor(False, False, None)
        n = 0
        miss = True
        direction = True
        render = board_obj.render_board(fleet_obj, True)
        display_at(40, 5, "strzałki - przesuwanie statku")
        display_at(40, 6, "r - obrót statku")
        display_at(40, 7, "spacja - zatwierdzenie pozycji statku")
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

    def fleet_status_render(self, fleet):
        frigate_num = 0
        destroyer_num = 0
        cruiser_num = 0
        battleship_num = 0
        for n, ship in enumerate(fleet):
            if ship.size == 4 and ship.status == True:
                battleship_num = battleship_num + 1
            elif ship.size == 3 and ship.status == True:
                cruiser_num = cruiser_num + 1
            elif ship.size == 2 and ship.status == True:
                destroyer_num = destroyer_num + 1
            elif ship.size == 1 and ship.status == True:
                frigate_num = frigate_num + 1
        pla = []
        pla.append([["╔══════════╗", "WHITE"]])
        pla.append([["║ ", "WHITE"],["▬▬▬▬ ", "YELLOW"], ["x " + str(battleship_num), "WHITE"], [" ║", "WHITE"]])
        pla.append([["║ ", "WHITE"],["▬▬▬  ", "YELLOW"], ["x " + str(cruiser_num), "WHITE"], [" ║", "WHITE"]])
        pla.append([["║ ", "WHITE"],["▬▬   ", "YELLOW"], ["x " + str(destroyer_num), "WHITE"], [" ║", "WHITE"]])
        pla.append([["║ ", "WHITE"],["■    ", "YELLOW"], ["x " + str(frigate_num), "WHITE"], [" ║", "WHITE"]])
        pla.append([["╚══════════╝", "WHITE"]])  
        return pla


    def change_player(self):
        if self.actual_player == True:
            self.actual_player = False
        else:
            self.actual_player = True

    def __del__(self):
        if self.mode == 3:
            del self.opponent

class cursor():
    cursor_x_offset = 2
    cursor_y_offset= 2
    cursor_x = 0
    cursor_y = 0
    cursor_char = 'X' 
    shooted = False
    
    def __init__(self, place, sound, mode):
        self.place = place
        self.allow_sound = sound
        self.mode = mode

    def multi_sound(self, sound):
        playsound(sound)

    def slow_multi_sound(self, sound):
        time.sleep(0.5)
        playsound(sound)

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
        display_at(20, 15, "                                        ", "WHITE")
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
            screen.apply_mask_to_render(render, 'X', "WHITE_ON_BLUE", self.cursor_x + self.cursor_x_offset, self.cursor_y + self.cursor_y_offset)
        else:
            if size != 1:
                if dir == True:
                    for n in range(size):
                        screen.apply_mask_to_render(render, '█', "YELLOW_ON_BLUE", self.cursor_x + self.cursor_x_offset, self.cursor_y + self.cursor_y_offset + n)
                else:
                    for n in range(size*2):
                        screen.apply_mask_to_render(render, '▬', "YELLOW_ON_BLUE", self.cursor_x + self.cursor_x_offset + n - 1, self.cursor_y + self.cursor_y_offset)
            else:
                screen.apply_mask_to_render(render, '■', "YELLOW_ON_BLUE", self.cursor_x + self.cursor_x_offset, self.cursor_y + self.cursor_y_offset)

        if key == " ":
            if self.place == True:
                n = board_obj.plansza[self.cursor_y][int(self.cursor_x/2)]
                if n != ['o'] and n != ['d'] and n != ['x']:
                    self.cursor_char = "O"
                    self.shoot(self.cursor_x, self.cursor_y, board_obj, fleet_obj)
                    self.shooted = True
                    return [self.cursor_x, self.cursor_y]
                else:
                    display_at(20, 15, "Nie strzela się 2 razy w to samo miejsce", "RED")
                    self.shooted = False
            else:
                return [self.cursor_x, self.cursor_y]
        else:
            self.shooted = False
        if key == "r" or key == "R":
            if self.place == False:
                return ["dir_change"]

    def shoot(self, x, y, board_obj, fleet):
        #playsound("sounds/Catapult.wav")
        if self.allow_sound == True:
            self.shoot_sound = multiprocessing.Process(target=self.multi_sound, args=("sounds/Catapult.wav",), daemon= True)
            self.hit_sound = multiprocessing.Process(target=self.slow_multi_sound, args=("sounds/Explode.wav",), daemon= True)
            self.miss_sound = multiprocessing.Process(target=self.slow_multi_sound, args=("sounds/Oilplat.wav",), daemon= True)
            self.shoot_sound.start()
        i = board_obj.plansza[y][int(x/2)]
        if  i != [0] and i != ['o'] and i != ['x'] and i != ['d']:
            destroyed = fleet[i[0]-1].damage_ship(i[1])
            if destroyed == True:
                x = fleet[i[0]-1].pos_x
                y = fleet[i[0]-1].pos_y
                board_obj.plansza[y][x] = ['d']
                if fleet[i[0]-1].dir == True:
                    for tile in range(fleet[i[0]-1].size):
                        board_obj.plansza[y+tile][x] = ['d']
                else:
                    for tile in range(fleet[i[0]-1].size):
                        board_obj.plansza[y][x+tile] = ['d']
            else:
                board_obj.plansza[y][int(x/2)] = ['x']
            #playsound("sounds/Explode.wav")
            if self.allow_sound == True:
                self.shoot_sound = None
                if self.mode != 3:
                    self.hit_sound.start()
        if i == [0]:
            board_obj.plansza[y][int(x/2)] = ['o']
            #playsound("sounds/Oilplat.wav")
            if self.allow_sound == True:
                self.shoot_sound = None
                if self.mode != 3:
                    self.miss_sound.start()
        if self.allow_sound == True:
            self.hit_sound = None
            self.miss_sound = None

    def next_player(self):
        return self.shooted

class enemy():
    def __init__(self):
        self.known_board = []
        self.past_moves = []

    def shoot (self, x, y, enemy_board, enemy_fleet):
        i = enemy_board.plansza[y][x]
        if i != [0] and i != ['d']:
            destroyed = enemy_fleet[i[0]-1].damage_ship(i[1])
            if destroyed == True:
                x = enemy_fleet[i[0]-1].pos_x
                y = enemy_fleet[i[0]-1].pos_y
                enemy_board.plansza[y][x] = ['d']
                if enemy_fleet[i[0]-1].dir == False:
                    for tile in range(enemy_fleet[i[0]-1].size):
                        enemy_board.plansza[y][x+tile] = ['d']
                else:
                    for tile in range(enemy_fleet[i[0]-1].size):
                        enemy_board.plansza[y+tile][x] = ['d']
            else:
                enemy_board.plansza[y][x] = ['x']
        else:
            enemy_board.plansza[y][x] = ['o']

    def easy_bot(self, enemy_board, enemy_fleet):
        repeat = False
        while repeat == False:
            x = random.randint(0, board.size_x-1)
            y = random.randint(0, board.size_y-1)
            if [x, y] in self.past_moves:
                repeat = False
            else:
                repeat = True
                self.past_moves.append([x, y])
                self.shoot(x, y, enemy_board, enemy_fleet)

class remote_player():
    def __init__(self, ip, sound):
        self.n = network.Network(ip)
        self.allow_sound = sound

    def slow_multi_sound(self, sound):
        time.sleep(0.5)
        playsound(sound)

    def get_shoot (self, x, y, enemy_board, enemy_fleet):
        i = enemy_board.plansza[y][x]
        if i != [0] and i != ['d']:
            destroyed = enemy_fleet[i[0]-1].damage_ship(i[1])
            if destroyed == True:
                x = enemy_fleet[i[0]-1].pos_x
                y = enemy_fleet[i[0]-1].pos_y
                enemy_board.plansza[y][x] = ['d']
                if enemy_fleet[i[0]-1].dir == False:
                    for tile in range(enemy_fleet[i[0]-1].size):
                        enemy_board.plansza[y][x+tile] = ['d']
                else:
                    for tile in range(enemy_fleet[i[0]-1].size):
                        enemy_board.plansza[y+tile][x] = ['d']
                return f"destroyed {x} {y} {enemy_fleet[i[0]-1].dir} {enemy_fleet[i[0]-1].size} {i[0]}" 
            else:
                enemy_board.plansza[y][x] = ['x']
                return "hit"
        else:
            enemy_board.plansza[y][x] = ['o']
            return "miss"

    def shoot(self, x, y, hit, enemy_board, enemy_fleet):
        self.hit_sound = multiprocessing.Process(target=self.slow_multi_sound, args=("sounds/Explode.wav",), daemon= True)
        self.miss_sound = multiprocessing.Process(target=self.slow_multi_sound, args=("sounds/Oilplat.wav",), daemon= True)
        if hit == True:
            enemy_board.plansza[y][x] = ['x']
            self.hit_sound.start()
        else:
            enemy_board.plansza[y][x] = ['o']
            self.miss_sound.start()

        self.miss_sound = None
        self.hit_sound = None

    def destory(self, x, y, dir, size, num, enemy_board, enemy_fleet):
        self.hit_sound = multiprocessing.Process(target=self.slow_multi_sound, args=("sounds/Explode.wav",), daemon= True)
        if dir == "True":
            dir = True
        else:
            dir = False
        num = int(num)
        x = int(x)
        y = int(y)
        size = int(size)
        self.hit_sound.start()
        enemy_fleet[num-1].destroy()
        enemy_board.plansza[y][x] = ['d']
        if dir == False:
            for tile in range(size):
                enemy_board.plansza[y][x+tile] = ['d']
        else:
            for tile in range(size):
                enemy_board.plansza[y+tile][x] = ['d']
        self.hit_sound = None

    def ready(self):
        return self.n.send("ready")
        
    def push(self, x, y, enemy_board, enemy_fleet):
        recive = self.n.send("check " + str(x) + " " + str(y)).split()
        if recive[0] == "miss":
            self.shoot(x, y, False, enemy_board, enemy_fleet)
        elif recive[0] == "hit":
            self.shoot(x, y, True, enemy_board, enemy_fleet)
        elif recive[0] == "destroyed":
            self.destory(recive[1], recive[2], recive[3], recive[4], recive[5], enemy_board, enemy_fleet)

    def get(self, our_board, our_fleet):
        recive = self.n.recive().split()
        if recive[0] == "check":
            status = self.get_shoot(int(recive[1]), int(recive[2]), our_board, our_fleet)
            self.n.pure_send(status)
        #else:
        #    self.n.pure_send("invalid command")

    def __del__(self):
        del self.n