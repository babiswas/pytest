class CalculatorError(Exception):
    def __init__(self,str1):
        self.str1=str1
    def __str__(self):
        return self.str1

class Calculator:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def addition(self):
       try:
          return self.a+self.b
       except TypeError as e:
          raise CalculatorError("Add Error")

   def add_all(self,*args):
       try:
         sum=0
         for i in args:
           sum+=i
         return sum
       except Exception as e:
         raise CalculatorError("Add all error")
           

   def subs(self):
       try:
          return self.a-self.b
       except TypeError as e:
          raise CalculatorError("Subs Error")

   def divison(self):
       try:
          return self.a//self.b
       except TypeError as e:
          raise CalculatorError("Division Error")
       except ZeroDivision as e:
          raise CalculatorError("Division Error")

   def add(self):
      return self.a+self.b

if __name__=="__main__":
   c=Calculator(2,"hello")
   print(c.addition())
   print(c.add())
   
