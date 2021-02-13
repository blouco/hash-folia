#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import re

from hashlib import md5

from flask import Flask, request, url_for, redirect
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
    pag_imagem = url_for('static', filename='avatares/porta_estandarte.png')

    return render_template('porta_estandarte.html', **locals())

@app.route('/puxadoras/')
def puxadoras():
    estandarte = request.args.get('estandarte')
    bonde = request.args.get('bonde')
    papo = request.args.get('papo')

    seed = '{estandarte}{bonde}{papo}'.format(**locals())
    pag_titulo = 'Página das Puxadoras!'
    pag_descricao = seed
    pag_imagem = url_for('static', filename='avatares/puxadoras.png')

    return render_template('puxadoras.html', **locals())

@app.route('/mixers/')
def mixers():
    estandarte = request.args.get('estandarte')
    bonde = request.args.get('bonde')
    papo = request.args.get('papo')
    trio = request.args.get('trio')

    seed = '{papo}{trio}{bonde}{estandarte}'.format(**locals())
    pag_titulo = 'Página das Mixers!'
    pag_descricao = seed
    pag_imagem = url_for('static', filename='avatares/mixers.png')

    return render_template('mixers.html', **locals())

@app.route('/artistas/')
def artistas():
    estandarte = request.args.get('estandarte')
    bonde = request.args.get('bonde')
    papo = request.args.get('papo')
    trio = request.args.get('trio')

    seed = '{estandarte}{bonde}{trio}'.format(**locals())
    pag_titulo = 'Página das Artistas!'
    pag_descricao = seed
    pag_imagem = url_for('static', filename='avatares/artistas.png')

    return render_template('artistas.html', **locals())

@app.route('/passistas/')
def passistas():
    estandarte = request.args.get('estandarte')
    bonde = request.args.get('bonde')

    seed = '{estandarte}{bonde}'.format(**locals())
    pag_titulo = 'Página das Passistas!'
    pag_descricao = seed
    pag_imagem = url_for('static', filename='avatares/passistas.png')

    return render_template('passistas.html', **locals())

@app.route('/cordoes/')
def cordoes():
    papo = request.args.get('papo')
    bonde = request.args.get('bonde')

    seed = '{bonde}{papo}'.format(**locals())
    pag_titulo = 'Página das Cordões!'
    pag_descricao = seed
    pag_imagem = url_for('static', filename='avatares/cordoes.png')

    return render_template('cordoes.html', **locals())

@app.route('/incautas/')
def incautas():
    papo = request.args.get('papo')
    transmissao = request.args.get('transmissao')

    seed = '{transmissao}{papo}'.format(**locals())
    pag_titulo = 'Página das Incautas!'
    pag_descricao = seed
    pag_imagem = url_for('static', filename='avatares/incautas.png')

    return render_template('incautas.html', **locals())

@app.route('/')
def index():
    seed = 'Segue o Blouco!!!'
    pag_titulo = 'Blouco'
    pag_descricao = 'Abram alas ou misturem-se no Bonde, que o Blouco vai passar! 💣 Dom, 14 de fev, pelas ruas da Web'
    pag_imagem = url_for('static', filename='pix/qr_logoblouco.png')
    return render_template('home.html', **locals())

@app.route('/hash/')
def hashfolia_index():
    seed = 'HashFolia'
    pag_titulo = 'HashFolia!'
    pag_descricao = 'Início'
    pag_imagem = url_for('hash_imagem', seed=seed)
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
    pag_titulo = 'HashFolia!'
    pag_descricao = seed
    pag_imagem = url_for('hash_imagem', seed=seed)
    seed = clean(seed)
    blouco_ = Blouco(seed)
    frases = [''.join(p[0]) for p in blouco_.hashfolia.frases]
    taro = blouco_.hashfolia.taro
    return render_template('hashfolia.html', blouco=blouco_, reseed=md5(seed.encode('utf-8')).hexdigest(), **locals())

if __name__ == "__main__":
    app.run()
