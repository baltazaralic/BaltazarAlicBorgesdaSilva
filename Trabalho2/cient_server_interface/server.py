import socket
import threading
import time
from get_html import *

SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 7555
ADDR = (SERVER_IP, PORT)
FORMATO = 'utf-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

conexoes = []
msg = ""

def get_comando():
    global msg
    while True:
        if msg == "":
            msg = get_html_f()

def handle_clientes(conn, addr):
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}")
    global conexoes
    global msg
    nome = "False"
    
    time.sleep(0.2)
    nome = conn.recv(1024).decode(FORMATO)
    mensagem_separada = nome.split("=")
    if len(mensagem_separada) > 1:
        nome = mensagem_separada[1]
    mapa_da_conexao = {
          "conn": conn,
          "addr": addr,
          "nome": nome,
          "status": False
    }
    conexoes.append(mapa_da_conexao)

    while(True):
        if msg.startswith(nome) and nome != "False":
              mensagem_separada = msg.split("=")
              if mensagem_separada[1]:
                   if mensagem_separada[1] == "True":
                         mapa_da_conexao["status"] = True
                   elif mensagem_separada[1] == "False":
                         mapa_da_conexao["status"] = False
                   conn.send(mensagem_separada[1].encode(FORMATO))
                   msg = ""
                   time.sleep(0.2)
        elif nome == "False":
            break
            

def start():
    print("[INICIANDO] Iniciando Socket")
    print(SERVER_IP)
    server.listen()
    thread2 = threading.Thread(target=get_comando, args=())
    thread2.start()
    while(True):
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))
        thread.start()

start()