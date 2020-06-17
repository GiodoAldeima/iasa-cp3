# coding:latin-1
from lib.plan.plan_pee.problema_plan import ProblemaPlan
from lib.plan.planeador import Planeador
from pee.mecproc.procura import Procura


class PlanPEE(Planeador):
    """
    Planeador com recurso a um mecanismo de procura de espaço de estados
    """

    def __init__(self, mec_pee):
        """
        Construtor da classe

        Parameters
        ----------
        mec_pee : Procura
        """
        self.__mec_pee = mec_pee
        self.__plano = []

    def planear(self, modelo_plan, estado_inicial, objetivos):
        problema = ProblemaPlan(estado_inicial, objetivos[0], modelo_plan.operadores())
        solucao = self.__mec_pee.resolver(problema)
        if solucao is not None:
            self.__plano = [no.operador for no in solucao[1:]]

    def obter_accao(self, estado):
        if self.__plano is not None and len(self.__plano) > 0:
            return self.__plano.pop(0)

    def plano_pendente(self):
        return self.__plano

    def terminar_plano(self):
        self.__plano = None

    def mostrar(self, vis, estado):
        """
        Para mostrar na plataforma de visualização
        """
        vis.campo(self.__mec_pee.obter_explorados())
        vis.plano(estado, self.__plano)
        vis.marcar([estado], 1)
