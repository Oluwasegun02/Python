# coffeeMachine//
#  any variable that start with _ are private dont call the out side the class
# Encapsulation
class Coffeemachine:
    """Coffee machine."""
    _hot_water_temp = 100
    
    def _heat_water(self):
        """Heat water."""
        print('heating water...')

    def _grind_beans(self):
        """Grind coffee beans."""
        print('Grinding beans')
    
    def _pour_water(self):
        """pour Water."""
        print('Pouring water...')
    
    def make_coffee(self):
        """Make a coffee."""
        self. _heat_water()
        self._grind_beans()
        self._pour_water()
        print('COFFEE')