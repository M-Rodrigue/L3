import socket

# Ecoute l'interface local de la machine
host = ""
port = 1337

s = socket.socket()

# Associe les paramètres
s.bind((host, port))
s.listen()

# Accepte la connexion du client et affiche l'addresse du client
s_client, adresse = s.accept()
print(adresse)

# Envoi un message au client
s_client.send(b"Bonjour client")

# Réception du message du client
data = s_client.recv(32)
print(data.decode())

# Fermeture de la connexion du client et du serveur
s_client.close()
s.close()