############################# CORRECTION ###############################
import socket
import time

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    start_time = time.perf_counter()
    client_socket.send("ping".encode())
    response = client_socket.recv(1024).decode()
    end_time = time.perf_counter()

    print(f"Réponse du serveur: {response}")
    print(f"Temps de réponse: {end_time - start_time} secondes")

    client_socket.close()

if __name__ == "__main__":
    client_program()