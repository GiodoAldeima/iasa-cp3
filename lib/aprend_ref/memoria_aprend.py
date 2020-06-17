# coding:latin-1

from pee.modprob.operador import Operador


class MemoriaAprend:

    def actualizar(self, s, a, q):
        """
        Atualiza o valor da estimativa de um estado e ação com o valor de um parâmetro

        Parameters
        ----------
        s : (int,int)
            estado
        a : Operador
            ação
        q : float
            estimativa com que vai ser atualizada a memória

        Returns
        -------
        None
        """
        raise NotImplementedError("Esta classe é uma interface, não pode ser invocada")

    def obter(self, s, a):
        """
        Devolve o valor da estimativa de um estado e ação passados como parâmetro

        Parameters
        ----------
        s : (int,int)
            estado
        a : Operador
            ação

        Returns
        -------
        float
            estimativa
        """
        raise NotImplementedError("Esta classe é uma interface, não pode ser invocada")
