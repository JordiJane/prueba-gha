from InterfaceCalculator import InterfaceCalculator

class Division(InterfaceCalculator):
    def __init__(self, values):
        super().__init__(values)
        self.values = values
    
    def DivisionValues(self):
        try:
            result = self.values[0]  
            for i in self.values[1:]:  
                result /= i  
        except ZeroDivisionError:
            print("No podemos dividir por cero")
            return ZeroDivisionError
        
        return result

