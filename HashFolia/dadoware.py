#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from subprocess import Popen, PIPE 
import random
from io import BytesIO
import sys
import os

WORDLIST = 'pt-br'

def _frase():
    def comando_diceware(rodadas):
        comando = ['diceware', '-n', '1', '-r', 'realdice']
        if WORDLIST:
            comando.extend(['-w', WORDLIST])
        cli_input = rodadas.encode('utf-8')
        p = Popen(comando, stdout=PIPE, stdin=PIPE, stderr=PIPE)
        stdout_data = p.communicate(input=cli_input)[0][99:-1]
        return stdout_data.decode('utf-8')

    rs = [random.choice(range(1, 7)) for i in range(5)]

    rodadas_cli = ', '.join([str(n) for n in rs])
    palavra = comando_diceware(rodadas_cli)

    return palavra


def frases_dado(padroes):
    if type(padroes) in (tuple, list):
        return [frases_dado(p) for p in padroes]

    return [_frase() for i in range(padroes)]

