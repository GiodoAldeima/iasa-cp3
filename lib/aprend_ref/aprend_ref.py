# coding:latin-1

from pee.modprob.operador import Operador
from lib.aprend_ref.sel_accao import SelAccao
from lib.aprend_ref.memoria_aprend import MemoriaAprend


class AprendRef:

    def __init__(self, mem_aprend, sel_accao):
        """
        Construtor da classe; Afeta os parâmetros recebidos a atributos

        Parameters
        ----------
        mem_aprend : MemoriaAprend
            memória de aprendizagem
        sel_accao : SelAccao
            selecionador da ação
        """
        self._mem_aprend = mem_aprend
        self._sel_accao = sel_accao

    def aprender(self, s, a, r, sn):
        """
        Atualiza o valor Q na memória para o estado seguinte, e a ação que maximiza a sua estimativa

        Parameters
        ----------
        s : (int,int)
            estado
        a : Operador
            ação
        r : float
            reforço
        sn : (int,int)
            estado seguinte

        Returns
        -------
        None
        """
        raise NotImplementedError("Este método é abstrato, deve ser implementado por sub-classes")
