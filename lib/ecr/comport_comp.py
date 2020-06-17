# coding:latin-1
from lib.ecr.comportamento import Comportamento


class ComportComp(Comportamento):

    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos

    def activar(self, percepcao):
        respostas = list(map(lambda c: c.activar(percepcao), self.__comportamentos))  # obter todas as respostas
        naoNones = [r for r in respostas if r]  # remover Nones das respostas
        return self.seleccionar_resposta(naoNones)

    def seleccionar_resposta(self, respostas):
        raise NotImplementedError("Este método é abstrato, deve ser implementado por sub-classes")
