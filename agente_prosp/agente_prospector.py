import psa
from psa.agente import Agente
from agente_prosp.controlo import Controlo


class AgenteProspector(Agente):

    # "_"  - protegido
    # "__" - privado
    #  ""  - público

    def __init__(self, controlo):
        super().__init__()
        assert isinstance(controlo, Controlo), "O parâmetro relativo ao controlo não é uma subclasse de Controlo!"
        self.controlo = controlo

    def executar(self):
        percepcao = self.__percepcionar()
        accao = self.__processar(percepcao)
        self.__actuar__(accao)

    def __percepcionar(self):
        return self.sensor_multiplo.detectar()

    def __processar(self, percepcao):
        return self.controlo.processar(percepcao)

    def __actuar__(self, accao):
        if accao is not None:
            self.actuador.actuar(accao)
