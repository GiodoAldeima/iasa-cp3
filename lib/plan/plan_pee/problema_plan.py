# coding:latin-1
from pee.modprob.problema_heur import ProblemaHeur
from psa.util import dist


class ProblemaPlan(ProblemaHeur):
    """
    Subclasse de ProblemaHeur; Representa um problema de planeamento
    Tem um estado inicial, final e o conjunto de operadores
    """

    def __init__(self, estado_inicial, estado_final, operadores):
        super().__init__(estado_inicial, operadores)
        self.__estado_final = estado_final

    def objectivo(self, estado):
        """
        Verifica se o estado passado como parâmetro é o objetivo

        Parameters
        ----------
        estado:Estado

        Returns
        -------
        bool
        """
        return estado == self.__estado_final

    def heuristica(self, estado):
        """
        Retorna o valor da heurística, ou seja, a distância entre o estado passado como parâmetro, e o  estado final

        Parameters
        ----------
        estado : Estado

        Returns
        -------
        float
        """
        return dist(estado, self.__estado_final)
