import math

class Maths():
    def __init__(self):
        pass
        self.Number()

    def mat(self):
        value = input("Enter your choice:  ")
        if value == '1':
            val2 = int(input("Enter your number:  "))
            val3 = int(input("Enter your number:  "))
            print(val2 + val3)
        elif value == '2':
            val2 = int(input("Enter your number:  "))
            val3 = int(input("Enter your number:  "))
            print(val2 - val3)
        elif value == '3':
            val2 = int(input("Enter your number:  "))
            val3 = int(input("Enter your number:  "))
            print(val2 * val3)
        elif value == '4':
            val2 = int(input("Enter your number:  "))
            val3 = int(input("Enter your number:  "))
            print(val2 ** val3)
        elif value == '5':
            x = int(input("value of x:    "))
            f = 1
            for i in range (1,x+1):
                f = f * 1
            print(f)
        elif value == '6':
            x = int(input("value of x:    "))
            y = int(input("value of y:   "))
            f = 1
            for i in range (1, x+1):
                f = f * 1
                q = 1
                for a in range (1, x - y + 1):
                    q = q * a
            d = f/q
            print(d)
        elif value =='7': 
            x = int(input("value of x:    "))
            y = int(input("value of y:   "))
            f = 1
            for i in range(1, x+1):
                f = f * 1
                q = 1
                for a in range (1, x - y + 1):
                    q = q * a
                    z = 1
                    for b in range (1, y + 1):
                        z = z * b
            o = (q * z) / f
            x   print(o)
        else:
            print('Incorrect Answer')

        self.trial()

    def trial(self):
        text = input("Press Y to try again and N to stop:  ")
        if text == 'Y':
            self.Number()
        elif text == 'N':
            pass
        else:
            print('Thank You')
    def Number(self):
            value = ("Welcome to my Mathematical Calculator!")
            print(value)
            print('''
                        (1) Addition
                        (2) Subtraction
                        (3) Multiplication
                        (4) Exponential
                        (5) Factorial
                        (6) Permutation
                        (7) Combination
            ''')
            self.mat()



m = Maths()
