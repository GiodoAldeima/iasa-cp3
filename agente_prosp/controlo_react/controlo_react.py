from agente_prosp.controlo import Controlo
from lib.ecr.comportamento import Comportamento
from psa.agente import Percepcao
from psa.accao import Accao


class ControloReact(Controlo):

    def __init__(self, comportamento):
        """

        Parameters
        ----------
        comportamento : Comportamento
            comportamento do agente
        """
        assert isinstance(comportamento,
                          Comportamento), "O parametro relativo ao comportamento nao e uma subclasse de Comportamento!"
        self.__comportamento = comportamento

    def processar(self, percepcao):
        """
        Obtem uma acao a partir de uma percecao usando o mecanismo de resposta

        Parameters
        ----------
        percepcao : Percepcao

        Returns
        -------
        Accao
            acao associada a resposta obtida do estimulo
        """
        resposta = self.__comportamento.activar(percepcao)
        if resposta is not None:
            return resposta.accao
