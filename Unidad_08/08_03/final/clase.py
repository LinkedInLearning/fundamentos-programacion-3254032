class Invitado:
    'Clase común para todos los invitados'

    def __init__(self, nombre, tiquetes):
        self.nombre = nombre
        self.tiquetes = tiquetes

    def mostrarInvitado(self):
        print('Nombre : {}, Tiquetes: {}'.format(self.nombre, self.tiquetes))

    def agregarTiquete(self):
        self.tiquetes += 1
        print('{} el número de tiquetes ahora es {}'.format(self.nombre, self.tiquetes))

invitado1 = Invitado('Eleanor A.', 2)
invitado2 = Invitado('Katherinne M.', 1)
invitado1.mostrarInvitado()
invitado2.mostrarInvitado()
invitado2.agregarTiquete()
invitado2.agregarTiquete()
