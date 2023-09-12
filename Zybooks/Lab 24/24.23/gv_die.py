import random

class GVDie:

    # Set initial die value
    def __init__(self):
        self.value = None

    # Roll the die to get 1 - 6
    def roll(self):
      self.value = random.randint(1, 6)

    # Return current die value
    def get_value(self):
      return self.value

    # Allows dice to be compared if necessary
    def compare_to(self, d):
        return self.value == d.value
