import psa
from psa.agente import Agente
from psa.accao import Avancar


class AgenteTeste(Agente):
    def executar(self):
        self.actuador.actuar(Avancar())


psa.iniciar("amb/amb1.das")
psa.executar(AgenteTeste())
