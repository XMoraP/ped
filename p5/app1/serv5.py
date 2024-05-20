import socket, os, time

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serv_socket.bind(('192.168.164.138', 8008))

while True:
    data_r, address = serv_socket.recvfrom(1024)
    print(address)
    if not data_r:
        break
    file = os.open(data_r.decode('utf-8'), os.O_RDONLY)
    while True: 
        data_s = os.read(file, 1024)
        if not data_s:
            serv_socket.sendto(b"", address)
            break
        serv_socket.sendto(data_s, address)
    os.close(file)

serv_socket.close()
