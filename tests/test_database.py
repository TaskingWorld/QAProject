import pytest
from unittest import mock

from QAProject.storage.core import Storage
from QAProject.storage.tiny_storage import TinyStorage
from QAProject.actividad.core import Actividad
from QAProject.persona.mentor import Mentor
from QAProject.estado import Estado

@pytest.fixture
def prepara_datos(): 
    # Save a couple of test activities
    mentor = Mentor('Pepe', 'Moreno',1)
    taller = Actividad('Taller',mentor,[],Estado.ABIERTA,5,mentor)
    return taller

def test_consulta_actividad(prepara_datos):
    with mock.patch.object(Storage, 'get_activities', return_value=prepara_datos):
        database = TinyStorage('prueba.json')
        assert database.get_activities() == prepara_datos