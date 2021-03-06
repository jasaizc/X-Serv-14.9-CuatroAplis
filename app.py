#!/usr/bin/python

import socket
import webapp
import aleat
import suma
import hola

class app:

    def parse(self, request, rest):

        return None

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>" + \
                    "Opciones disponibles: " + \
                    "</h1><p> <a href='/hola'>/hola</a></p><p><a href='/adios'>/adios</a></p><p>/suma/operando1/operando2</p><p><a href='/aleat'>/aleat</a></p></body></html>")



class appWeb(webapp.webApp):

    def parse(self, request, rest):

        return None

    def process(self, parsedRequest):
        return ("200 OK", "<html><body><h1>" + \
                    "Opciones disponibles: " + \
                    "</h1><p> <a href='/hola'>/hola</a></p><p><a href='/adios'>/adios</a></p><p>/suma/operando1/operando2</p><p><a href='/aleat'>/aleat</a></p></body></html>")

    def __init__ (self, hostname, port, apps):
        """Initialize the web application."""

        self.apps = apps
        self.myApp = app()
        # Create a TCP objet socket and bind it to a port
        mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        mySocket.bind((hostname, port))

        # Queue a maximum of 5 TCP connection requests
        mySocket.listen(5)

        # Accept connections, read incoming data, and call
        # parse and process methods (in a loop)

        while True:
            print 'Waiting for connections'
            (recvSocket, address) = mySocket.accept()
            print 'HTTP request received (going to parse and process):'
            request = recvSocket.recv(2048)
            print request
            (theApp, rest) = self.select (request)
            parsedRequest = theApp.parse (request, rest)
            (returnCode, htmlAnswer) = theApp.process (parsedRequest)
            print 'Answering back...'
            recvSocket.send("HTTP/1.1 " + returnCode + " \r\n\r\n"
                         + htmlAnswer + "\r\n")
            recvSocket.close()
        

if __name__ == "__main__":
    holaWeb = hola.holaApp()
    adiosWeb = hola.holaApp()
    sumaWeb = suma.sumaApp()
    aleatWeb = aleat.aleatApp()
    dic = {'/hola': holaWeb,'/adios': adiosWeb,'/suma': sumaWeb,'/aleat':aleatWeb}
    testWebApp =  appWeb("localhost", 1234, dic)
