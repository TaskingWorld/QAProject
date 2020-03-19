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
    return [mentor, taller]

def test_consulta_actividad(prepara_datos):
    with mock.patch.object(TinyStorage, 'get_activities', return_value=prepara_datos[1]):
        
        
        class Test(object):
            def __init__(self, database: Storage):
                self.database = database
            
            def consulta_datos(self):
                return self.database.get_activities()
    
        my_database = TinyStorage('test')
        test = Test(my_database)

        assert test.consulta_datos() == prepara_datos[1]