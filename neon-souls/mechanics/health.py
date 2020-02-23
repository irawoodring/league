
"""
Defines a health object for use by any actor in the game

"""
class Health:
    """
    Defines a health componenet for any actor in the game. Class allows for 
    flexiblity in how health is implemented. Health could be implemented in a 
    low HP system or high HP system. The implementation is up to the programmer
    """

    def __init__(self, initial_health, loss_rate):
        """
        Inits Health object. Sets the inital health and the default health loss 
        rate. Asserts that both values are positive 

        param - initial_health: The inital health for this health object
        param - loss_rate: The default loss rate for this health object
        """
        assert initial_health > 0
        assert loss_rate > 0

        self.MAX_HEALTH = initial_health
        self.current_health = initial_health
        self.loss_rate = loss_rate

    def lose_health(self, custom_hit=None):
        """
        Triggers health loss on this health object. Can optionally specify how 
        much health is lost. Otherwise, the default will be used. 

        param - custom_hit: A custom hit rate for the health loss. Asserted to 
        be positive. 
        """
        if custom_hit is None:
            self.current_health = self.current_health - self.loss_rate
        else:
            assert custom_hit > 0
            self.current_health = self.current_health - custom_hit
    
    def gain_health(self, amount):
        """
        Allows health object to gain health. 

        param - amount: The amount of health that will be gained. Asserted to be 
        positive.
        """
        assert amount > 0
        self.current_health = self.current_health + amount

    def at_zero(self):
        """
        Returns weather this health object has a health of zero or less. 
        """
        return self.current_health <= 0
