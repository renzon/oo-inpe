class Despachador():
    def __init__(self):
        self._listeners = []

    def adicionar(self, *listeners):
        self._listeners.extend(listeners)

    def despachar(self, evento):
        for lis in self._listeners:
            lis.tratar(evento)
