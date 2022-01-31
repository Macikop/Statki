import os
import sys
import time
if os.name == 'nt':
    import winsound
    import msvcrt      
else:
    import termios
    import tty

colors = {
    "PURPLE" : '\033[95m',
    "BLUE" : '\033[94m',
    "CYAN" : '\033[96m',
    "GREEN" : '\033[92m',
    "YELLOW" : '\033[93m',
    "RED" : '\033[91m',
    "WHITE" : '\033[0m',
    "BOLD" : '\033[1m',
    "UNDERLINE" : '\033[4m'
}

def wait(time_s):
        animation = "|/-\\"
        for i in range(time_s):
            time.sleep(0.1)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print ("End!")
        print ("\033[A                             \033[A")

def clear():
    if os.name == 'nt':
        _ = os.system('cls')   #windows
    else:
        _ = os.system('clear') #linux

def playsound(file):
    if os.name == 'nt':
        winsound.PlaySound(file, winsound.SND_FILENAME)
    else:
        os.system("aplay " + os.path.join(sys.path[0],file))

def print_at(x, y, message):
    print(f'\033[{y};{x}H'+message, end='')


def display(text, color = "WHITE", newline = True):
    if newline == True:
        print(f"{colors[color]}{text}{colors['WHITE']}")
    else:
        print(f"{colors[color]}{text}{colors['WHITE']}", end='')

def display_at(x, y, message, color = "WHITE", newline = True):
    if newline == True:
        print(f'{colors[color]}\033[{y};{x}H'+  message + '\033[0m', end='', flush= True)
    else: 
        print(f'{colors[color]}\033[{y};{x}H'+  message + '\033[0m', end='', flush= True)

def lirterki(word):
    word = word.upper()
    with open(os.path.join(sys.path[0], "Literki.txt")) as file:
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


def key_detect():
    if os.name == 'nt':
        repeat = True
        m = None
        n = None
        last_m = None
        while repeat == True:
            if msvcrt.kbhit():
                ch = msvcrt.getch()
                m = str(ch)
                if m == "b'\\xe0'":
                    n = str(ch)
                elif last_m != "b'\\xe0'":
                    n = None
                if n == "b'\\xe0'" and m == "b'M'":
                    return "right"
                elif n == "b'\\xe0'" and m == "b'P'":
                    return "down"
                elif n == "b'\\xe0'" and m == "b'H'":
                    return "up"
                elif n == "b'\\xe0'" and m == "b'K'":
                    return "left"
                elif m != "b'\\xe0'" and n == None:
                    m = m[1:]
                    m = m.replace("'", "")
                    return m
                last_m = m
    else:
        orig_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)
        x = 0
        m = 1
        n = 1
        returner = ''
        while True:
            x=sys.stdin.read(1)[0]
            if x == chr(27):
                m = x
            elif m == chr(27):
                n = x
                if n == "[":
                    x=sys.stdin.read(1)[0]
                    if x == 'A':
                        returner = "up"
                    elif x == 'B':
                        returner = "down"
                    elif x == 'C':
                        returner = "right"
                    elif x == 'D':
                        returner = "left"
                    n = 0
                m = 0
                x = 0
            else:
                returner = x
            if returner != '':
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
                return returner
            
def print_image(file_name):
    with open(os.path.join(sys.path[0], file_name)) as file:
        lines = file.readlines()
        for n in lines:
            for chars in n:
                print(chars, end='')
    print("\n")

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

    def __del__ (self):
        clear()