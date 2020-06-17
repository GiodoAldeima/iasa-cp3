# coding:latin-1
from lib.ecr.reaccao import Reaccao
from psa.actuador import ESQ,FRT,DIR
from psa.accao import Mover

from lib.ecr.resposta import Resposta


class Contornar(Reaccao):

    def _detectar_estimulo(self, percepcao):
        return (percepcao[ESQ].contacto and percepcao[ESQ].obstaculo) or \
               (percepcao[DIR].contacto and percepcao[DIR].obstaculo)

    def _gerar_resposta(self, estimulo):
        acao = Mover(FRT)
        return Resposta(acao)
