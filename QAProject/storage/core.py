
from QAProject.actividad.core import Actividad

class Storage(object):
    
    def save_activitiy(self, actividad: Actividad):
        raise NotImplementedError('Subclasses must override!')

    
    def get_activities(self):
        raise NotImplementedError('Subclasses must override!')

    
    def eliminate_activity(self, actividad: Actividad):
        raise NotImplementedError('Subclasses must override!')