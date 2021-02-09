#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import re

from hashlib import md5

from flask import Flask, request, url_for
from flask import render_template, send_file

try:
    from .blouco import Blouco
except:
    from HashFolia.blouco import Blouco

app = Flask(__name__)


def clean(seed):
    return re.sub('[^A-Za-z0-9_]', '', seed)

@app.route('/blouco/')
def blouco():
    return 'aguarde...'

@app.route('/porta_estandarte/')
def porta_estandarte():
    estandarte = request.args.get('estandarte')
    bonde = request.args.get('bonde')

    seed = '{estandarte}{bonde}'.format(**locals())
    pag_titulo = 'Página da Porta-estandarte!'
    pag_descricao = seed
    pag_imagem = url_for('hash_imagem', seed=seed)

    return render_template('porta_estandarte.html', **locals())

@app.route('/puxadoras/')
def puxadoras():
    return 'aguarde...'

@app.route('/mixers/')
def mixers():
    return 'aguarde...'

@app.route('/artistas/')
def artistas():
    return 'aguarde...'

@app.route('/passistas/')
def passistas():
    return 'aguarde...'

@app.route('/cordoes/')
def cordoes():
    papo = request.args.get('papo')
    bonde = request.args.get('bonde')

    seed = '{papo}{bonde}'.format(**locals())
    pag_titulo = 'Página das Cordões!'
    pag_descricao = seed
    pag_imagem = url_for('hash_imagem', seed=seed)

    return render_template('cordoes.html', **locals())

@app.route('/incautas/')
def incautas():
    papo = request.args.get('papo')
    transmissao = request.args.get('transmissao')

    seed = '{transmissao}{papo}'.format(**locals())
    pag_titulo = 'Página das Incautas!'
    pag_descricao = seed
    pag_imagem = url_for('hash_imagem', seed=seed)

    return render_template('incautas.html', **locals())

@app.route('/')
def index():
    return 'Uso: /hash/TEXTO-DA-SEMENTE. Exemplo: <a href="/hash/volooptaz">/volooptaz</a>'

@app.route('/hash/<seed>.png')
def hash_imagem(seed):
    seed = clean(seed)
    blouco_ = Blouco(seed)
    img = blouco_.hashfolia.avatar
    filename = '/tmp/hashfolia-' + seed + '.png'
    img.save(filename)
    return send_file(filename, mimetype='image/png')

@app.route('/hash/<seed>')
def hash_completo(seed):
    seed = clean(seed)
    blouco_ = Blouco(seed)
    frases = [''.join(p[0]) for p in blouco_.hashfolia.frases]
    taro = blouco_.hashfolia.taro
    return render_template('hashfolia.html', seed=seed, frases=frases, taro=taro, blouco=blouco_, reseed=md5(seed.encode('utf-8')).hexdigest())

if __name__ == "__main__":
    app.run()
