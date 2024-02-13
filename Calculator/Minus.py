from InterfaceCalculator import InterfaceCalculator

class Minus(InterfaceCalculator):
    def __init__(self, values):
        super().__init__(values)
        self.values = values
    
    def MinusValues(self):
        result = 0
        for i in self.values:
            result -= i
        return result

