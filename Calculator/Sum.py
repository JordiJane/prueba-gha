class Sum:
    def __init__(self, values):
        self.values = values

    def SumValues(self):
        result = 0
        for i in self.values:
            result += i
        return result

