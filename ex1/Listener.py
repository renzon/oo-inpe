from ex1.gerador import Gerador


class Listener():
    def tratar(self, evento):
        """
        Método que deve tratar evento despachado
        :param evento:
        :return:
        """
        raise NotImplementedError('Deve ser implementado por subclasses')


class Impressor(Listener):
    def tratar(self, evento):
        print(evento.s)


class Contador(Listener):
    def __init__(self):
        self._count = 0

    def tratar(self, evento):
        print('Contador: {}'.format(self._count))
        self._count += 1


class GeradorListener(Gerador, Listener):
    def __init__(self, msg):
        super().__init__(msg)
        self._msgs = []

    def gerar_evento(self, tempo):
        print('--------Evento gerador msgs:')
        for m in self._msgs:
            print(m)
        print('--------- Termino de msgs')

    def tratar(self, evento):
        self._msgs.append(evento.s)
