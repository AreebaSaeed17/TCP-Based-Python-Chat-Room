import socket

server_socket = socket.socket()                 # create a socket using constructor from socket class
server_name = socket.gethostname()              # get the name of host machine
server_ip = socket.gethostbyname(server_name)   # get the ip address of that host by passing ita name
port = 8080                                     # using the standard available port


# bind the created socket with the host
# this will set up our socket at the server end so now the client can connect to this server

# the bind function takes one argument only so im wrapping the servername and port as one
server_socket.bind((server_ip, port))
print ("Socket at host end binded successfully.\n")     # print a msg for confirmation
print("The IP Address is:" + server_name)
print("The IP Address is:" + server_ip)
print("The port number is: " + str(port))

# now ill configure the socket to listen for incoming connections
print("Enter your name below so that clients can know your name while communicating.\n")
name_ServerEnd = input("Enter your name: ")
server_socket.listen(1)                                 # listen activates the socket to receive incoming connections
                                                        # arg passed is 1 which means it will form one connection at a time

# create connection with a client
# clientsocket creates a new socket
# client address holds both ip addr and port (ip, port)
# server_socket.accept( ) will accept that connection onto the socket

client_socket, client_address = server_socket.accept()

print("The server socket is receiving any incoming connection from " + client_address[0] + "\n")
print("Connection Established.\nConnected from " + client_address[0] + "\n")

# make the server store the incoming connections

# store the incoming msg into client_msg variable
# from the client socket that connected to the server, receive upto 1024bytes at a time
# decode it from bytes to readable language by decode function
client_msg = (client_socket.recv(1024)).decode()      
print(client_address[0]+ " has connected.\n")
print("The message received is as follows:\n")
print(client_msg)

# send name of server back
client_socket.send(name_ServerEnd.encode())


# Now delievering msgs
while True:
    msg_fromServer = input("ME: ")
    client_socket.send(msg_fromServer.encode())            # sending encoded msg to client

    if msg_fromServer.lower() == 'exit':
        print("Closing server...")                         # if server wants to end convo
        break

    msg_fromClient = (client_socket.recv(1024)).decode()   # receive and decode msg from client
    print("Client: " + msg_fromClient)

    if not msg_fromClient:
        print("Client disconnected abruptly.")             # sudden disconnection
        break



