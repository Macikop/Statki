import os
import sys
import winsound
import msvcrt
import time

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
        os.system("play " + file)

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
        #sleep(0.1)

def key_detect():
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
            