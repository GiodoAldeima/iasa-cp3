# coding:latin-1

from lib.plan.modelo_plan import ModeloPlan


class Planeador:

    def planear(self, modelo_plan, estado_inicial, objectivos):
        """
        Desenvolve um plano

        Parameters
        ----------
        modelo_plan : ModeloPlan
        estado_inicial
            posi��o inicial
        objectivos:list
            lista de objetivos

        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")

    def obter_accao(self, estado):
        """

        Parameters
        ----------
        estado : Estado

        Returns
        -------
        Operador

        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")

    def plano_pendente(self):
        """
        Verifica se o plano est� pendente

        Returns
        -------
        bool
        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")

    def terminar_plano(self):
        """
        Termina o plano

        """
        raise NotImplementedError("Esta classe � uma interface, n�o pode ser invocada")

