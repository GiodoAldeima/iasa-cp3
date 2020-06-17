# coding:latin-1
from agente_prosp.controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from lib.ecr.prioridade import Prioridade
from psa.actuador import ESQ, FRT, DIR


class Aproximar(Prioridade):

    def __init__(self):
        super().__init__([AproximarDir(ESQ), AproximarDir(FRT), AproximarDir(DIR)])
