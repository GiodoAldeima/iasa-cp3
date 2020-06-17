# coding:latin-1
from pee.modprob.operador import Operador


class SelAccao:

    def seleccionar_accao(self, s):
        """
        Seleciona a a��o a executar

        Parameters
        ----------
        s :(int,int)
            estado

        Returns
        -------
        Operador
            a��o a executar
        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")
