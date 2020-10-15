from socket import * # sockets
import time

# definicao das variaveis
serverName = 'localhost' # ip do servidor a se conectar
serverPort = 55000 # porta a se conectar
clientSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP

message = input('Digite algo: ')
clientSocket.sendto(message.encode('utf8'),(serverName, serverPort)) # envia mensagem para o servidor
modifiedMessage, serverAddress = clientSocket.recvfrom(2048) # recebe do servidor a resposta
print (modifiedMessage.decode('utf8'))
clientSocket.close() # encerra o socket do cliente