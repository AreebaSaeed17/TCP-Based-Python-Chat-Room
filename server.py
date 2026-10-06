import socket
import threading

# create a socket using socket constructor
# AF_INET specifies address family as IPv4 
# sock_stream establishes a tcp connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          

server_name = socket.gethostname()              # get the name of host machine
server_ip = socket.gethostbyname(server_name)   # get the ip address of that host by passing ita name
port = 8080                                     # using the standard available port


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

    
# Client_Atempt Function
    # this receives msg from a client and then sends it to everyone (basically broadcasts it)
    # this keeps running infinitely so that it can keep receiving connections
    # this runs in the bg for each client

def Client_Attempt(client_socket, client_nickname):
    while True:
        try:
            # receive the msg from client
            client_msg = client_socket.recv(1024)
            decode_clientmsg = client_msg.decode()
            
            if not client_msg:
            # If recv returns empty bytes, the client disconnected gracefully
                raise Exception("Disconnected")
            
            formatted_msg_for_broadcast = (f"{client_nickname}: {decode_clientmsg}").encode()
           
            Broadcast(formatted_msg_for_broadcast, sender_socket=client_socket)

        # if a client fails, locate it and remove it
        except:                                                 
            index_cli = clients.index(client)
            clients.remove(client)

            print(nickname + " has left this server.\n")
            nickname = nicknames.index(index_cli)               # remove that client from both the lists
            nicknames.remove(nickname)




def Client_Attempt(client_socket, client_nickname):
    # Loop infinitely to keep receiving messages from this specific client
    while True:
        try:
            # Receive data directly from the CLIENT socket, not the server socket
            client_msg_bytes = client_socket.recv(1024)
            
            if not client_msg_bytes:
                # If recv returns empty bytes, the client disconnected gracefully
                raise Exception("Disconnected")

            # Decode message to see what they typed
            incoming_text = client_msg_bytes.decode().strip()
            
            # Format the message nicely for everyone else
            formatted_broadcast = f"{client_nickname}: {incoming_text}".encode()
            Broadcast(formatted_broadcast, sender_socket=client_socket)

        # If a client fails or disconnects, locate it and remove it cleanly
        
# CONNECTION Function
    # create connection with a client
    # clientsocket creates a new socket
    # client address holds both ip addr and port (ip, port)
    # server_socket.accept( ) will accept that connection onto the socket

def Connection_Client():
    while True:

        client_socket, client_address = server_socket.accept()

        print("The server socket is receiving any incoming connection from " + client_address[0] + "\n")
        print("Connection Established.\nConnected from " + client_address[0] + "\n")

        # ask for client nickname
        # decode what client sent
        client_socket.send(("Enter your nickname: ").encode())
        client_nn = (client_socket.recv(1024)).decode()      

        # make entry for this client
        clients.append(client_socket)
        nicknames.append(client_nn)


        # tell everyone that someone joined (using broadcast func)
        # send a custom msg only to that client welcoming it
        client_socket.send("HI! You have joined the server\n Welcome!\n")
        Broadcast(client_socket + " has joined our server!\n")


        # THREAD
            # define and run one thread per client
            # this will allow simultaneous communication
        
            # the target for threading is the connection_client func
            # while the args begin passed is the client_socket
        thread = threading.Thread(Connection_Client, args=client_socket)
        thread.start()



# now call the function and use it
Connection_Client()






# make the server store the incoming connections

# store the incoming msg into client_msg variable
# from the client socket that connected to the server, receive upto 1024bytes at a time
# decode it from bytes to readable language by decode function

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



