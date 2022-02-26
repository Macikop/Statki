import socket

class Network:
    def __init__(self, ip):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip
        self.port = 5555
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.client.connect(self.addr)
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
            return "error"

    def recive(self):
        try:
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
            return "error"

    def pure_send(self, data):
        try:
            self.client.send(str.encode(data))
        except socket.error as e:
            print(e)
            return "error"

    def __del__(self):
        self.client.close()