# coding:latin-1
from lib.aprend_ref.memoria_aprend import MemoriaAprend


class MemoriaEsparsa(MemoriaAprend):

    def __init__(self, valor_omissao=0):
        """
        Construtor da classe MemoriaEsparsa que afeta o valor por omissão com o passado como parâmetro ou 0

        Parameters
        ----------
        valor_omissao : int
        memoria : dict
        """
        self.__valor_omissao = valor_omissao
        self.__memoria = {}

    def actualizar(self, s, a, q):
        self.__memoria[(s, a)] = q

    def obter(self, s, a):
        return self.__memoria.get((s, a), self.__valor_omissao)

    @property
    def memoria(self):
        return self.__memoria