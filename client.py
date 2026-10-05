import socket
import sys
import time

host_socket = socket.socket()               # create the client socket
host_ip = socket.gethostbyname()            # get host ip for future use
port_Server = 8080                          # connect to server on this port


# connect to the server
print("Your IP Address is " + str(host_ip))
print("Enter your name below so that server can know your name while communicating.\n")
client_name = input("Enter your name: ")

server_ip = input("Enter the IP of the server you want to connect to: ")
server_name = input("What is the name of the host you are trying to talk to? ")

print("\nAttempting to connect to " + str(server_ip) +" from " + str(host_ip) )
host_socket.connect((server_name, port_Server))

# receive the msg from server
