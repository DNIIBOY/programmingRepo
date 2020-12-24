import socket

HOST = "192.168.1.46"
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

print(f"Server hosted at {HOST}, PORT: {PORT}")
print("Looking for connection")

server.listen()

client, adress = server.accept()

print(f"Connected to {adress}")

while True:
    cmd_input = input("Enter command: ")
    try:
        client.send(cmd_input.encode("utf-8"))
        print(client.recv(1024).decode("utf-8"))
    except ConnectionResetError:
        print("Client has disconnected")
