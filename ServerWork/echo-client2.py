#!/usr/bin/env python3

import socket
 #local host to loopback to
PORT = 6644 #any port above 1023 are not binded



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('', PORT))
    s.connect(('',PORT))
    s.sendall(b'Hello World')
    data = s.recv(1024)


print('Recieved', repr(data))
