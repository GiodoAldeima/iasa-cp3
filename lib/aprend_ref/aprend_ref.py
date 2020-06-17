# coding:latin-1

from pee.modprob.operador import Operador
from lib.aprend_ref.sel_accao import SelAccao
from lib.aprend_ref.memoria_aprend import MemoriaAprend


class AprendRef:

    def __init__(self, mem_aprend, sel_accao):
        """
        Construtor da classe; Afeta os par�metros recebidos a atributos

        Parameters
        ----------
        mem_aprend : MemoriaAprend
            mem�ria de aprendizagem
        sel_accao : SelAccao
            selecionador da a��o
        """
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao

    def aprender(self, s, a, r, sn):
        """
        Atualiza o valor Q na mem�ria para o estado seguinte, e a a��o que maximiza a sua estimativa

        Parameters
        ----------
        s : (int,int)
            estado
        a : Operador
            a��o
        r : float
            refor�o
        sn : (int,int)
            estado seguinte

        Returns
        -------
        None
        """
        raise NotImplementedError("Este m�todo � abstrato, deve ser implementado por sub-classes")
