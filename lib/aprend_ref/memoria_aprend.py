# coding:latin-1

from pee.modprob.operador import Operador


class MemoriaAprend:

    def actualizar(self, s, a, q):
        """
        Atualiza o valor da estimativa de um estado e a��o com o valor de um par�metro

        Parameters
        ----------
        s : (int,int)
            estado
        a : Operador
            a��o
        q : float
            estimativa com que vai ser atualizada a mem�ria

        Returns
        -------
        None
        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")

    def obter(self, s, a):
        """
        Devolve o valor da estimativa de um estado e a��o passados como par�metro

        Parameters
        ----------
        s : (int,int)
            estado
        a : Operador
            a��o

        Returns
        -------
        float
            estimativa
        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")
