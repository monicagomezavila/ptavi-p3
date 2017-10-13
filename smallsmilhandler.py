#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.Letiquetas = []
        self.Dlistatributos = {'root-layout': ['width', 'height', 'background-color'],
                               'region': ['id', 'top', 'bottom', 'left', 'right'],
                               'img': ['src', 'begin', 'dur', 'region'],
                               'audio': ['src', 'begin', 'dur'],
                               'textstream': ['src', 'region']}

    def startElement(self, name, attrs):

        if name in self.Dlistatributos:
            diccionario = {}
            diccionario['etiqueta'] = name
            for atributo in self.Dlistatributos[name]:
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
