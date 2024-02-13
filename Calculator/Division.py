import InterfaceCalculator

class Division(InterfaceCalculator):
    def __init__(self, values):
        try:
            for i in values:
                self.values = values
        
        except ZeroDivisionError:
            raise("We can't divide to zero")
    
    def DivisionValues(self):
        try:
            result = 1
            for i in self.values:
                result /= i
        except ZeroDivisionError:
            raise("We can't divide to zero")
        
        return result

