#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import base64
from io import BytesIO
import sys
import os

from flask import Flask
from flask import render_template, send_file

import vizhash
from robohash import Robohash

from .logogram import logogram

app = Flask(__name__)


def hashfolia(seed):
    vh = vizhash.Vizhash(seed, 32, 16)
    vizhash_img = vh.identicon()

    logogram_img = logogram(seed, (1024,1024), 10, 10, 500, (1,1))
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


    robohash = Robohash(seed)
    robohash.assemble(sizex=512,sizey=512)

    vizhash_img.paste(robohash.img, (0, 0), robohash.img)
    return vizhash_img


@app.route('/')
def index():
    return 'Uso: /TEXTO-DA-SEMENTE. Exemplo: <a href="/volooptaz">/volooptaz</a>'

@app.route('/<seed>.png')
def get_image(seed):
    img = hashfolia(seed)
    filename = '/tmp/hashfolia-' + seed + '.png'
    img.save(filename)
    #buffered = BytesIO()
    #img.save(buffered, format="PNG")
    #img_str = base64.b64encode(buffered.getvalue())
    return send_file(filename, mimetype='image/png')

@app.route('/<seed>')
def get_hashfolia(seed):
    return render_template('hashfolia.html', seed=seed)

if __name__ == "__main__":
    app.run()
