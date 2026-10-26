This is a chatting program based on the client server paradigm. 
It establishes connections using TCP sockets.
It can support more than 4 simulatenous clients
some functionalities include Concurrent chatting, broadcast, privatemsgs


[![Architecture diagram](https://gitdiagram.com/diagram-badge.svg)](https://gitdiagram.com/areebasaeed17/tcp-based-python-chat-room?utm_source=readme&utm_medium=badge)

Chat user → Client app: enters chat — evidence: client.py
Client app → TCP socket: connects via — evidence: client.py
Connection listener → TCP socket: accepts via — evidence: server.py
Client app → Connection listener: sends nickname — evidence: server.py
Connection listener → Client registry: registers client — evidence: server.py
Connection listener → Client handler: starts thread — evidence: server.py
Client app → Client handler: sends messages — evidence: client.py
Client handler → Private messaging: routes private — evidence: server.py
Private messaging → Client registry: looks up recipient — evidence: server.py
Client handler → Online user list: handles request — evidence: server.py
