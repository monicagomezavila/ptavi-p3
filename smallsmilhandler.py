#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.Letiquetas = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            diccionario = {}
            diccionario['etiqueta'] = name
            atributos = ['width', 'heigth', 'bgcolor']
            for atributo in atributos:
                diccionario[atributo] = attrs.get(atributo, "")
            self.Letiquetas.append(diccionario)

        elif name == 'region':
            diccionario = {}
            diccionario['etiqueta'] = name
            atributos = ['id', 'top', 'bottom', 'left', 'right']
            for atributo in atributos:
                diccionario[atributo] = attrs.get(atributo, "")
            self.Letiquetas.append(diccionario)

        elif name == 'img':
            diccionario = {}
            diccionario['etiqueta'] = name
            atributos = ['src', 'begin', 'dur', 'region']
            for atributo in atributos:
                diccionario[atributo] = attrs.get(atributo, "")
            self.Letiquetas.append(diccionario)

        elif name == 'audio':
            diccionario = {}
            diccionario['etiqueta'] = name
            atributos = ['src', 'begin', 'dur']
            for atributo in atributos:
                diccionario[atributo] = attrs.get(atributo, "")
            self.Letiquetas.append(diccionario)

        elif name == 'textstream':
            diccionario = {}
            diccionario['etiqueta'] = name
            atributos = ['src', 'region']
            for atributo in atributos:
                diccionario[atributo] = attrs.get(atributo, "")
            self.Letiquetas.append(diccionario)

    def get_tags(self):
        return self.Letiquetas

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
