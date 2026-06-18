# Classes/Objects

class AlgebraicCalculation:
    def binomialSquare(self, a=0, b=0):
        return f"({a} + {b})^2 = {a*a + b*b + 2*a*b}"
    
    def squareOfDifference(self, a=0, b=0):
        return f"({a} - {b})^2 = {a*a + b*b - 2*a*b}"

class Calculator(AlgebraicCalculation):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"
    
    def sub(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"
    
    def mul(self):
        return f"{self.num1} x {self.num2} = {self.num1 * self.num2}"
    
    def div(self):
        return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"
    
    
def main():
    obj = Calculator(4,6)
    print(obj.sum())
    print(obj.sub())
    print(obj.mul())
    print(obj.div())
    print(obj.binomialSquare(4,7))
    print(obj.squareOfDifference(5,8))

main()