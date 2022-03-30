import socket
import threading
import time



PORT = 7555
FORMATO = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)



class client():
    def __init__(self, nome):
        self.nome = nome
        self.cliente = False
        self.msg = ""
        self.state = False

    def enviar(self):
        self.cliente.send(self.msg.encode(FORMATO))

    def iniciar(self):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.connect(ADDR)
        thread = threading.Thread(target=self.handle_mensagens, args=())
        thread.start()

    def handle_mensagens(self):
         self.msg = "nome" + "=" + self.nome
         print(self.msg)
         self.enviar()
         while(True):
             if(len(self.nome) > 1):
                 self.msg = self.cliente.recv(1024).decode()
                 if(self.msg == "True"):
                     self.state = True
                     print(self.nome + "=" + self.msg)
                 elif(self.msg == "False"):
                     self.state = False
                     print(self.nome + "=" + self.msg)
             else:
                 break


sala = client("sala")
cozinha = client("cozinha")
quarto = client("quarto")
banheiro = client("banheiro")

time.sleep(2)
sala.iniciar()
time.sleep(2)
cozinha.iniciar()
time.sleep(2)
quarto.iniciar()
time.sleep(2)
banheiro.iniciar()



