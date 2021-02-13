#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import random
import vizhash
from robohash import Robohash

import json
from PIL import Image

try:
    from .logogram import logogram
except:
    from logogram import logogram
try:
    from .deck import deck
except:
    from deck import deck

from flask import Flask

FRASES_PADROES = ((3, 3), (3, 3), (3, 3), (3, 3), (3, 3))

app = Flask(__name__)

BUILD_DIR = os.path.join(app.root_path, '_build/')
WORDLIST = os.path.join(app.root_path, 'palavras.txt')

class HashFolia():
    def __init__(self, consulta):
        self.seed = consulta
        self.avatar = self._get_avatar()
        self.taro = self._get_taro()
        self.frases = self._get_frases()

    def _get_avatar(self):
        filename = os.path.join(BUILD_DIR, self.seed + '.png')

        if os.path.isfile(filename):
            avatar = Image.open(filename)
        else:
            vh = vizhash.Vizhash(self.seed, 32, 16)
            vizhash_img = vh.identicon()

            logogram_img = logogram(self.seed, (1024,1024), 10, 10, 500, (1,1))
            transp_logogram = logogram_img.convert("RGBA")
            datas = transp_logogram.getdata()
            newData = []
            for item in datas:
                if item[0] == 255 and item[1] == 255 and item[2] == 255:
                    newData.append((255, 255, 255, 0))
                elif item[0] == 0 and item[1] == 0 and item[2] == 0:
                    newData.append((255, 0, 255, 127))
                else:
                    if item[0] > 150:
                        newData.append((0, 0, 0, 255))
                    else:
                        newData.append(item)
            transp_logogram.putdata(newData)

            vizhash_img.paste(transp_logogram, (0, 0), transp_logogram)


            robohash = Robohash(self.seed)
            robohash.assemble(sizex=512,sizey=512)

            vizhash_img.paste(robohash.img, (0, 0), robohash.img)

            avatar = vizhash_img
            avatar.save(filename)
        return avatar

    def _get_taro(self):
        random.seed(self.seed)
        arcano_maior = random.choice(deck['major'])
        arcano_menor = random.choice(deck['minor'])
        return (arcano_maior, arcano_menor)


    def _get_frases(self):

        def expandir_padroes(padroes, palavras):
            if type(padroes) in (tuple, list):
                return [expandir_padroes(p, palavras) for p in padroes]
            return [random.choice(palavras).capitalize() for i in range(padroes)]

        with open(WORDLIST) as wordlist_file:
            palavras = [w for w in wordlist_file.read().split('\n') if w]
            filename = os.path.join(BUILD_DIR, self.seed + '-frases.json')
            has_file = False
            if os.path.isfile(filename):
                with open(filename) as json_file:
                    frases = json.load(json_file)
            else:
                random.seed(self.seed)
                frases = expandir_padroes(FRASES_PADROES, palavras)
                with open(filename, 'w') as json_file:
                    json.dump(frases, json_file)

            return frases

class Divindade():
    def __init__(self):
        pass

class Blouco(Divindade):
    def __init__(self, consulta):
        self.hashfolia = HashFolia(consulta)
        frases = self.hashfolia.frases
        self.estandarte = Estandarte(self, frases[0])
        self.bonde = Bonde(self, frases[1])
        self.trio = Trio(self, frases[2])
        self.papo = Papo(self, frases[3])
        self.rua = Rua(self, frases[4])

    @property
    def porta_estandarte(self):
        return 'porta_estandarte/?seed={rua.codigo}&bonde={bonde.codigo}&estandarte={estandarte.codigo}'.format(**vars(self))

    @property
    def puxadoras(self):
        return 'puxadoras/?seed={rua.codigo}&bonde={bonde.codigo}&estandarte={estandarte.codigo}&papo={papo.codigo}'.format(**vars(self))

    @property
    def artistas(self):
        return 'artistas/?seed={rua.codigo}&bonde={bonde.codigo}&estandarte={estandarte.codigo}&trio={trio.codigo}'.format(**vars(self))

    @property
    def mixers(self):
        return 'mixers/?seed={rua.codigo}&bonde={bonde.codigo}&estandarte={estandarte.codigo}&papo={papo.codigo}&trio={trio.codigo}'.format(**vars(self))

    @property
    def passistas(self):
        return 'passistas/?seed={rua.codigo}&estandarte={estandarte.codigo}&bonde={bonde.codigo}'.format(**vars(self))

    @property
    def cordoes(self):
        return 'cordoes/?seed={rua.codigo}&bonde={bonde.codigo}&papo={papo.codigo}'.format(**vars(self))

    @property
    def incautas(self):
        return 'incautas/?seed={rua.codigo}&papo={papo.codigo}&twitch=&youtube='.format(**vars(self))

class Elemento():
    def __init__(self, blouco, frases):
        self.blouco = blouco
        self.frases = frases
        self.codigo = self.frases_str[0]
        self.senha = self.frases_str[1]

    @property
    def frases_str(self):
        return [''.join(f) for f in self.frases]

class Bonde(Elemento):
    pass


class Trio(Elemento):
    pass

class Papo(Elemento):
    pass


class Rua(Elemento):
    pass


class Estandarte(Elemento):
    pass

if __name__ == '__main__':
    b = Blouco('blouco')
    print(b.porta_estandarte)
    print(b.puxadoras)
    print(b.artistas)
    print(b.mixers)
    print(b.passistas)
    print(b.cordoes)
    print(b.incautas)
