# coding:latin-1

from pee.modprob.operador import Operador


class ModeloPDM:

    def S(self):
        """
        Devolve o conjunto de estados do mundo

        Returns
        -------
        list of (int,int)
            lista de estados

        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")

    def A(self, s):
        """
        Obt�m o conjunto de a��es associadas a um estado

        Parameters
        ----------
        s : (int,int)
            estado para o qual se quer obter as a��es poss�veis

        Returns
        -------
        list of Operador
            lista de a��es

        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")

    def T(self, s, a):
        """
        Obt�m o estado seguinte, bem como a probabilidade da sua ocorr�ncia

        Parameters
        ----------
        s : (int,int)
            estado
        a : Operador
            a��o

        Returns
        -------
            list of (float,(int,int))

        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")

    def R(self, s, a, sn):
        """
        Obt�m o retorno da transi��o de um estado para outro atrav�s de uma a��o

        Parameters
        ----------
        s : (int,int)
            estado atual
        a : Operador
            a��o
        sn : (int,int)
            estado seguinte

        Returns
        -------
        float
            retorno da transi��o

        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")
