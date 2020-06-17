# coding:latin-1

from lib.pdm.modelo_pdm import ModeloPDM


class PDM:

    def __init__(self, gama, delta_max):
        self.__gama = gama  # fator de desconto temporal
        self.__delta_max = delta_max  # limiar de convergência

    def utilidade(self, modelo):
        """

        Parameters
        ----------
        modelo : ModeloPDM

        Returns
        -------
        dict[(int,int), float]
            mapa de pares estado utilidade
        """
        S, A = modelo.S, modelo.A  # renomear funções
        U = {s: 0 for s in S()}
        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max(self.util_accao(s, a, Uant, modelo) for a in A(s))
                delta = max(delta, abs(U[s] - Uant[s]))
            if delta < self.__delta_max:
                break
        return U

    def util_accao(self, s, a, U, modelo):
        """
        Obtém a utilidade da execução de uma ação num estado

        Parameters
        ----------
        s : (int,int)
            estado
        a : Operador
            ação
        U :  dict[(int,int), float]
            utilidade
        modelo : ModeloPDM
            modelo

        Returns
        -------
        float
            a utilidade
        """
        T, R, gama = modelo.T, modelo.R, self.__gama
        return sum(p * (R(s, a, sn) + gama * U[sn]) for (p, sn) in T(s, a))

    def politica(self, U, modelo):
        """
        Calcula a politica ótima

        Parameters
        ----------
        U : dict[(int,int), float]
            utilidade
        modelo : ModeloPDM
            modelo

        Returns
        -------
        dict[(int,int), float]
            a política ótima

        """
        pol = {}
        for s in modelo.S():
            pol[s] = max(modelo.A(s), key=lambda a: self.util_accao(s, a, U, modelo))
        return pol

    def resolver(self, modelo):
        utilidade = self.utilidade(modelo)
        return utilidade, self.politica(utilidade, modelo)
