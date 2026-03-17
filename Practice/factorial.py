class Factorial:
    def __init__(self, numb):
        self.number = numb
    
    def process(self):
        numbers = []
        factorial = 1
        for num in range(1, self.number+1):
            numbers.append(num)
        
        for num in numbers:
            factorial *= num
        
        print(factorial)
