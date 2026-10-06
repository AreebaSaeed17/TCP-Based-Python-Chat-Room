import socket
import threading

# create a socket using socket constructor
# AF_INET specifies address family as IPv4 
# sock_stream establishes a tcp connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          

server_name = socket.gethostname()              # get the name of host machine
server_ip = socket.gethostbyname(server_name)   # get the ip address of that host by passing ita name
port = 8080                                     # using the standard available port
name_ServerEnd = input("Enter your server nickname: ")

# the bind function takes one argument only so im wrapping the servername and port as one
server_socket.bind((server_ip, port))
print ("Socket at host end binded successfully.\n")     # print a msg for confirmation
print("The IP Address is:" + server_name)
print("The IP Address is:" + server_ip)
print("The port number is: " + str(port))

# make the server listen for incoming connections from clients on its socket
server_socket.listen()                                

# creating a client dictionary to keep record of connected clients
clients = {}                           # { "username": client_socket }
client_lock = threading.Lock()         # keeps the dictionary from breaking incase of multiple new clients simultaneously being added
                                                      

# BROADCAST Function
    # using this, we can send a msg to all of the clients connected to the server at the same time

# it takes the msg as an argument
# it also takes in who sent it as an arg
# we want to share that msg to everyone connected but not back to the person who sent it
def Broadcast (message, sender_socket = None):   
    with client_lock:
        for username, client_socket in clients.items():     # loop through each client from dictionary

            try:
                if client_socket != sender_socket:          # if the client aint the one who sent the msg, it should receive the msg
                    client_socket.send(message)

            except:
                pass                                

    
# ClIENT ATTEMPT Function
    # this receives msg from a client and then sends it to everyone (basically broadcasts it)
    # this keeps running infinitely so that it can keep receiving connections
    # this runs in the bg for each client

def Client_Attempt(client_socket, client_nickname):
    while True:
        try:
            # receive the msg from client
            client_msg = client_socket.recv(1024)
            if not client_msg:
                        # If recv returns empty bytes, the client has disconnected
                            raise Exception("Disconnected")
            # if msg was existent, decode to save it
            decode_clientmsg = client_msg.decode()
            
            # send the received msg to all other connected ppl
            # print the sender name and send it onto the client socket
            formatted_msg_for_broadcast = (f"{client_nickname}: {decode_clientmsg}").encode()
            Broadcast(formatted_msg_for_broadcast, sender_socket=client_socket)

        # incase the user hasnt communicated, it has disconnected
        # remove that particular user from the dictionary
        # with client_lock ensures that this can be done for multiple users at the same time
        except:
            with client_lock:
                if client_nickname in clients:
                    del clients[client_nickname]

            # close the socket for that client
            client_socket.close()
            print(f"{client_nickname} has left the server.\n")
            
            # Notify everyone else that they left
            broadcast_leave = (f"{client_nickname} has left the chat.\n").encode()
            Broadcast(broadcast_leave)
            break                                   # destroy the thread for this user

# CONNECTION Function
    # create connection with a client
    # clientsocket creates a new socket
    # client address holds both ip addr and port (ip, port)
    # server_socket.accept( ) will accept that connection onto the socket

def Connection():
    print("The server is actively listening and awaiting connections.\n")
    while True:

        # accept connections
        client_socket, client_address = server_socket.accept()

        print("The server socket is receiving any incoming connection from " + client_address[0] + "\n")
        print("Connection Established.\nConnected from " + client_address[0] + "\n")

        # ask for client nickname
        # decode what client sent
        client_socket.send(("Enter your nickname: ").encode())
        client_nn = (client_socket.recv(1024)).decode().strip()   

        # Make sure username isn't already taken
        with client_lock:
            if client_nn.lower() == 'server' or client_nn.lower() == name_ServerEnd.lower():
                client_socket.send("ERROR: Username taken or invalid. Disconnecting...\n".encode())
                client_socket.close()
                continue
      
        # if nickname is acceptable
        clients[client_nn] = client_socket

        # tell everyone that someone joined (using broadcast func)
        # send a custom msg only to that client welcoming it
        client_socket.send("HI! You have joined the server\n Welcome!\n")
        Broadcast(client_socket + " has joined our server!\n")


        # THREAD
            # define and run one thread per client in the background
            # this will allow simultaneous communication
        
            # the target for threading is the client_attempt func bcs that it where the client is sending msgs
            # while the args begin passed is the client_socket
        thread = threading.Thread(target=Client_Attempt, args=(client_socket, client_nn))
        thread.start()



# now call the function and use it
Connection()

