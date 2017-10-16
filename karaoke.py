#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import json
import urllib.request


class Karaoke(smallsmilhandler.SmallSMILHandler):

    def get_tags(self):
        listauxiliar = []

        for diccionario in self.Letiquetas:
            etiqueta = diccionario.get('etiqueta', [])
            diccionario.pop('etiqueta', etiqueta)

            for clave, valor in diccionario.items():
                if valor != "":
                    listauxiliar.append(clave)
                    listauxiliar.append(valor)

            leng = len(listauxiliar)
            n = 0
            var = etiqueta

            while n <= leng-1:
                var += ('{tabulador}{clave}="{valor}"'.format(clave=listauxiliar[n],
                        valor=listauxiliar[n+1], tabulador='\t'))
                n = n+2
            print(var)
            listauxiliar = []

    def fichjson(self):
        with open('karaoke.json', 'w') as outfile:
            json.dump(self.Letiquetas, outfile)

    def urls(self):
        for diccionario in self.Letiquetas:
            for clave, valor in diccionario.items():
                if clave == 'src' and valor[:valor.find(':')] == 'http':
                        with urllib.request.urlopen(valor) as response:
                            nombre = valor[valor.rfind('/')+1:]
                            local_filename, headers = urllib.request.urlretrieve(valor, filename=nombre)

if __name__ == "__main__":
    try:
        nombresmil = str(sys.argv[1])
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")

    parser = make_parser()
    cHandler = Karaoke()
    parser.setContentHandler(cHandler)
    try:
        parser.parse(open(nombresmil))
    except FileNotFoundError:
        sys.exit("File not found // Usage: python3 karaoke.py file.smil")
    print(cHandler.get_tags())
    cHandler.fichjson()
    cHandler.urls()
