############################# CORRECTION ###############################
import socket
import time
import threading


def server_program():
    host = socket.gethostname()
    port = 5005

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    print("Serveur prêt à recevoir des connexions...")


    client_socket, address = server_socket.accept()
    print(f"Connexion de {str(address)}")
    request = client_socket.recv(1024)
    time.sleep(5)  # Ralentissement artificiel du serveur
    if request.decode() == "ping":
        client_socket.send("pong".encode())
    client_socket.close()


if __name__ == "__main__":
    server_program()