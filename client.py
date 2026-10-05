import socket

client_socket = socket.socket()               # create the client socket
client_ip = socket.gethostbyname()            # get host ip for future use
port_Server = 8080                            # connect to server on this port


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
client_socket.connect((server_name, port_Server))
print("Successfully connected to the server!\n")

# in the server configuration, it is waiting for the first msg from the client
client_socket.send(client_name.encode())

# receive the msg from server
while True:
    message_fromServer = (client_socket.recv(1024)).decode()

    # if no communication possible break out
    if not message_fromServer:
        print("Server closed the connection.")
        break

    print("Message from Server: " + message_fromServer + "\n") 

    # now send a reply back
    my_reply = input("Enter your response: ")

    if my_reply.lower() == 'exit':  
        print("Ending the chat...")                  # if client wants to end
        break

    client_socket.send(my_reply.encode())           # if user doesnt want to end convo keep sending 


client_socket.close()
