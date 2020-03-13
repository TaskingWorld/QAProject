from persona.core import Persona
from actividad.core import Actividad

class Asistente(Persona):

    def __init__(self, nombre: str, apellidos: str, id: int):
        super().__init__(nombre, apellidos, id)


    def consultar_actividad(self, actividad: Actividad):
        return actividad.estado_curso()
        

    def inscribirme(self): #HU2
        pass

    def desinscribirme(self): #HU5
        pass