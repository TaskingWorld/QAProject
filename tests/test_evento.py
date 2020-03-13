import pytest

from QAProject.actividad.core import Actividad
from QAProject.persona.asistente import Asistente
from QAProject.persona.mentor import Mentor
from QAProject.estado import Estado

def test_consulta_actividad(asistente: Asistente, actividad: Actividad):
    estado = asistente.consultar_actividad(actividad)
    assert isinstance(estado, Estado)


mentor = Mentor('Pepe', 'Moreno',1)
asistente = Asistente('Antonio', 'Jaimez', 2)

actividad = Actividad('Curso',mentor,[asistente],Estado.ABIERTA,20,mentor)

