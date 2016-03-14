from random import randint

from ex1.evento import Evento


class Gerador():
    def __init__(self, msg):
        self.msg = msg

    def gerar_evento(self, tempo):
        """
        Método que gera evento levando em conta tempo de execução.
        :return: Instancia de Evento ou Nulo se não for para gerar envento
        """
        raise NotImplementedError()


class GeradorDecorator(Gerador):
    def __init__(self, msg, gerador, despachador):
        super().__init__(msg)
        self._despachador = despachador
        self._gerador = gerador

    def gerar_evento(self, tempo):
        evento = self._gerador.gerar_evento(tempo)
        if evento:
            self._despachador.despachar(evento)


class TempoEstrategia():
    def deve_gerar_evento(self, tempo):
        """
        Método abstrato que returna verdadeiro se evento deve ser gerado e falso caso contrário
        :return: bool
        """
        raise NotImplementedError('Deve definir estratégia de tempo')


class Tempo5Segundos(TempoEstrategia):
    def deve_gerar_evento(self, tempo):
        return tempo % 5 == 0


class TempoAleatorio(TempoEstrategia):
    def __init__(self):
        self._proximo_tempo = randint(1, 10)

    def deve_gerar_evento(self, tempo):
        flag = self._proximo_tempo <= tempo
        if flag:
            self._proximo_tempo += randint(1, 10)
        return flag


class TransformadorString():
    def transformar(self, s, tempo):
        """
        Recebe string e transforma de acordo com estratégia
        :param s: string a ser transformada
        :param tempo: Tempo que string foi transformada
        :return: string transformada
        """
        raise NotImplementedError('Deve ser implementado')


class TransformadorNulo(TransformadorString):
    def transformar(self, s, tempo):
        return s


class TransformadorComTempo(TransformadorString):
    def transformar(self, s, tempo):
        return '{}. Tempo={}'.format(s, tempo)


class GeradorBridge(Gerador):
    def __init__(self, msg, tempo_strategia, transformador):
        super().__init__(msg)
        self._transformador = transformador
        self._tempo_strategia = tempo_strategia

    def gerar_evento(self, tempo):
        if self._tempo_strategia.deve_gerar_evento(tempo):
            s = self._transformador.transformar(self.msg, tempo)
            return Evento(s)
