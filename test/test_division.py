import sys
sys.path.append('./Calculator') 
from Division import Division
import pytest

class TestDivision:

    def testDivisionPositives(self):
        div_values = [500,2,2]
        div = Division(div_values)
        result_div = div.DivisionValues()
        assert result_div == 125
    
    def testDivisionNegatives(self):
        div_values = [-100,-2,-2]
        div = Division(div_values)
        result_div = div.DivisionValues()
        assert result_div == -25
    
    def testDivisionByZero(self):
        div_values = [-10,20,0]
        div = Division(div_values)
        result_div = div.DivisionValues()
        assert result_div == ZeroDivisionError
    

    