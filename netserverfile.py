import socket

#  Setting the host, port and the size
host = "localhost"
port = 8890
size = 512


#   Step 1 (Initializing the socket)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#   Step 2 (Binding the socket to the address)
mysock.bind((host, port))
mysock.listen(4)

#   Step 3 (Accepting the connection)
c, addr = mysock.accept()

#   Step 4 (Receiving the data)
data = c.recv(size)
if data:
    fileone = open("buffer.txt", "+w")
    print("Connection received from: ", addr[0])
    fileone.write(addr[0])
    fileone.write(" : ")
    fileone.write(data.decode("utf-8"))
    fileone.close()
mysock.close()