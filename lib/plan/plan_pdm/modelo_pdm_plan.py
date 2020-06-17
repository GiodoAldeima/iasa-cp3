# coding:latin-1
from lib.pdm.modelo_pdm import ModeloPDM

from lib.plan.modelo_plan import ModeloPlan


class ModeloPDMPlan(ModeloPDM, ModeloPlan):

    def __init__(self, modelo_plan, objectivos):
        """

        Parameters
        ----------
        modelo_plan : ModeloPlan
        objectivos : list of (int,int)
        """
        self.__rmax = 100
        self.__objectivos = objectivos
        self.__modelo_plan = modelo_plan

    def estados(self):
        return self.S()

    def operadores(self):
        return self.A()

    def S(self):
        return self.__modelo_plan.estados()

    def A(self, s=None):
        # s é ignorado
        return self.__modelo_plan.operadores()

    def T(self, s, a):
        sn = a.aplicar(s)
        return [] if not sn else [(1, sn)]

    def R(self, s, a, sn):
        if sn:
            r = -1 * a.custo(s, sn)
            return r if sn not in self.__objectivos else r + self.__rmax
        return None
