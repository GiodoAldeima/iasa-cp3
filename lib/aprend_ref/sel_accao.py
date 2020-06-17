# coding:latin-1
from pee.modprob.operador import Operador


class SelAccao:

    def seleccionar_accao(self, s):
        """
        Seleciona a ação a executar

        Parameters
        ----------
        s :(int,int)
            estado

        Returns
        -------
        Operador
            ação a executar
        """
        raise NotImplementedError("Esta classe é uma interface, não pode ser invocada")
