import datetime
from typing import List

from estado import Estado
from persona.mentor import Mentor
from persona.asistente import Asistente

class Actividad(object):

    def __init__(self, nombre: str, organizador: Mentor, \
        asistentes: List[Asistente] , estado: Estado, AFORO_MAX: int, \
        mentor: Mentor,  fecha: datetime = datetime.datetime.now()):

        self.nombre = nombre
        self.fecha = fecha
        self.organizador = organizador
        self.asistentes = asistentes
        self.estado = estado
        self.AFORO_MAX = AFORO_MAX
        self.mentor = mentor
        self.asistentes = asistentes

    def cambiar_estado(self, estado: Estado):
        self.estado = estado

    def inscribir(self, asistente: Asistente):
        if (Estado(self.estado) == Estado.COMPLETA):
            print('No se puede inscribir, no hay plazas')
        elif(Estado(self.estado) == Estado.CERRADA or Estado.FINALIZADA or Estado.CANCELADA):
            print('No se puede inscribir a esta actividad')
        else:
            self.asistentes.append(asistente) #HU3
            if len(self.asistentes == self.AFORO_MAX):
                self.estado = Estado.COMPLETA
    
    def desinscribir(self, asistente: Asistente):
        if asistente not in self.asistentes:
            print('No estas inscrito en este evento')
        else:
            self.asistentes.remove(asistente)


        

    