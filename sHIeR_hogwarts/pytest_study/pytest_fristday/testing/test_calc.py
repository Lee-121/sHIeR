from calc import Calculator

#import sys
#print(sys.path)

class TestCalc:


    def test_add1(self):

        calc = Calculator()

        r = calc.add(5,6)

        assert 11 == r

    def test_add2(self):

        calc = Calculator()

        r = calc.add(600,600)

        assert 1200 == r

    @pytest.mark.add
    def test_add3(self):

        calc = Calculator()

        r = calc.add(-1,-3)

        assert -4 == r

