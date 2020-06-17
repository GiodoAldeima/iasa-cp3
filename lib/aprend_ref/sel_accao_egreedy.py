# coding:latin-1
from lib.aprend_ref.sel_accao import SelAccao
from lib.aprend_ref.memoria_aprend import MemoriaAprend
from random import choice, random, shuffle
from pee.modprob.operador import Operador


class SelAccaoEGreedy(SelAccao):
    """
    Representa um mecanismo de sele��o do tipo Epsilon Greedy;
    A a��o selecionada � aleat�ria com probabilidade Epsilon,
     ou � a que tem um refor�o melhor com probabilidade 1-Epsilon
    """

    def __init__(self, mem_aprend, accoes, epsilon):
        """
        Construtor da classe

        Parameters
        ----------
        mem_aprend : MemoriaAprend
        accoes : list
            lista de a��es
        epsilon : float
            valor que permite decidir quando se explora e quando se aproveita
        """
        self.__mem_aprend = mem_aprend
        self.__epsilon = epsilon
        self.__accoes = accoes

    def seleccionar_accao(self, s):
        for a in self.__accoes:
            return self.max_accao(s) if random() > self.__epsilon else self.explorar(s)

    def max_accao(self, s):
        """
        Devolve a a��o com maior refor�o

        Parameters
        ----------
        s : (int,int)
            estado/posi��o

        Returns
        -------
        Operador
            a��o com maior refor�o

        """
        shuffle(self.__accoes)
        am = max(self.__accoes, key=lambda a: self.__mem_aprend.obter(s, a))
        return am

    def explorar(self, s):
        """
        Seleciona uma a��o aleat�riamente da lista de a��es poss�veis

        Parameters
        ----------
        s : (int,int)
            estado/posi��o

        Returns
        -------
        Operador
            uma a��o aleat�ria
        """
        return choice(self.__accoes)

    @property
    def accoes(self):
        return self.__accoes
