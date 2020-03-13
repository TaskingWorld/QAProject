from QAProject.persona.core import Persona


class Asistente(Persona):

    def __init__(self, nombre: str, apellidos: str, id: int):
        super().__init__(nombre, apellidos, id)


    def consultar_actividad(self):
        pass
        

    def inscribirme(self): #HU2
        pass

    def desinscribirme(self): #HU5
        pass