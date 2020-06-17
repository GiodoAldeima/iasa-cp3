# coding:latin-1

from psa.actuador import DIR,FRT

from psa.accao import Rodar

from lib.ecr.reaccao import Reaccao
from lib.ecr.resposta import Resposta


class Evitar(Reaccao):

    def _detectar_estimulo(self, percepcao):
        return percepcao[FRT].contacto and percepcao[FRT].obstaculo

    def _gerar_resposta(self, estimulo):
        accao = Rodar(DIR)
        return Resposta(accao)
