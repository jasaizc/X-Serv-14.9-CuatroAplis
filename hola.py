#!/usr/bin/python

class holaApp:
    def parse(self, request, rest):
        peticion = request.split()[1][1:]
        return peticion

    def process(self,parsedRequest):
        peticiones = parsedRequest;
        if peticiones == "hola":           
            return ("200 OK","<html><body><b>Hola Mundo!</h1></body></html>")
        elif peticiones == "adios":
            return ("200 OK","<html><body><b>Adios Mundo!</h1></body></html>")    
