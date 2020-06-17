# coding:latin-1
import psa

from agente_prosp.controlo import Controlo
from agente_prosp.controlo_delib.modelo_mundo import ModeloMundo
from psa.agente import Percepcao
from psa.accao import Accao
from psa.elementos import ALVO


class ControloDelib(Controlo):

    def __init__(self, planeador):
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__objectivos = None

    def processar(self, percepcao):
        """

        Parameters
        ----------
        percepcao : Percepcao
            perceção obtida da observação do mundo

        Returns
        -------
            Accao
        """
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        accao = self.__executar()
        self.mostrar()
        return accao

    def __assimilar(self, per):
        """

        Parameters
        ----------
        per : Percepcao

        """
        self.__modelo_mundo.actualizar(per)

    def __reconsiderar(self):
        return self.__modelo_mundo.alterado or not self.__objectivos or self.__planeador.plano_pendente()

    def __deliberar(self):
        """
        Atualiza os objetivos
        """

        self.__objectivos = [estado for estado in self.__modelo_mundo.estados()
                             if self.__modelo_mundo.obter_elem(estado) == ALVO]

    def __planear(self):
        """
        Se existem objetivos é feito o planeamento. Caso contrário, o planeador termina o plano
        """
        if self.__objectivos:
            self.__planeador.planear(self.__modelo_mundo, self.__modelo_mundo.estado, self.__objectivos)
        else:
            self.__planeador.terminar_plano()

    def __executar(self):
        """
        Executa a ação do operador obtido do planeador, se esta não for nula

        Returns
        -------
        Accao
        """
        operador = self.__planeador.obter_accao(self.__modelo_mundo.estado)
        print("OP: ", operador)
        if operador is not None:
            return operador.accao

    def mostrar(self):
        vis = psa.vis(1)
        vis.limpar()
        self.__planeador.mostrar(vis, self.__modelo_mundo.estado)
        self.__modelo_mundo.mostrar(vis)
