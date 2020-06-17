# coding:latin-1
from lib.ecr.comport_comp import ComportComp


class Hierarquia(ComportComp):

    def __init__(self,comportamentos):
        super().__init__(comportamentos)

    def seleccionar_resposta(self, respostas):
        """
        Seleciona a resposta com maior  hierarquia

        Parameters
        ----------
        respostas : list
            lista de respostas obtidas da ativação dos comportamentos

        Returns
        -------
        a resposta com maior hierarquia, que corresponde à que está na primeira posição da lista

        """
        return None if(not respostas) else respostas[0]
