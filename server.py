import socket

server_socket = socket.socket()                 # create a socket using constructor from socket class
server_name = socket.gethostname()              # get the name of host machine
server_ip = socket.gethostbyname(server_name)   # get the ip address of that host by passing ita name
port = 8080                                     # using the standard available port


# bind the created socket with the host
# this will setup our socket at the host end so now the client can connect to this server

# the bind function takes one argument only so im wrapping the servername and port as one
server_socket.bind((server_name, port))
print ("Socket at host end binded successfully.\n")     # print a msg for confirmation
print("The IP Address is:" + server_name)
print("The IP Address is:" + server_ip)
print("The port number is: " + str(port))

# now ill configure the socket tos listen for incoming connections\
cli_name = input("Enter your name: ")
server_socket.listen(5)             # listen activates the socket to receive incoming connections

# create connection with a client
# clientsocket creates a new socket
# client address holds both ip addr and port (ip, port)
# server_socket.accept( ) will accept that connection onto the socket

client_socket, client_address = server_socket.accept()

print("The server socket is receiving any incoming connection from " + client_address[0])
print("Connection Established.\nConnected from " + client_address[0])

# make the server store the incoming connections

# receive the connction on a buffer of 1024 bytes
client = (client_socket.recv(1024)).decode()        



