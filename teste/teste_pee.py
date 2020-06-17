# coding:latin-1

import psa
from agente_prosp.agente_prospector import AgenteProspector
from agente_prosp.controlo_delib.controlo_delib import ControloDelib
from pee.melhorprim.procura_aa import ProcuraAA
from pee.melhorprim.procura_sofrega import ProcuraSofrega
from pee.melhorprim.procura_custo_unif import ProcuraCustoUnif
from lib.plan.plan_pee.plan_pee import PlanPEE

psa.iniciar("amb/amb1.das")
mec_pee = ProcuraAA()
# mec_pee = ProcuraSofrega()
# mec_pee = ProcuraCustoUnif()
planeador = PlanPEE(mec_pee)
controlo = ControloDelib(planeador)
agente = AgenteProspector(controlo)
psa.executar(agente)
