from InterfaceCalculator import InterfaceCalculator

class Multiplicate(InterfaceCalculator):
    def __init__(self, values):
        super().__init__(values)
        self.values = values
    
    def MultiplicateValues(self):
        result = 1
        for i in self.values:
            result *= i
        return result
    

