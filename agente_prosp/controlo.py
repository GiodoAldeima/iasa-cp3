
"""
Interface que define o contrato relativo ao Controlo
"""
class Controlo:

    """
    Processa uma percecao, retornando uma ação
    """
    def processar(self,percepcao):
        raise NotImplementedError("Esta classe é uma interface, não pode ser invocada")
