import socket
from _thread import *
import sys

server = socket.gethostbyname(socket.gethostname())
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")
print(server, port)

ready = [False, False]

conn = [[], []]
addr = [[], []]
players = 2

for n in range(players):
    try:
        conn[n], addr[n] = s.accept()
        print("Connected to:", addr[n])
        conn[n].send(str.encode(n))
    except:
        pass

while ready[0] == False and ready[1] == False:
    for n in range(players):
        try:
            odp = conn[n].recv(2048).decode()
            print(odp)
            if odp == "ready":
                ready[n] = True
                conn[n].send(str.encode(n))
        except:
            pass

try:
    conn[0].send(str.encode("0"))
    conn[1].send(str.encode("1"))
except:
    pass

while True:
    try:
        odp = conn[0].recv(2048).decode()
        conn[1].send(str.encode(odp))
        print(odp, "Direction: 0->1")
        odp = conn[1].recv(2048).decode()
        conn[0].send(str.encode(odp))
        print(odp, "Direction: 1->0")

        odp = conn[1].recv(2048).decode()
        conn[0].send(str.encode(odp))
        print(odp, "Direction: 1->0")
        odp = conn[0].recv(2048).decode()
        conn[1].send(str.encode(odp))
        print(odp, "Direction: 0->1")
        if "lost" in odp:
            break
    except:
        print("connection lost")
        break

for n, m in enumerate(conn, 0):
    conn[n].close()