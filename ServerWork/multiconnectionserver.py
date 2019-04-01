"""
Simple multi-connection server


"""

import selectors
sel = selectors.DefaultSelector()
import socket
messages = [b'Message 1 from client.',b'Message 2 from client']

def accept_wrapper(sock):
    conn, addr = sock.accept()
    print('accepted connection from', addr)
    conn.setblocking(False)
    data = types.SimpleNamespace(addr=addr, inb=b'',outb=b'')
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    sel.register(conn, events,data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)
        if recv_data:
            data.outb += recv_data
        else:
            print('closing connection to', data.addr)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print('echoing', repr(data.outb), 'to', data.addr)
            sent = sock.send(data.outb) #Shoud be ready to write
            data.outb = data.outb[sent:]

def start_connection(host, port, num_conns):
    server_addr = (host,port)
    for i in range(0, num_conns):
        connid = i+1
        print('starting connection', connid, 'to',server_addr)
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #inclomplete

def main():
    HOST = "127.0.0.1" #local host to loopback to
    PORT = 6555 #any port above 1023 are not binded

    lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    lsock.bind((HOST, PORT))
    lsock.listen()
    print('listening on ', (HOST, PORT))
    lsock.setblocking(False)
    sel.register(lsock, selectors.EVENT_READ, data=None)#registers the socket to be monitored

    while True:
        events = sel.select(timeout=None)# what is being monitored. this blocks until there are sockets ready for  I/O
        for key, mask in events:
            if key.data is None:# if this is true then we know its form the listening socket and we to accept()
                accept_wrapper(key.fileobj)
            else:
                service_connection(key,mask)
                #if its not none then we know it's a client socket that's already been accpetd and we need to service itself.

if __name__ == "__main__":
    main()
