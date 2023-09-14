# Exercice 2 - Socket
# Nous voulons créer un client serveur qui jouent au chifoumi.
import socket
import random

def connexion():
  host = "127.0.0.1"
  port = 2001
  s_client = socket.socket()
  s_client.connect((host, port))
  data = s_client.recv(128) #1-R
  print(data.decode())
  return s_client

def chifoumi(s_client):
  l = ["pierre", "feuille", "ciseaux"]

  for i in range(5):
    choix_client = random.choice(l)
    s_client.send(choix_client.encode()) #2-Q
    data = s_client.recv(128) #3-R
    print(data.decode())

def main():
  s_client = connexion()
  chifoumi(s_client)
  s_client.close()

main()