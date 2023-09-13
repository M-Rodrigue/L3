# Exercice 1 - Client-serveur jeu trouve
# Ecrire un jeu qui permet à un client de deviner un nombre aléatoire choisi par le serveur. Le client indique le nombre maximum au serveur. Le serveur demande un nombre au client et répond ‘plus’ ou ‘moins’. La connexion est terminée lorsque le nombre est trouvé.
import socket

def connexion():
  host = "127.0.0.1"
  port = 1217
  s = socket.socket()
  s.connect((host, port))
  data = s.recv(128) #1
  print(data.decode())
  return s

def client(s):
  while True:
    nombre = input("Donnez un nombre (ou '0' pour quitter) : ")
    if nombre == 0:
      break
    s.send(nombre.encode()) #2
    data = s.recv(128).decode() #3
    print(data)

def main():
  s = connexion()
  client(s)
  s.close()

main()