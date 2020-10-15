
from socket import * # sockets
import time

# definicao das variaveis
serverPort = 55000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind(('', serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = time.ctime()
    message = message.decode('utf8')
    if message == 'data':    
        serverSocket.sendto(modifiedMessage.encode('utf8'), clientAddress)
    else:
        serverSocket.sendto('comando invalido'.encode('utf8'), clientAddress)