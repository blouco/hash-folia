#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import re

from hashlib import md5

from flask import Flask, request, url_for, redirect
from flask import render_template, send_file, jsonify

try:
    from .blouco import Blouco
except:
    from HashFolia.blouco import Blouco

app = Flask(__name__)


def clean(seed):
    return re.sub('[^-A-Za-z0-9_,]', '', seed)

@app.route('/blouco/')
def blouco():
    return 'aguarde...'

@app.route('/porta_estandarte/')
def porta_estandarte():
    estandarte = clean(request.args.get('estandarte'))
    bonde = clean(request.args.get('bonde'))
    rua = clean(request.args.get('rua'))
    papo = clean(request.args.get('papo'))
    pag_titulo = 'Página da Porta-estandarte!'
    pag_descricao = rua
    pag_imagem = url_for('static', filename='avatares/porta_estandarte.png')
    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))

    return render_template('porta_estandarte.html', **locals())

@app.route('/puxadoras/')
def puxadoras():
    estandarte = clean(request.args.get('estandarte'))
    bonde = clean(request.args.get('bonde'))
    papo = clean(request.args.get('papo'))

    rua = clean(request.args.get('rua'))
    pag_titulo = 'Página das Puxadoras!'
    pag_descricao = rua
    pag_imagem = url_for('static', filename='avatares/puxadoras.png')
    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))

    return render_template('puxadoras.html', **locals())

@app.route('/mixers/')
def mixers():
    estandarte = clean(request.args.get('estandarte'))
    bonde = clean(request.args.get('bonde'))
    papo = clean(request.args.get('papo'))
    trio = clean(request.args.get('trio'))
    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))

    rua = clean(request.args.get('rua'))
    pag_titulo = 'Página das Mixers!'
    pag_descricao = rua
    pag_imagem = url_for('static', filename='avatares/mixers.png')

    return render_template('mixers.html', **locals())

@app.route('/artistas/')
def artistas():
    estandarte = clean(request.args.get('estandarte'))
    bonde = clean(request.args.get('bonde'))
    papo = clean(request.args.get('papo'))
    trio = clean(request.args.get('trio'))
    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))

    rua = clean(request.args.get('rua'))
    pag_titulo = 'Página das Artistas!'
    pag_descricao = rua
    pag_imagem = url_for('static', filename='avatares/artistas.png')

    return render_template('artistas.html', **locals())

@app.route('/passistas/')
def passistas():
    estandarte = clean(request.args.get('estandarte'))
    bonde = clean(request.args.get('bonde'))
    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))

    rua = clean(request.args.get('rua'))
    pag_titulo = 'Página das Passistas!'
    pag_descricao = rua
    pag_imagem = url_for('static', filename='avatares/passistas.png')

    return render_template('passistas.html', **locals())

@app.route('/cordoes/')
def cordoes():
    papo = clean(request.args.get('papo'))
    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))
    bonde = clean(request.args.get('bonde'))
    estandarte = clean(request.args.get('estandarte'))

    rua = clean(request.args.get('rua'))
    pag_titulo = 'Página das Cordões!'
    pag_descricao = rua
    pag_imagem = url_for('static', filename='avatares/cordoes.png')

    return render_template('cordoes.html', **locals())

@app.route('/incautas/')
def incautas():
    papo = clean(request.args.get('papo'))
    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))
    if request.args.get('doubletwitch'):
        doubletwitch = clean(request.args.get('doubletwitch')).split(',')

    rua = clean(request.args.get('rua'))
    pag_titulo = 'Página das Incautas!'
    pag_descricao = rua
    pag_imagem = url_for('static', filename='avatares/incautas.png')

    return render_template('incautas.html', **locals())

@app.route('/')
def index():
    seed = 'Anunciação e Rechamada'
    pag_titulo = 'Segue o Blouco!'
    pag_descricao = 'Abram alas ou misturem-se no Bonde, que o Blouco vai passar! 💣'
    pag_imagem = url_for('hash_imagem', seed=seed)
    return render_template('home.html', **locals())

@app.route('/hash/')
def hashfolia_index():
    seed = 'HashFolia'
    pag_titulo = 'HashFolia!'
    pag_descricao = 'O HashFolia transforma um texto-semente em um Estandarte, sendo usado para o início para um Blouco e também para sua movimentação.'
    pag_imagem = url_for('static', filename='hashfolia_estandarte.png')
    if "semente" in request.args:
        semente = clean(request.args["semente"])
        return redirect("https://ruas.bloucos.art/hash/" + semente, code=302)

    return render_template('hashfolia-index.html', **locals())
@app.route('/')


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
    pag_titulo = 'HashFolia!'
    pag_descricao = seed
    pag_imagem = url_for('hash_imagem', seed=seed)
    blouco_ = Blouco(seed)
    frases = [''.join(p[0]) for p in blouco_.hashfolia.frases]
    taro = blouco_.hashfolia.taro
    return render_template('hashfolia.html', blouco=blouco_, reseed=md5(seed.encode('utf-8')).hexdigest(), **locals())

@app.route('/hash/<seed>.json')
def hash_json(seed):
    pag_titulo = 'HashFolia!'
    pag_descricao = seed
    pag_imagem = request.url_root[:-1] + url_for('hash_imagem', seed=seed)
    seed = clean(seed)
    blouco_ = Blouco(seed)
    frases = [''.join(p[0]) for p in blouco_.hashfolia.frases]
    taro = [request.url_root + i['img'] for i in blouco_.hashfolia.taro]
    return jsonify({
        'titulo': pag_descricao,
        'imagem': pag_imagem,
        'taro': taro,
        'frases': frases,
        'pags': {k: (request.url_root + path) for k, path in {
            'incautas': blouco_.incautas,
            'cordoes': blouco_.cordoes,
            'passistas': blouco_.passistas,
            'artistas': blouco_.artistas,
            'mixers': blouco_.mixers,
            'puxadoras': blouco_.puxadoras,
            'porta_estandarte': blouco_.porta_estandarte,
        }.items()}
    })

if __name__ == "__main__":
    app.run()
