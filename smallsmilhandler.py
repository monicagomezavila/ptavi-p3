#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):

        self.width = ""
        self.height = ""
        self.bgcolor = ""

        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""

        self.src = ""
        self.begin = ""
        self.dur = ""
        self.region = ""

        self.audiosrc = ""
        self.audiobegin = ""
        self.audiodur = ""

        self.txtsrc = ""
        self.txtregion = ""

        self.Letiquetas = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            diccionario = {}
            diccionario['etiqueta'] = name
            self.width = attrs.get('width', "")
            diccionario['width'] = self.width
            self.height = attrs.get('height', "")
            diccionario['heigth'] = self.height
            self.bgcolor = attrs.get('background-color', "")
            diccionario['bgcolor'] = self.bgcolor
            self.Letiquetas.append(diccionario)
        elif name == 'region':
            diccionario = {}
            diccionario['etiqueta'] = name
            self.id = attrs.get('id', "")
            diccionario['id'] = self.id
            self.top = attrs.get('top', "")
            diccionario['top'] = self.top
            self.bottom = attrs.get('bottom', "")
            diccionario['bottom'] = self.bottom
            self.left = attrs.get('left', "")
            diccionario['left'] = self.left
            self.right = attrs.get('right', "")
            diccionario['right'] = self.right
            self.Letiquetas.append(diccionario)
        elif name == 'img':
            diccionario = {}
            diccionario['etiqueta'] = name
            self.src = attrs.get('src', "")
            diccionario['src'] = self.src
            self.begin = attrs.get('begin', "")
            diccionario['begin'] = self.begin
            self.dur = attrs.get('dur', "")
            diccionario['dur'] = self.dur
            self.region = attrs.get('region', "")
            diccionario['region'] = self.region
            self.Letiquetas.append(diccionario)
        elif name == 'audio':
            diccionario = {}
            diccionario['etiqueta'] = name
            self.audiosrc = attrs.get('src', "")
            diccionario['src'] = self.audiosrc
            self.audiobegin = attrs.get('begin', "")
            diccionario['begin'] = self.audiobegin
            self.audiodur = attrs.get('dur', "")
            diccionario['dur'] = self.audiodur
            self.Letiquetas.append(diccionario)
        elif name == 'textstream':
            diccionario = {}
            diccionario['etiqueta'] = name
            self.txtsrc = attrs.get('src', "")
            diccionario['src'] = self.txtsrc
            self.txtregion = attrs.get('begin', "")
            diccionario['region'] = self.txtregion
            self.Letiquetas.append(diccionario)

    def get_tags(self):
        return self.Letiquetas

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
