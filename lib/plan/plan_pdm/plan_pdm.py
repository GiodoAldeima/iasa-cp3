# coding:latin-1
from lib.pdm.pdm import PDM
from lib.plan.plan_pdm.modelo_pdm_plan import ModeloPDMPlan
from lib.plan.planeador import Planeador


class PlanPDM(Planeador):
    """
    Planeador PDM
    """

    def __init__(self):
        self.__gama = 0.85
        self.__delta_max = 1
        self.__pdm = PDM(self.__gama, self.__delta_max)
        self.__utilidade = {}
        self.__politica = {}

    def planear(self, modelo_plan, estado_inicial, objectivos):
        if objectivos:
            modelo_plan = ModeloPDMPlan(modelo_plan, objectivos)
            self.__utilidade, self.__politica = self.__pdm.resolver(modelo_plan)

    def obter_accao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)

    def plano_pendente(self):
        return self.__politica

    def terminar_plano(self):
        self.__politica=[]

    def mostrar(self,vis,estado):
        if self.__politica:
            vis.limpar()
