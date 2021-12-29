import msvcrt
import sys

while True:
    if msvcrt.kbhit():
        ch = msvcrt.getch()
        if str(ch) in '\x00\xe0':
            ch = msvcrt.getch()
        if str(ch) == 'q':
           print("Q was pressed")
        elif str(ch) == 'x':
           sys.exit()
        else:
           print("Key Pressed:", str(ch))