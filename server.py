import socket
import sys
import threading

active_clients = {}
def start_server():
    #create a socket using TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #input validation
    #TODO : improve argument validation
    if len(sys.argv) != 2:
        print("Please provide a port number for to run the server on.")
        exit()
    port = int(sys.argv[1])

    #bind the server to localhost on the provided port
    server.bind(("", port))

    #Listen for up to 5 active connections
    server.listen(5)
    print("!")
    #dictionary to store connected clients
    while True:
        conn, addr = server.accept()
        print(addr)
        user = conn.recv(2048).decode("utf-8")
        print(user + " has joined")
        active_clients[addr[0]] = [conn, user]
        threading.Thread(target=new_client, args=(conn, user,)).start()



# when a user connects create a new thread to constantly check if the new client is sending anything to the server
#if a client does send something broadcast it to all active clients
def new_client(conn, user):
    conn.send("Welcome!".encode())
    while True:
        try:
            message = conn.recv(2048).decode()

            if message:
                print(user + ": " + message)
                #broadcast to all connected clients
            else:
                print("Empty msg")
                #disconnect
        except:
            continue
        


if __name__ == "__main__":
    start_server()


