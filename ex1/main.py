import os

import sys

project_dir = os.path.dirname(__file__)
project_dir = os.path.join('..', project_dir)
project_dir = os.path.abspath(project_dir)

sys.path.append(project_dir)

from ex1.dispatcher import Despachador
from ex1.gerador import GeradorDecorator, Tempo5Segundos, TempoAleatorio, TransformadorNulo, TransformadorComTempo, \
    GeradorBridge
from ex1.listener import Impressor, Contador, GeradorListener

MSG = 'MSG'


def injetar_despachador_e_decorar(gerador):
    return GeradorDecorator(MSG, gerador, despachador)


despachador = Despachador()

gerador_listener = GeradorListener(MSG)
despachador.adicionar(Impressor(), Contador(), gerador_listener)

tempo_5_s = Tempo5Segundos()
tempo_aleatorio = TempoAleatorio()
transformador_nulo = TransformadorNulo()
transformador_com_tempo = TransformadorComTempo()

geradores = (GeradorBridge(MSG, tempo_5_s, transformador_nulo),
             GeradorBridge(MSG, tempo_aleatorio, transformador_com_tempo),
             GeradorBridge(MSG, tempo_aleatorio, transformador_nulo),
             gerador_listener)

geradores = tuple(injetar_despachador_e_decorar(g) for g in geradores)

for tempo in range(1, 20):
    print("###### Tempo: {} #########".format(tempo))
    for gerador in geradores:
        gerador.gerar_evento(tempo)
