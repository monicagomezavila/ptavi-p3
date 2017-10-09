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
            diccionario['width'] = attrs.get('width', "")
            diccionario['heigth'] = attrs.get('height', "")
            diccionario['bgcolor'] = attrs.get('background-color', "")
            self.Letiquetas.append(diccionario)
        elif name == 'region':
            diccionario = {}
            diccionario['etiqueta'] = name
            diccionario['id'] = attrs.get('id', "")
            diccionario['top'] = attrs.get('top', "")
            diccionario['bottom'] = attrs.get('bottom', "")
            diccionario['left'] = attrs.get('left', "")
            diccionario['right'] = attrs.get('right', "")
            self.Letiquetas.append(diccionario)
        elif name == 'img':
            diccionario = {}
            diccionario['etiqueta'] = name
            diccionario['src'] = attrs.get('src', "")
            diccionario['begin'] = attrs.get('begin', "")
            diccionario['dur'] = attrs.get('dur', "")
            diccionario['region'] = attrs.get('region', "")
            self.Letiquetas.append(diccionario)
        elif name == 'audio':
            diccionario = {}
            diccionario['etiqueta'] = name
            diccionario['src'] = attrs.get('src', "")
            diccionario['begin'] = attrs.get('begin', "")
            diccionario['dur'] = attrs.get('dur', "")
            self.Letiquetas.append(diccionario)
        elif name == 'textstream':
            diccionario = {}
            diccionario['etiqueta'] = name
            diccionario['src'] = attrs.get('src', "")
            diccionario['region'] = attrs.get('begin', "")
            self.Letiquetas.append(diccionario)

    def get_tags(self):
        return self.Letiquetas

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
