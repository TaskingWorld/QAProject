import pytest
import datetime

from QAProject.actividad.core import Actividad
from QAProject.persona.mentor import Mentor
from QAProject.estado import Estado


@pytest.fixture
def prepara_datos():
    mentor = Mentor('Pepe', 'Moreno',1)
    actividad = Actividad('Curso',mentor,[],Estado.ABIERTA,20,mentor)
    return [mentor, actividad]


def test_consulta_actividad(prepara_datos):
    assert isinstance(prepara_datos[1].fecha_evento(),datetime.datetime)
