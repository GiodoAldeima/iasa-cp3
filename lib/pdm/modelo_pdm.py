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
        raise NotImplementedError("Esta classe é uma interface, não pode ser invocada")

    def A(self, s):
        """
        Obtém o conjunto de ações associadas a um estado

        Parameters
        ----------
        s : (int,int)
            estado para o qual se quer obter as ações possíveis

        Returns
        -------
        list of Operador
            lista de ações

        """
        raise NotImplementedError("Esta classe é uma interface, não pode ser invocada")

    def T(self, s, a):
        """
        Obtém o estado seguinte, bem como a probabilidade da sua ocorrência

        Parameters
        ----------
        s : (int,int)
            estado
        a : Operador
            ação

        Returns
        -------
            list of (float,(int,int))

        """
        raise NotImplementedError("Esta classe é uma interface, não pode ser invocada")

    def R(self, s, a, sn):
        """
        Obtém o retorno da transição de um estado para outro através de uma ação

        Parameters
        ----------
        s : (int,int)
            estado atual
        a : Operador
            ação
        sn : (int,int)
            estado seguinte

        Returns
        -------
        float
            retorno da transição

        """
        raise NotImplementedError("Esta classe é uma interface, não pode ser invocada")
