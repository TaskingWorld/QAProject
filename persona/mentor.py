from persona.core import Persona

class Mentor(Persona):

    def __init__(self, nombre: str, apellidos: str, id: int):
        super().__init__(nombre, apellidos, id)

    def crear_actividad(self): #HU1
        pass

    def cancelar_actividad(self):
        pass

    def abrir_inscripcion(self):
        pass

    def cerrar_inscripcion(self):
        pass

    def eliminar_actividad(self): #HU4
        pass

    def notificar_cambios(self): #HU6
        pass