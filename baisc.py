from os import system, name
from time import sleep
import sys
import threading
import winsound

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

def playsound(file):
    if name == 'nt':
        winsound.PlaySound(file, winsound.SND_FILENAME)
    else:
        system("play " + file)

def display(text, color = "WHITE", newline = True):
    if newline == True:
        print(f"{colors[color]}{text}{colors['WHITE']}")
    else:
        print(f"{colors[color]}{text}{colors['WHITE']}", end='')

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