import socket, os, sys, time 

cli_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

address = ('192.168.164.138', 8008)

file = sys.argv[1]

cli_socket.sendto(file.encode('utf-8'), address)

while True: 
    data, _ = cli_socket.recvfrom(1024)
    if not data:
        break
    os.write(sys.stdout.fileno() ,data)
cli_socket.close()
