#!/usr/bin/env python3
import socket
import sys

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 40000           # Porta que o Servidor esta

if len(sys.argv) > 1:
    HOST = sys.argv[1]
serv = (HOST, PORT)
print('Conectando ao servidor', serv)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(serv)
while True:
    try:
        msg = input('Mensagem (Ctrl+D encerra): ')
    except: break
    sock.send(str.encode(msg))
    msg = sock.recv(1024)
    if msg:
        msg = msg.decode()
        print('Recebi:', msg)
sock.close()