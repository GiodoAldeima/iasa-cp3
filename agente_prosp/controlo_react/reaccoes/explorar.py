# coding:latin-1

from lib.ecr.resposta import Resposta
from lib.ecr.comportamento import Comportamento

from random import choice

from psa.actuador import ESQ, FRT, DIR


class Explorar(Comportamento):

    def activar(self, _):
        accao = choice([(ESQ, 1), (FRT,1), (DIR,1)])
        return Resposta(accao)
