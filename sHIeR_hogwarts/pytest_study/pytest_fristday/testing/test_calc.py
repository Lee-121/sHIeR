from calc import Calculator


class TestCalc:


    def test_add1(self):
        # 实例化Calculator
        calc = Calculator()
        #调用add方法
        r = calc.add(5,6)
        #断言
        assert 11 == r

    def test_add2(self):
        # 实例化Calculator
        calc = Calculator()
        #调用add方法
        r = calc.add(600,600)
        #断言
        assert 1200 == r

    def test_add3(self):
        # 实例化Calculator
        calc = Calculator()
        #调用add方法
        r = calc.add(-1,-3)
        #断言
        assert -4 == r

