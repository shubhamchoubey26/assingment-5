from ast import literal_eval
class Power:
    def __init__(self, x, n ):
        self.x = x
        self.n = n
        
    def power_number(self):
        if isinstance(self.x, (int,float)):        # check whether x object belong to int, float class    
            if isinstance(self.n, (int, float)):   # check whether x object belong to int, float class 
                if self.x == 0:
                    if self.n <=0:
                        return ("Math Domin Error ")   # checking its belong to maths domin or not
                    else:
                        return 0                      
                elif self.n == 0:                   #  checking whether power is 0 or not  
                    return 1
                elif self.n < 0:                    # checking whether power is inverse or not       
                    self.n = abs(self.n)
                    x = 1/(self.x**self.n)
                    return x
                else:
                    res = self.x**self.n
                    return res
            else: 
                return ("Not a valid number")      
        else: 
            return ("Not a valid number")
    
x = literal_eval(input("Enter base number (x) :- "))     # using literal_eval with input to take input from user
n = literal_eval(input("Enter power number (n) :- "))
obj1 = Power(x,n)
result = obj1.power_number()
print("The Expected output = {}".format(result))