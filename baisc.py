import os
import sys
import time
import threading
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
    "WHITE" : '\033[97m',
}

more_colors = {
    "PURPLE" : '\033[95m',
    "BLUE" : '\033[94m',
    "CYAN" : '\033[96m',
    "GREEN" : '\033[92m',
    "YELLOW" : '\033[93m',
    "RED" : '\033[91m',
    "WHITE" : '\033[0m',
    "YELLOW_ON_BLUE" : '\033[93;104m',
    "PURPLE_ON_BLUE" : '\033[95;104m',
    "RED_ON_BLUE" : '\033[91;104m',
    "WHITE_ON_BLUE" : '\033[97;104m'

}

lirterki_dict = {}

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
        os.system("aplay " + os.path.join(sys.path[0],file + " > /dev/null 2>&1 &"))

def print_at(x, y, message):
    print(f'\033[{y};{x}H'+message, end='')


def display(text, color = "WHITE", newline = True):
    if newline == True:
        print(f"{more_colors[color]}{text}\033[0m")
    else:
        print(f"{more_colors[color]}{text}\033[0m", end='')

def display_at(x, y, message, color = "WHITE", newline = True):
    if newline == True:
        print(f'{more_colors[color]}\033[{y};{x}H'+  message + '\033[0m', end='', flush= True)
    else: 
        print(f'{more_colors[color]}\033[{y};{x}H'+  message + '\033[0m', end='', flush= True)

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

def load_lirterki_new():
    global lirterki_dict
    lirterki_dict.clear()
    #word = word.upper()
    with open(os.path.join(sys.path[0], "More_literki.txt"),encoding="utf-8") as file:
        file_content = file.readlines()
        header = file_content[0].split("█")

        letters = file_content[2:]

        for index, line in enumerate(letters):
            letters[index] = line.split('%')

        for index, char in enumerate(header):
            letter = []
            for line in letters:
                letter.append(line[index])

            lirterki_dict.update({char : letter })

load_lirterki_new()

def lirterki_render(word, color = "WHITE"):
    global lirterki_dict
    global colors
    render = [[],[],[],[],[],[],[],[],[]]
    word = word.upper()
    if color != "RAINBOW":
        for letter in word:
            big_letter = lirterki_dict[letter]
            for i, line in enumerate(render):
                render[i].append([big_letter[i], color])
    else:
        key = list(colors.keys())
        key_len = len(key)
        tup = []
        for i, letter in enumerate(word,):
            if i < key_len:
                i = i
            else:
                i = i - (int(i/key_len)*key_len)
            tup.append([letter, key[i]])
        for letter in tup:
                big_letter = lirterki_dict[letter[0]]
                for i, line in enumerate(render):
                    render[i].append([big_letter[i], letter[1]])

    return render

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

def image_to_render(file_name, color):
    render = []
    with open(os.path.join(sys.path[0], file_name)) as file:
        lines = file.readlines()
        for line in lines:
            render_line = []
            for char in line:
                render_line.append([char, color])
            render.append(render_line)
    return render
                

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
    
    def apply_mask_to_render(self, render, mod, color, x, y):
        render[y][x][0] = mod
        render[y][x][1] = color

    def __del__ (self):
        clear()