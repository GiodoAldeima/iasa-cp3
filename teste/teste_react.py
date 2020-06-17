# coding:latin-1

import psa
from agente_prosp.agente_prospector import AgenteProspector
from agente_prosp.controlo_react.controlo_react import ControloReact
from agente_prosp.controlo_react.reaccoes.recolher import Recolher as Comportamento

psa.iniciar("amb/amb1.das")
controlo = ControloReact(Comportamento())
agente = AgenteProspector(controlo)
psa.executar(agente)
