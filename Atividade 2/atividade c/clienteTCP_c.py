from socket import *

serverName = 'localhost'
serverPort = 15000
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input('Digite um comando: ')
clientSocket.send(sentence.encode('utf-8'))
clientSocket.close()