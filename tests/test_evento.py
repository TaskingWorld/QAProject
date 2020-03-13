import pytest

from QAProject.persona.mentor import Mentor
from QAProject.estado import Estado
from QAProject.actividad.core import Actividad

@pytest.fixture
def prepara_datos():
    mentor = Mentor('Pepe', 'Moreno',1)
    actividad = Actividad('Curso',mentor,[],Estado.ABIERTA,20,mentor)
    return [mentor, actividad]

def test_consulta_actividad(prepara_datos):
    estado = Estado.ABIERTA
    assert prepara_datos[1].estado_curso()==estado
