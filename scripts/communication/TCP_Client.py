#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import time

HOST = '127.0.0.2'
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('connecting to %s port ' + str(server_address))
s.connect(server_address)

try:
    while True:
        s.sendall(b'Hello, World')

        data = s.recv(1024)
        print('Server: ', data.decode("utf8"))
        time.sleep(2)
finally:
    s.close()