from league import Updateable
import logging
import abc

"""
Classed assosicated with gravity are kept here
"""

class GravityManager(Updateable):
    """
    Gravity Manager is a list of gravity regions which tracks what objects 
    in the game are associated with having gravity.
    """

    def __init__(self):
        """
        Inits Gravity Manager. There should only ever be one of these classed in
        play (could have done singleton but life's too short). Sets up 
        a dict to track gravity regions and a list to track GravityBound objects

        Currently all objects affected by gravity only check its affect on the y axis
        Therefore all added gravity retions added should only have a y componenet 
        """
        self.gravity_map = dict()
        self.gravity_bound_objects = []

    def add_object(self, game_object):
        """
        Adds a GravityBound object to the list of objects being tracked for having
        gravity

        param - game_object: The object being appended to list.
        """
        self.gravity_bound_objects.append(game_object)

    def add_gravity(self, gravity_name, gravity_vector):
        """
        Adds a gravity region to the gravity map

        param - gravity_name: The name of the new gravity region
        param - gravity_vector: The vector of force being imposed by this 
        new region
        """
        self.gravity_map[gravity_name] = gravity_vector
    
    def update(self, gameDeltaTime):
        """
        Implements Updatable Game object. Iterates through list of GravityBound
        objects and imparts gravity vectors on them. 

        param - gameDeltaTime: The delta time since this function was last called.
        """
        for object in self.gravity_bound_objects:
            gravity_vector = self.gravity_map[object.get_gravity_name()]
            object.process_gravity(gameDeltaTime, gravity_vector)
        
class GravityBound(abc.ABC):
    """
    Interface for gravity bound objects. Objects that need to have gravity can
    implement this interface.
    """
    @abc.abstractmethod
    def process_gravity(self, game_delta_time, gravity_vector):
        """
        Handled in Gravity Manager to impart gravity on the game object. 
        Ususally adds vector to actors current velocity. 

        param - game_delta_time: The delta time since this function was last called.
        param - gravity_vector: The gravity vector that will be imparted on the actor
        """
        pass
    

        