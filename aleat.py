#!/usr/bin/python

import random


class aleatApp:
  def parse(self, request, rest):
        return None
      
  def process(self, parsedRequest):
    aleatorio = str(random.randrange(100000000))
    return ("200 OK","<html>" +
                         "<body><h1>Pagina para pedir una nueva pagina aleatoria</h1>" +
                         "<p>Hola, <a href='" + aleatorio + "'>Dame otra</a></p>" +                        
                         "</body></html>" +
                         "\r\n")
