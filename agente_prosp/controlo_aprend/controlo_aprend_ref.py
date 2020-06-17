# coding:latin-1
from psa.accao import Mover

from agente_prosp.controlo import Controlo
from agente_prosp.controlo_aprend.mec_aprend import MecAprend
from psa.util import dirmov
from psa.accao import Accao


class ControloAprendRef(Controlo):

    def __init__(self):
        """
        Construtor da classe; Cria os atributos do reforço máximo, estado e ação atuais
        e mecanismo de aprendizagem
        """
        self.__rmax = 100
        self.__s = None
        self.__a = None
        accoes = [Mover(a, ang_abs=True) for a in dirmov()]
        self.__mec_aprend = MecAprend(accoes)

    def processar(self, percepcao):
        """
        Executa um passo do algoritmo Q-Learning

        Parameters
        ----------
        percepcao : Percepcao
            uma perceção

        Returns
        -------
        accao : Accao
            a ação a executar

        """
        sn = percepcao.posicao
        if self.__s is not None:
            r = self.gerar_reforco(percepcao)
            self.__mec_aprend.aprender(self.__s, self.__a, r, sn)
        an = self.__mec_aprend.seleccionar_accao(self.__s)
        self.__s = sn
        self.__a = an
        #print(an)
        return an

    def gerar_reforco(self, percepcao):
        """
        Calcula e devolve o reforço associado à perceção

        Parameters
        ----------
        percepcao

        Returns
        -------
        float
            reforço do passo

        """
        reforco = -1 * percepcao.custo_mov
        if percepcao.carga:
            reforco += self.__rmax
        elif percepcao.colisao:
            reforco += -1 * self.__rmax
        return reforco
