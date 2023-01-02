import socket
import sys

def start_client():
    #create TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #validate and read in command line arguments
    if len(sys.argv) != 4:
        print("Please run client.py in the format: python client.py [username] [hostname] [port]")
        exit()
    username = sys.argv[1]
    ip = str(sys.argv[2])
    port = int(sys.argv[3])

    #connect to the specified ip via port
    sock.connect((ip, port))
    sock.send(username.encode())
    print(sock.recv(2048).decode("utf-8"))
    while True:
        message = input("Type message to send here: ")
        sock.send(message.encode())


if __name__ == "__main__":
    start_client()
