#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
nsms_web_api.py v 0.1
NSMS, 2011, http://www.nsms.com.br
Author: Thiago Rondon <thiago@nsms.com.br>

HTTP API é a forma mais popular entre os desenvolvedores quando querem
efetuar integraçõe utilizando uma API, por que existem várias maneiras de se
utilizar, facilitadores e módulos disponiveis nas diversas linguagens,
software e etc. Ela pode ser utilizada tanto com um baixo, como com um alto
volume de mensagens.

Esta é uma implementação na linguagem python da comunicação via SMS, e para
utilizar ela, basta ter uma conta na NSMS (http://www.nsms.com.br).

A documentação completa desta API esta disponível em:
http://www.nsms.com.br/doc/NSMS_Especificacao_HTTP_API.pdf

Para mais informações sobre a empresa e o produto, veja
http://www.nsms.com.br

"""

__author__ = 'Thiago Rondon'
__license__ = 'Python Software Foundation License version 2'
__url__ = 'http://www.nsms.com.br/'

import urllib

class NSMS(object):
    def __init__(self, username, password, baseurl = 'http://api.nsms.com.br/api'):
        self.username = username
        self.password = password
        self.baseurl = baseurl

    def auth(self):
        if not self.username or not self.password:
            raise TypeError, 'Autenticação falhou'

        url = '/'.join( [self.baseurl, 'auth', self.username, self.password] )
        response = urllib.urlopen(url).read()
        return json.dumps(response)

    def send(self, to, message, extra = ''):
        if not to or not message:
            raise TypeError, 'Parâmetro obrigatório: to ou message'

        url = '/'.join( [self.baseurl, 'get', 'json'] )
        url = url + "?to=55"+to+"&content="+message+"&extra="+extra
        return urllib.urlopen(url).read()

