#!/usr/bin/env python3

import socket

HOST = "127.0.0.1" #local host to loopback to
PORT = 65555 #any port above 1023 are not binded

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #SOCK_STREAM refers to TCP
    #AF_INET is refering to the Internet Addresss family for IPv4
    s.bind((HOST,PORT))#Set the host to that port whenever it is opened on the server
    #in general IPv4 assumes a 2 argument tuple and so (HOST,PORT) fills that req.
    s.listen()
    conn, addr = s.accept()
    with conn:
            print('Connection Established from', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)
