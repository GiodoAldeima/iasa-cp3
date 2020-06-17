# coding:latin-1

import psa
from agente_prosp.agente_prospector import AgenteProspector
from agente_prosp.controlo_delib.controlo_delib import ControloDelib
from lib.plan.plan_pdm.plan_pdm import PlanPDM

psa.iniciar("amb/amb2.das")
planeador = PlanPDM()
controlo = ControloDelib(planeador)
agente = AgenteProspector(controlo)
psa.executar(agente)
