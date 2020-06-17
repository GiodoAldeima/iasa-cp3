# coding:latin-1

import psa
from agente_prosp.agente_prospector import AgenteProspector
from agente_prosp.controlo_aprend.controlo_aprend_ref import ControloAprendRef

psa.iniciar("amb/amb3.das",reiniciar=True)
controlo = ControloAprendRef()
agente = AgenteProspector(controlo)
psa.executar(agente)