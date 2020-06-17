# coding:latin-1
from psa.sensormultiplo import Percepcao
from psa.util import dirmov

from agente_prosp.controlo_delib.operador_mover import OperadorMover
from lib.plan.modelo_plan import ModeloPlan


class ModeloMundo(ModeloPlan):
    """
    Representa o modelo do mundo

    Attributes
    ----------
    __alterado : bool
        indica se o modelo do mundo foi alterado
    __elementos : dict
        dicionário de elementos, que mapeia uma coordenada a um tipo de elemento(VAZIO,ALVO,...)
    __estados : list[Estado]

    """

    def __init__(self):
        self.__alterado = False
        self.__elementos = {}
        self.__estados = []
        self.__estado = None
        self.__operadores = [OperadorMover(self, ang) for ang in dirmov()]
        print(self.__operadores)

    def actualizar(self, percepcao):
        """
        Atualiza os atributos do modelo do mundo caso hajam diferenças entre os elementos do modelo e a imagem da percepção

        Parameters
        ----------
        percepcao : Percepcao
        """
        self.__estado = percepcao.posicao
        print("ESTADO:", self.__estado)
        if self.__elementos != percepcao.imagem:
            self.__alterado = True
            self.__estados = percepcao.imagem.keys()
            self.__elementos = percepcao.imagem
        else:
            self.__alterado = False

    def estados(self):
        return self.__estados

    def operadores(self):
        return self.__operadores

    def obter_elem(self, estado):
        return self.__elementos.get(estado)

    @property
    def estado(self):
        return self.__estado

    @property
    def alterado(self):
        return self.__alterado

    def mostrar(self, vis):
        alvos_obst={k:v for (k,v) in self.__elementos.items() if v in ['alvo','obst']}
        vis.elementos(alvos_obst)
