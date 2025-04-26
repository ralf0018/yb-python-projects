class Factorial:
    #initialisation
    def __init__(self, num):
        self.num = num
        self.result = 1
    
    #calculate and output the result
    #if the input is not a integer, return "error", other wise calculate the result
    def cal(self):
       
        if self.num!=int(self.num) or self.num<0:
            return "error"
        elif self.num == 0 or self.num == 1:
            return 1
        else:
            for i in range(2,self.num+1,1):
                self.result *=i
            return self.result
        

f = Factorial(10)
print(f.cal())