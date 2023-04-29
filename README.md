# hash-folia

hash-folia - Transforma texto em uma composição de *visual hashes*

![Imagem de exemplo para input "blouco"](https://github.com/blouco/hash-folia/raw/main/exemplo-blouco.png)

Este projeto está sendo desenvolvido para gerar os Estandartes do
[OpenBlouco](https:;//openblouco.readthedocs.io). Muito em construção!!!

## Texto -> Hash -> Estandarte

Um texto-base é passado por uma composição de *[visual
hashes](https://github.com/drhus/awesome-identicons)*.

Os hashes utilizados são os seguintes:

- [Robohash](https://robohash.org/) - módulo `vobohash` em `requirements.txt`
- [Vizhash](https://github.com/sebsauvage/VizHash) - módulo `vizhash`
  em `requirements.txt`
- [arrival\_logograms](https://github.com/FlxB2/arrival_logograms) - Adaptação do script original desenvolvido pela Wolfram Mathematica para gerar *logogramas* para o filme Arrival.


## Executando localmente

Clonando:

```bash
$ git clone https://github.com/blouco/hash-folia
$ cd hash-folia/
```

```bash
$ pip3 install -r requirements.txt
```

Executando o ambiente de desenvolvimento:

```bash
$ export FLASK_APP=__init__.py
$ flask run
```

O arquivo `hashfolia.wsgi` é uma base para executar o aplicativo Flask em um
[servidor de produção](https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps).

## Licença

A licença usada para o código, incluindo a adaptação do `arrival_logograms`, é a MIT License, descrita em `LICENSE`.
