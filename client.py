import socket
import sys
import time

host_socket = socket.socket()               # create the client socket
host_ip = socket.gethostbyname()            # get the host ip

port_Server = 8080                          # connect to server on this port
server_ip = socket.gethostname()            # get the name of server

# connect to the server
server_ip = input("Enter the IP of the server you want to connect to: ")
server_name = input("What is the name of the host you are trying to talk to? ")

host_socket.connect((server_name, port_Server))

# receive the msg from server
