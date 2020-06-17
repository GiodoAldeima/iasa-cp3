# coding:latin-1


class ModeloPlan:
    """Um modelo de planeamento"""

    def estados(self):
        """
        Obter a lista de estados

        Returns
        -------
        list
            lista de estados
        """
        raise NotImplementedError("Esta classe é uma interface, não pode ser invocada")

    def operadores(self):
        """
        Obter a lista de operadores

        Returns
        -------
        list
            lista de operadores
        """
        raise NotImplementedError("Esta classe é uma interface, não pode ser invocada")
