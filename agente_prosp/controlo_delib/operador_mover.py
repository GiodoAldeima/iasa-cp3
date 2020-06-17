# coding:latin-1
from pee.modprob.operador import Operador
from psa.accao import Mover
from psa.util import mover, dist
from psa.elementos import VAZIO, ALVO


class OperadorMover(Operador):

    def __init__(self, modelo_mundo, ang):
        """
        Construtor da classe OperadorMover, que implementa a interface Operador

        Parameters
        ----------
        modelo_mundo : ModeloMundo
        ang : float
        """
        super().__init__()
        self.__accao = Mover(ang, ang_abs=True)
        self.__ang = ang
        self.__modelo_mundo = modelo_mundo

    def aplicar(self, estado):
        novo_estado = mover(estado, self.__ang)
        elemento = self.__modelo_mundo.obter_elem(estado)
        if elemento in [VAZIO, ALVO]:
            return novo_estado

    def custo(self, estado, novoEstado):
        return max(dist(estado, novoEstado), 1)

    @property
    def accao(self):
        return self.__accao
