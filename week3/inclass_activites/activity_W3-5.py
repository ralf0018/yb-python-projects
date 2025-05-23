class Factorial:
    #Constructor to initialize the number
    def __init__(self, num):
        self.num = num
        self.result = 1
    
    #calculate and output the result
    #if the input is not valid, return "error", other wise calculate the result
    def cal(self):
        if self.num != int(self.num) or self.num<0:
            return "invalid input"
        elif self.num == 0 or self.num == 1:
            return 1
        else:
            for i in range(2,int(self.num)+1,1):
                self.result *=i
            return self.result
        
    # check if the input number is prime
    def isPrime(self):
        if self.num!=int(self.num) or self.num <=1:
            return False
        elif self.num == 2:
            return True
        else:
            for i in range(3,int(self.num**0.5+1)):
                if self.num % i == 0:
                    return False
            return True

number = float(input("please input a number: "))
f = Factorial(number)
print(f"the factorial result is {f.cal()}")
print(f"The number is prime: {f.isPrime()}")