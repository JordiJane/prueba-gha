import InterfaceCalculator

class Minus(InterfaceCalculator):
    def __init__(self, values):
        self.values = values
    
    def MinusValues(self):
        result = 0
        for i in self.values:
            result -= i
        return result

