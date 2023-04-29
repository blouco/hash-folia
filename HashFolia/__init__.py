#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import re

from urllib.parse import urljoin
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



@app.route('/puxadoras/')
def puxadoras():
    estandarte = clean(request.args.get('estandarte'))
    bonde = clean(request.args.get('bonde'))
    papo = clean(request.args.get('papo'))
    trio = clean(request.args.get('trio'))
    rua = clean(request.args.get('rua'))
    blouco = Blouco(rua, papo, trio, bonde, estandarte)

    pag_titulo = 'Blouco @ ' + rua + ' ~ Puxadora'
    pag_descricao = "& {estandarte} / {bonde} | {papo} @ {rua}".format(**locals())
    # pag_imagem = "https://avatars.dicebear.com/api/identicon/" + rua + ".svg?colors[]=green"

    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))

    avatar = url_for('static', filename='avatares/puxadoras.png')
    pag_imagem = avatar

    return render_template('divindades/puxadora.html', **locals())

@app.route('/mixers/')
def mixers():
    estandarte = clean(request.args.get('estandarte'))
    bonde = clean(request.args.get('bonde'))
    papo = clean(request.args.get('papo'))
    trio = clean(request.args.get('trio'))
    rua = clean(request.args.get('rua'))

    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))

    blouco = Blouco(rua, papo, trio, bonde, estandarte)

    pag_titulo = 'Blouco @ ' + rua + ' ~ Mixer'
    pag_descricao = "& {estandarte} / {bonde} < {trio} | {papo} @ {rua}".format(**locals())
    # pag_imagem = "https://avatars.dicebear.com/api/identicon/" + rua + ".svg?colors[]=green"
    avatar = url_for('static', filename='avatares/mixers.png')
    pag_imagem = avatar

    return render_template('divindades/mixer.html', **locals())

@app.route('/artistas/')
def artistas():
    estandarte = clean(request.args.get('estandarte'))
    bonde = clean(request.args.get('bonde'))
    papo = clean(request.args.get('papo'))
    trio = clean(request.args.get('trio'))
    rua = clean(request.args.get('rua'))

    blouco = Blouco(rua, papo, trio, bonde, estandarte)

    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))

    pag_titulo = 'Blouco @ ' + rua + ' ~ Artista'
    pag_descricao = "& {estandarte} / {bonde} < {trio} | {papo} @ {rua}".format(**locals())
    # pag_imagem = "https://avatars.dicebear.com/api/identicon/" + rua + ".svg?colors[]=green"
    avatar = url_for('static', filename='avatares/artistas.png')
    pag_imagem = avatar

    print("######")
    print(request.args)

    return render_template('divindades/artista.html', **locals())

@app.route('/passistas/')
def passistas():
    estandarte = clean(request.args.get('estandarte'))
    bonde = clean(request.args.get('bonde'))
    papo = clean(request.args.get('papo'))
    rua = clean(request.args.get('rua'))
    blouco = Blouco(rua, papo)

    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))

    pag_titulo = 'Blouco @ ' + rua + ' ~ Passista'
    pag_descricao = "& {estandarte} / {bonde} @ {rua}".format(**locals())
    # pag_imagem = "https://avatars.dicebear.com/api/identicon/" + rua + ".svg?colors[]=green"
    avatar = url_for('static', filename='avatares/passistas.png')
    pag_imagem = avatar

    return render_template('divindades/passista.html', **locals())

@app.route('/cordoes/')
def cordoes():
    estandarte = clean(request.args.get('estandarte'))
    bonde = clean(request.args.get('bonde'))
    papo = clean(request.args.get('papo'))
    rua = clean(request.args.get('rua'))
    blouco = Blouco(rua, papo)

    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))

    pag_titulo = 'Blouco @ ' + rua + ' ~ Cordão'
    pag_descricao = "& {estandarte} | {papo} @ {rua}".format(**locals())
    # pag_imagem = "https://avatars.dicebear.com/api/identicon/" + rua + ".svg?colors[]=green"
    avatar = url_for('static', filename='avatares/cordoes.png')
    pag_imagem = avatar

    return render_template('divindades/cordao.html', **locals())

@app.route('/passantes/')
def passantes():
    papo = clean(request.args.get('papo'))
    rua = clean(request.args.get('rua'))

    blouco = Blouco(rua, papo)

    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))
    if request.args.get('doubletwitch'):
        doubletwitch = clean(request.args.get('doubletwitch')).split(',')

    pag_titulo = 'Blouco @ ' + rua + ' ~ Passante'
    pag_descricao = "| {papo} @ {rua}".format(**locals())
    # pag_imagem = "https://avatars.dicebear.com/api/identicon/" + rua + ".svg?colors[]=green"
    avatar = url_for('static', filename='avatares/passantes.png')
    pag_imagem = avatar

    return render_template('divindades/passante.html', **locals())

@app.route('/')
def index():
    pag_titulo = 'Segue o Blouco!'
    pag_descricao = 'Uma trans-experiência pelas tecnologias carnavalescas exusíacas e oxalufânicas da informação'
    pag_imagem = url_for('static', filename='logo.png')
    return render_template('home.html', **locals())

@app.route('/2021')
def index_2021():
    seed = 'Anunciação e Rechamada'
    pag_titulo = 'Segue o Blouco!'
    pag_descricao = 'Abram alas ou misturem-se no Bonde, que o Blouco vai passar! 💣'
    pag_imagem = url_for('gerar_blouco_imagem', seed=seed)
    return render_template('home-2021.html', **locals())

@app.route('/blouco/')
def gerar_blouco_index():
    seed = 'blouco'
    pag_titulo = 'HashFolia'
    pag_descricao = 'O HashFolia transforma um texto-semente em um Estandarte, sendo usado para o início para um Blouco e também para sua movimentação.'
    pag_imagem = urljoin(request.url_root, url_for('gerar_blouco_imagem', seed=seed))
    if "semente" in request.args:
        semente = clean(request.args["semente"])
        if "youtube" in request.args:
            youtube = clean(request.args["youtube"])
        if "twitch" in request.args:
            twitch = clean(request.args["twitch"])
        return redirect("/blouco/" + semente, code=302)

    return render_template('hashfolia-index.html', **locals())

@app.route('/blouco/<seed>.png')
def gerar_blouco_imagem(seed):
    seed = clean(seed)
    blouco_ = Blouco.hash_folia(seed)
    img = blouco_.hashfolia.avatar
    filename = '/tmp/bloucofolia-' + seed + '.png'
    img.save(filename)
    return send_file(filename, mimetype='image/png')

@app.route('/blouco/<seed>')
def gerar_blouco(seed):
    seed = clean(seed)
    hash_md5 = md5(seed.encode('utf-8')).hexdigest()
    blouco_ = Blouco.hash_folia(seed)

    taro = blouco_.hashfolia.taro
    gramas = blouco_.hashfolia.gramas

    vars_streaming = []
    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
        vars_streaming += ['youtube=' + youtube]
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))
        vars_streaming += ['twitch=' + twitch]

    if vars_streaming:
        sufixo_url = '&' + '&'.join(vars_streaming)
    else:
        sufixo_url = ''

    pag_titulo = 'HashFolia'.format(**locals())
    pag_descricao = "& {estandarte} / {bonde} < {trio} | {papo} @ {rua}".format(**vars(blouco_))
    pag_imagem = url_for('gerar_blouco_imagem', seed=seed)


    return render_template('divindades/porta_estandarte.html', blouco=blouco_, **locals())

@app.route('/blouco/<seed>.json')
def gerar_blouco_json(seed):
    seed = clean(seed)
    hash_md5 = md5(seed.encode('utf-8')).hexdigest()
    Blouco_ = Blouco.hash_folia(seed)
    frases = [''.join(p[0]) for p in blouco_.hashfolia.frases]
    taro = blouco_.hashfolia.taro
    gramas = blouco_.hashfolia.gramas
    if request.args.get('youtube'):
        youtube = clean(request.args.get('youtube'))
    else:
        youtube = None
    if request.args.get('twitch'):
        twitch = clean(request.args.get('twitch'))
    else:
        twitch = None

    pag_titulo = 'HashFolia <<< "{seed}"'.format(**locals())
    pag_descricao = "& {frases[0]} / {frases[1]} < {frases[2]} | {frases[3]} @ {frases[4]}".format(**locals())
    pag_imagem = urljoin(request.url_root, url_for('gerar_blouco_imagem', seed=seed))

    result = {
        'semente': seed,
        'hashes': {
            'md5': hash_md5,
            'selo': pag_imagem,
        },
        'elementos': {
            'estandarte': frases[0],
            'bonde': frases[1],
            'trio': frases[2],
            'papo': frases[3],
            'rua': frases[4],
        },
        'sorte': {
            'maior': urljoin(request.url_root, taro[0]['img']),
            'menor': urljoin(request.url_root, taro[1]['img']),
            'trigrama': gramas[0],
            'hexagrama': gramas[1],
        },
        'transmissao': {
            'twitch': twitch,
            'youtube': twitch,
        },
        'titulo': pag_titulo,
        'descricao': pag_descricao,
        'divindades': {k: (request.url_root + path) for k, path in {
            'passantes': blouco_.passantes,
            'cordoes': blouco_.cordoes,
            'passistas': blouco_.passistas,
            'artistas': blouco_.artistas,
            'mixers': blouco_.mixers,
            'puxadoras': blouco_.puxadoras,
            'porta_estandarte': blouco_.porta_estandarte,
        }.items()},
    }

    return result

if __name__ == "__main__":
    app.run()
