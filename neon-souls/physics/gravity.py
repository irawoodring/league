from league import Updateable
import logging
import abc

# logger = logging.getLogger('GravityManager')

class GravityManager(Updateable):
    def __init__(self):
        self.gravity_map = dict()
        self.gravity_bound_objects = []

    def add_object(self, game_object):
        self.gravity_bound_objects.append(game_object)

    def add_gravity(self, gravity_name, gravity_vector):
        self.gravity_map[gravity_name] = gravity_vector
    
    def update(self, gameDeltaTime):
        for object in self.gravity_bound_objects:
            gravity_vector = self.gravity_map[object.get_gravity_name()]
            object.process_gravity(gameDeltaTime, gravity_vector)
        
class GravityBound(abc.ABC):
    @abc.abstractmethod
    def process_gravity(self, game_delta_time, gravity_vector):
        pass
    

        