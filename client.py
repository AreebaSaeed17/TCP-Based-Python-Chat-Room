import socket
import threading

# create the client socket in the same format as the server socket
# AF_INET specifies the address family as IPv4 
# sock_stream establishes a tcp connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
  
client_ip = socket.gethostbyname(socket.gethostname())            # get host ip for future use
port_Server = 8080                                                  # connect to server on this port

# connect to the server
print("\n_______________________________________________________________________________\n")
print("\n.................... Welcome to the TCP Chat Room Program .....................\n")
print("\n_______________________________________________________________________________\n")
print("\nYour IP Address is: " + str(client_ip))
print("Enter your name below so that server can know your name while communicating.\n")
client_name = input("Enter your name: ")
server_ip = input("Enter the IP of the server you want to connect to: ")
server_name = input("What is the name of the host you are trying to talk to? ")


# print a msg for better User Interface
print("\n_______________________________________________________________________________\n")
print("\nAttempting to connect to " + str(server_ip) +" from " + str(client_ip) +".....\n")
print("\n_______________________________________________________________________________\n")


# connect the client socket to the server
# connect() takes only one arg so wrap the server_name and port as one
try:
    client_socket.connect((server_ip, port_Server))
    print("Successfully connected to the server!\n")

    # once client connects, give them the instructions
    print("______________ CHAT ROOM GUIDE ______________")
    print("• Type anything normally to broadcast to everyone.")
    print("• Type @username message for a private chat.")
    print("• Type /users to see who is currently online.")
    print("• Type /quit to leave the chat room gracefully.")
    print("____________________________________________\n")

except:
    print("Failed to connect to the server. Please check the IP and try again.")
    exit()

# server needs nickname so prompt will appear here
server_prompt = client_socket.recv(1024).decode()

# server is waiting for nickname, send it
client_socket.send(client_name.encode())


# RECEIVEMESSAGE FUNCTION
    # this is the baseline of this process

def Receive_Message():
    while True:
        try:
            message_fromServer = (client_socket.recv(1024)).decode()        # receive the msg from server

            # if no communication possible break out
            if not message_fromServer:
                print("Server closed the connection.")
                break

            # print whatever msg has been recieved from server
            print("\nMessage from Server: \n" + message_fromServer.strip())
            print("Your Response: ", end="", flush=True)

        except:
            break

# the requirement of the program is that the clients are able to send and receive msgs concurrently
# while I'm typing, the other client's msg can get displayed onto my screen without interrupting my typing
thread = threading.Thread(target = Receive_Message, daemon=True)
thread.start()


while True:
    try:
        my_reply = input()

        # if client want to quit
        if my_reply.strip() == '/quit':  
            print("Exiting the chat Room.\nEnding the chat...")                  
            break

        # if client types a simple msg then send it over
        else:   
            client_socket.send(my_reply.encode())

    except (KeyboardInterrupt, EOFError):
        print("Error!!\n")
        break


client_socket.close()