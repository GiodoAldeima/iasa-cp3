# coding:latin-1
from lib.ecr.reaccao import Reaccao
from psa.accao import Mover

from lib.ecr.resposta import Resposta


class AproximarDir(Reaccao):

    def __init__(self, direcao):
        self.__direccao = direcao

    def _detectar_estimulo(self, percepcao):
        if percepcao[self.__direccao].alvo:
            return percepcao[self.__direccao].distancia

    def _gerar_resposta(self, estimulo):
        accao = Mover(self.__direccao)
        prioridade = 1 / estimulo
        return Resposta(accao, prioridade)
