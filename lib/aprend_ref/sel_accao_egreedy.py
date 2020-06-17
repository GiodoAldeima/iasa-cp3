# coding:latin-1
from lib.aprend_ref.sel_accao import SelAccao
from lib.aprend_ref.memoria_aprend import MemoriaAprend
from random import choice, random, shuffle
from pee.modprob.operador import Operador


class SelAccaoEGreedy(SelAccao):
    """
    Representa um mecanismo de seleção do tipo Epsilon Greedy;
    A ação selecionada é aleatória com probabilidade Epsilon,
     ou é a que tem um reforço melhor com probabilidade 1-Epsilon
    """

    def __init__(self, mem_aprend, accoes, epsilon):
        """
        Construtor da classe

        Parameters
        ----------
        mem_aprend : MemoriaAprend
        accoes : list
            lista de ações
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
        Devolve a ação com maior reforço

        Parameters
        ----------
        s : (int,int)
            estado/posição

        Returns
        -------
        Operador
            ação com maior reforço

        """
        shuffle(self.__accoes)
        am = max(self.__accoes, key=lambda a: self.__mem_aprend.obter(s, a))
        return am

    def explorar(self, s):
        """
        Seleciona uma ação aleatóriamente da lista de ações possíveis

        Parameters
        ----------
        s : (int,int)
            estado/posição

        Returns
        -------
        Operador
            uma ação aleatória
        """
        return choice(self.__accoes)

    @property
    def accoes(self):
        return self.__accoes
