# Module interface réseau
import socket

# Addresse et le port
host = "ftp.ibiblio.org"
port = 21

# Par défaut socket réseau TCP

# Attribution de l'objet socket() à la variable s
s = socket.socket()

# Connexion
s.connect((host, port))

# Réception des données dans la variable data avec une taille de 128 bits
data = s.recv(128)

# Affichage des données
print(data.decode())

# Connexion en utilisateur anonymous
s.send(b"USER anonymous\r\n")
data = s.recv(128)
print(data.decode())

# Mot de passe toto@exemple.fr
s.send(b"PASS toto@exemple.fr\r\n")
data = s.recv(128)
print(data.decode())

# Envoi d'une commande
s.send(b"QUIT\r\n")

# Fermeture de la connexion
s.close