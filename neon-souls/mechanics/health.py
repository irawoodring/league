

class Health:
    def __init__(self, initial_health, loss_rate):
        assert initial_health > 0
        assert loss_rate > 0

        self.MAX_HEALTH = initial_health
        self.current_health = initial_health
        self.loss_rate = loss_rate

    def lose_health(self, custom_hit=None):
        if custom_hit is None:
            self.current_health = self.current_health - self.loss_rate
        else:
            assert custom_hit > 0
            self.current_health = self.current_health - custom_hit
    
    def gain_health(self, amount):
        assert amount > 0
        self.current_health = self.current_health + amount

    def at_zero(self):
        return self.current_health <= 0
