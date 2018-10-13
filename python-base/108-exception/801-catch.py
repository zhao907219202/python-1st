try:
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    print(x / y)
except ZeroDivisionError:
    print("The second number can't be zero")
except(TypeError, NameError, ValueError)as e:
    print(e)


class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print("Division by zero is illegal")
            else:
                raise


calculator = MuffledCalculator()
# calculator.calc('10/0')  ZeroDivisionError: division by zero
calculator.muffled = True
calculator.calc('10/0')
