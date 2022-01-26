class CalculatorError(Exception):
    def __str__(self):
        return "CalculatorError"

class Calculator:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def addition(self):
       try:
          return self.a+self.b
       except TypeError as e:
          raise CalculatorError

   def add_all(self,*args):
       try:
         sum=0
         for i in args:
           sum+=i
         return sum
       except Exception as e:
         raise CalculatorError
           

   def subs(self):
       try:
          return self.a-self.b
       except TypeError as e:
          raise CalculatorError

   def divison(self):
       try:
          return self.a//self.b
       except TypeError as e:
          raise CalculatorError

   def add(self):
      return self.a+self.b

if __name__=="__main__":
   c=Calculator(2,"hello")
   print(c.addition())
   print(c.add())
   
