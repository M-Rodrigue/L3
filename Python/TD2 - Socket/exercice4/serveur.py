############################# CORRECTION ###############################
import socket

def server_program():
    host = socket.gethostname()
    port = 1337

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    print("Serveur prêt à recevoir des connexions...")

    client_socket, address = server_socket.accept()
    print(f"Connexion de {str(address)}")

    client_socket.send("Bienvenue, veuillez entrer votre login : ".encode())
    login = client_socket.recv(1024).decode()

    if login == "admin":
        client_socket.send("Veuillez entrer votre mot de passe : ".encode())
        while True:
            password = client_socket.recv(1024).decode()
            if password == "abcd":
                client_socket.send("Connexion réussie !".encode())
                break
            else:
                client_socket.send("Mot de passe incorrect, veuillez réessayer : ".encode())
    else:
        client_socket.send("Login incorrect.".encode())

    client_socket.close()

if __name__ == "__main__":
    server_program()