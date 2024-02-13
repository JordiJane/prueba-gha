import InterfaceCalculator

class Multiplicate(InterfaceCalculator):
    def __init__(self, values):
        self.values = values
    
    def MultiplicateValues(self):
        result = 1
        for i in self.values:
            result *= i
        return result
    

