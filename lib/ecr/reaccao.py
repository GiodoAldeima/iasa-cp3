# coding:latin-1
from lib.ecr.comportamento import Comportamento


class Reaccao(Comportamento):

    def activar(self, percepcao):
        estimulo = self._detectar_estimulo(percepcao)
        if estimulo is not None and estimulo is not False:
            return self._gerar_resposta(estimulo)

    def _detectar_estimulo(self, percepcao):
        raise NotImplementedError("Este método é abstrato, deve ser implementado por sub-classes")

    def _gerar_resposta(self, estimulo):
        raise NotImplementedError("Este método é abstrato, deve ser implementado por sub-classes")
