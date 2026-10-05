import socket

server_socket = socket.socket()                 # create a socket using constructor from socket class
server_name = socket.gethostname()              # get the name of host machine
server_ip = socket.gethostbyname(server_name)   # get the ip address of that host by passing ita name
port = 8080                                     # using the standard available port


# bind the created socket with the host
# this will setup our socket at the host end so now the client can connect to this server

server_socket.bind(server_name, server_ip)
print ("Socket at host end binded successfully.\n")     # print a msg for confirmation
print("The IP Address is:" + server_name)
print("The IP Address is:" + server_ip)
print("The port number is:" + port)

# now ill configure the socket to listen for incoming connections\
cli_name = input("Enter your name: ")
server_socket.listen(5)             # listen activates the socket to receive incoming connections

# create connection with a client
# clientsocket creates a new socket
# client address holds both ip addr and port (ip, port)
# server_socket.accept( ) will accept that connection onto the socket
client_socket, client_address = server_socket.accept()

print("The server socket is receiving any incoming connection from " + client_address[0])
print("Connected from " + client_address[0])
