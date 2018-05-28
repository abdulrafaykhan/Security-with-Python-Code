import socket

host = "localhost"
addr = (host, 8890)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(addr)

try:
    x = bytes(input("Please enter some txt"), "utf-8")
    msg = x
    mysock.sendall(msg)
except socket.errno as e:
    print("Message sending failed!", e)
finally:
    mysock.close()
