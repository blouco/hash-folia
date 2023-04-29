#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import random

import vizhash

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

HEXAGRAMAS = '䷀䷁䷂䷃䷄䷅䷆䷇䷈䷉䷊䷋䷌䷍䷎䷏䷐䷑䷒䷓䷔䷕䷖䷗䷘䷙䷚䷛䷜䷝䷞䷟䷠䷡䷢䷣䷤䷥䷦䷧䷨䷩䷪䷫䷬䷭䷮䷯䷰䷱䷲䷳䷴䷵䷶䷷䷸䷹䷺䷻䷼䷽䷾䷿'

TRIGRAMAS = "☰☱☲☳☴☵☶☷"

app = Flask(__name__)

BUILD_DIR = os.path.join(app.root_path, '_build/')
WORDLIST = os.path.join(app.root_path, 'palavras.txt')

class HashFolia():
    def __init__(self, consulta):
        self.seed = consulta
        self.avatar = self._get_avatar()
        self.taro = self._get_taro()
        self.gramas = self._get_gramas()
        self.frases = self._get_frases()

    def _get_avatar(self):
        filename = os.path.join(BUILD_DIR, self.seed + '.png')

        if os.path.isfile(filename):
            avatar = Image.open(filename)
        else:
            vh = vizhash.Vizhash(self.seed, 32, 16)
            vizhash_img = vh.identicon()

            logogram_img = logogram(self.seed, (1500,1500), 10, 10, 500, (1,1))
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

            #resized_logogram = transp_logogram.resize((512, 512))
            resized_logogram = transp_logogram

            vizhash_img.paste(resized_logogram, (0, 0), transp_logogram)


            avatar = vizhash_img
            avatar.save(filename)
        return avatar

    def _get_taro(self):
        random.seed(self.seed)
        arcano_maior = random.choice(deck['major'])
        arcano_menor = random.choice(deck['minor'])
        return [arcano_maior, arcano_menor]


    def _get_gramas(self):
        random.seed(self.seed)
        return [random.choice(TRIGRAMAS), random.choice(HEXAGRAMAS)]

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

            return [''.join(p[0]) for p in frases]

class Divindade():
    def __init__(self):
        pass

class Blouco(Divindade):
    def __init__(self, rua=None, papo=None, trio=None, bonde=None, estandarte=None):
        self.rua = Rua(self, rua)
        self.papo = Papo(self, papo)
        self.trio = Trio(self, trio)
        self.bonde = Bonde(self, bonde)
        self.estandarte = Estandarte(self, estandarte)
        self.hashfolia = None

    @classmethod
    def hash_folia(cls, consulta):
        hashfolia = HashFolia(consulta)
        frases = hashfolia.frases
        blouco = cls()
        blouco.hashfolia = hashfolia
        blouco.estandarte = Estandarte(blouco, frases[0])
        blouco.bonde = Bonde(blouco, frases[1])
        blouco.trio = Trio(blouco, frases[2])
        blouco.papo = Papo(blouco, frases[3])
        blouco.rua = Rua(blouco, frases[4])

        print(blouco)
        return blouco

    @property
    def porta_estandarte(self):
        return 'porta_estandarte/?rua={rua.codigo}&estandarte={estandarte.codigo}&bonde={bonde.codigo}'.format(**vars(self))

    @property
    def puxadoras(self):
        return 'puxadoras/?rua={rua.codigo}&estandarte={estandarte.codigo}&bonde={bonde.codigo}&trio={trio.codigo}&papo={papo.codigo}'.format(**vars(self))

    @property
    def artistas(self):
        return 'artistas/?rua={rua.codigo}&estandarte={estandarte.codigo}&bonde={bonde.codigo}&trio={trio.codigo}&papo={papo.codigo}'.format(**vars(self))

    @property
    def mixers(self):
        return 'mixers/?rua={rua.codigo}&estandarte={estandarte.codigo}&bonde={bonde.codigo}&trio={trio.codigo}&papo={papo.codigo}'.format(**vars(self))

    @property
    def passistas(self):
        return 'passistas/?rua={rua.codigo}&estandarte={estandarte.codigo}&bonde={bonde.codigo}&papo={papo.codigo}'.format(**vars(self))

    @property
    def cordoes(self):
        return 'cordoes/?rua={rua.codigo}&estandarte={estandarte.codigo}&bonde={bonde.codigo}&papo={papo.codigo}'.format(**vars(self))

    @property
    def passantes(self):
        return 'passantes/?rua={rua.codigo}&papo={papo.codigo}'.format(**vars(self))

class Elemento():
    def __init__(self, blouco, frases):
        self.blouco = blouco
        self.frases = frases
        self.codigo = frases

    def __str__(self):
        return self.frases

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
