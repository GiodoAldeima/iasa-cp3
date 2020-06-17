# coding:latin-1
from lib.ecr.comport_comp import ComportComp


class Prioridade(ComportComp):
    def seleccionar_resposta(self, respostas):
        if respostas is not None and len(respostas) > 0:
            prioridades = list(map(lambda r: r.prioridade, respostas))
            return respostas[prioridades.index(max(prioridades))]
