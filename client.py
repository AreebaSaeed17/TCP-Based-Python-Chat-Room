import socket
import threading
import sys

# create the client socket in the same format as the server socket
# AF_INET specifies the address family as IPv4 
# sock_stream establishes a tcp connection
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    
  
client_ip = socket.gethostbyname(socket.gethostname())            # get host ip for future use
port_Server = 8080                                                  # connect to server on this port


# connect to the server
print("Your IP Address is " + str(client_ip))
print("Enter your name below so that server can know your name while communicating.\n")
client_name = input("Enter your name: ")
server_ip = input("Enter the IP of the server you want to connect to: ")
server_name = input("What is the name of the host you are trying to talk to? ")


# print a msg for better User Interface
print("\nAttempting to connect to " + str(server_ip) +" from " + str(client_ip) +".....\n")


# connect the client socket to the server
# connect() takes only one arg so wrap the server_name and port as one
try:
    client_socket.connect((server_ip, port_Server))
    print("Successfully connected to the server!\n")
except:
    print("Failed to connect to the server. Please check the IP and try again.")
    exit()

# server is waiting for nickname, send it
client_socket.send(client_name.encode())

def Receive_Message():
    while True:
        try:
            message_fromServer = (client_socket.recv(1024)).decode()        # receive the msg from server

            # if no communication possible break out
            if not message_fromServer:
                print("Server closed the connection.")
                break

            # print whatever msg has been recieved from server
            print("Message from Server: " + message_fromServer + "\n") 

    # now send a reply back
    my_reply = input("Enter your response: ")

    if my_reply.lower() == 'exit':  
        print("Ending the chat...")                  # if client wants to end
        break

    client_socket.send(my_reply.encode())           # if user doesnt want to end convo keep sending 

# Instantly display whatever lands, whether it's a broadcast or private message
            print("\n" + message_from_server)
            # Reprint the input prompt marker so the UI stays clean while typing
            print("Enter your response: ", end="", flush=True)
            
        except:
            # If the socket gets closed by our main thread, exit cleanly
            break

client_socket.close()
