#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import re

from flask import Flask, request
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
    return 'aguarde...'

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
    return 'aguarde...'

@app.route('/incautas/')
def incautas():
    request.args.get('papo')
    papo = request.args.get('papo')
    transmissao = request.args.get('transmissao')
    return render_template('incautas.html', papo=papo, transmissao=transmissao)

@app.route('/')
def index():
    return 'Uso: /hash/TEXTO-DA-SEMENTE. Exemplo: <a href="/hash/volooptaz">/volooptaz</a>'

@app.route('/hash/<seed>.png')
def get_image(seed):
    seed = clean(seed)
    blouco_ = Blouco(seed)
    img = blouco_.hashfolia.avatar
    filename = '/tmp/hashfolia-' + seed + '.png'
    img.save(filename)
    return send_file(filename, mimetype='image/png')

@app.route('/hash/<seed>')
def get_hashfolia_img(seed):
    seed = clean(seed)
    blouco_ = Blouco(seed)
    frases = [''.join(p[0]) for p in blouco_.hashfolia.frases]
    taro = blouco_.hashfolia.taro
    return render_template('hashfolia.html', seed=seed, frases=frases, taro=taro, blouco=blouco_)

if __name__ == "__main__":
    app.run()
