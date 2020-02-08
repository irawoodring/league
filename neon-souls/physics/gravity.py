import abc
from threading import Lock
import logging

logger = logging.getLogger('GravityManager')

class GravityManager:
    gravity_instance = None
    lock = Lock()

    def __init__(self):
        raise RuntimeError('Use get_instance')
    
    @classmethod
    def get_instance(cls):
        if cls.gravity_instance is None:
            cls.lock.acquire()
            if cls.gravity_instance is None:
                cls.gravity_instance = cls.__new__(cls)
                cls.gravity_instance.gravity_map = {}
            cls.lock.release()
        return cls.gravity_instance

    def add_gravity(self, gravity_name, gravity_vector):
        self.gravity_map[gravity_name] = gravity_vector

    def get_gravity(self, gravity_name):
        logger.debug(gravity_name)
        logger.debug(self.gravity_map)
        return self.gravity_map[gravity_name]

class GravityBound(abc.ABC):
    @abc.abstractmethod
    def process_gravity(self):
        pass
    

        