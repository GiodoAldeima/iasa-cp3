# coding:latin-1
from lib.aprend_ref.aprend_ref import AprendRef

from lib.aprend_ref.sel_accao import SelAccao
from lib.aprend_ref.memoria_aprend import MemoriaAprend


class AprendQ(AprendRef):

    def __init__(self, mem_aprend, sel_accao, alfa, gama):
        """
        Construtor da classe; Afeta os par�metros recebidos a atributos

        Parameters
        ----------
        mem_aprend : MemoriaAprend
            mem�ria de aprendizagem
        sel_accao : SelAccao
            selecionador da a��o
        alfa : float
            fator de aprendizagem
        gama : float
            fator de desconto temporal
        """
        super().__init__(mem_aprend, sel_accao)
        self._alfa = alfa
        self._gama = gama

    def aprender(self, s, a, r, sn):
        qsa = self._mem_aprend.obter(s, a)
        an = self._sel_accao.max_accao(sn)
        qsnan = self._mem_aprend.obter(sn, an)
        q = qsa + self._alfa * (r + self._gama * qsnan - qsa)
        self._mem_aprend.actualizar(s, a, q)
