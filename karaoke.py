#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import smallsmilhandler
import json
import urllib.request


class KaraokeLocal():

    def __init__(self):
        parser = make_parser()
        cHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(sys.argv[1]))
        self.Letiquetas = cHandler.get_tags()

    def __str__(self):
        listauxiliar = []
        z = ''
        for diccionario in self.Letiquetas:
            etiqueta = diccionario.get('etiqueta', [])


            for clave, valor in diccionario.items():
                if valor != "" and clave != etiqueta:
                    listauxiliar.append(clave)
                    listauxiliar.append(valor)

            leng = len(listauxiliar)
            n = 0
            var = etiqueta

            while n <= leng-1:
                var += ('{tabulador}{clave}="{valor}"'.format(clave=listauxiliar[n],
                        valor=listauxiliar[n+1], tabulador='\t'))
                n = n+2

            z += ('{variable}{salto}'.format(variable=var, salto='\n'))
            listauxiliar = []
        return(z)

    def do_json(self, fichjson = ''):
        if fichjson == '':
            fichjson = sys.argv[1][:sys.argv[1].find('.')]
            fichjson = fichjson + '.json'
        with open(fichjson, 'w') as outfile:
            json.dump(self.Letiquetas, outfile)

    def do_local(self):
        for diccionario in self.Letiquetas:
            for clave, valor in diccionario.items():
                if clave == 'src' and valor[:valor.find(':')] == 'http':
                        with urllib.request.urlopen(valor) as response:
                            nombre = valor[valor.rfind('/')+1:]
                            local_filename, headers = urllib.request.urlretrieve(valor, filename=nombre)

                            diccionario['src'] = nombre
if __name__ == "__main__":
    try:
        classkaraoke = KaraokeLocal()
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
    print(classkaraoke)
    classkaraoke.do_json()
    classkaraoke.do_local()
    classkaraoke.do_json('local.json')
    print(classkaraoke)
