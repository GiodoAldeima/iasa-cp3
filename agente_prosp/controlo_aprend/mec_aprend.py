# coding:latin-1
from lib.aprend_ref.aprend_q import AprendQ
from lib.aprend_ref.memoria_esparsa import MemoriaEsparsa
from lib.aprend_ref.sel_accao_egreedy import SelAccaoEGreedy
import psa


# alfa=0.5,gama=0.9;epsilon=0.01
class MecAprend:
    """
    Mecanismo de Aprendizagem
    """

    def __init__(self, accoes):
        """

        Parameters
        ----------
        accoes
        """
        self.__accoes = accoes
        self.__mem_aprend = MemoriaEsparsa()
        self.__sel_accao = SelAccaoEGreedy(self.__mem_aprend, accoes, 0.01)
        self.__aprend_ref = AprendQ(self.__mem_aprend, self.__sel_accao, 0.5, 0.9)

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
        self.__aprend_ref.aprender(s, a, r, sn)
        self.mostrar(s)

    def seleccionar_accao(self, s):
        return self.__sel_accao.seleccionar_accao(s)


    def mostrar(self,s):
        psa.vis(1).limpar()
        psa.vis(1).aprendref(self.__aprend_ref)
        psa.vis(2).accoesestado(s,self.__accoes,self.__mem_aprend.memoria)
