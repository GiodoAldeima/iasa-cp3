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
            lista de respostas obtidas da ativa��o dos comportamentos

        Returns
        -------
        a resposta com maior hierarquia, que corresponde � que est� na primeira posi��o da lista

        """
        return None if(not respostas) else respostas[0]
