# hash-folia

hash-folia - Transforma texto em uma composição de *visual hashes*

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
servidor de produção.

## Licença

A licença usada para o código, incluindo a adaptação do `arrival_logograms`, é a MIT License, descrita em `LICENSE`.

## Trabalho futuro

uma “senha” de N (a definir) palavras escolhidas da lista Diceware -- ex: .
Seus componentes são utilizados para criar:
O nome do documento do próximo Estandarte
O nome da stream de transmissão da Banda
O nome do ambiente do Desfile
Uma arte composta de: “visual hashes” / “identicons” relacionados à frase
Um arcano maior e menor do tarô
Por enquanto usando o Marsella por ser domínio público mas parece que o RWS
também é :-)
