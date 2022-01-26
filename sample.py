class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b

  def __str__(self):
     return f"{self.a} and {self.b}"

  def __add__(self,other):
      if isinstance(other,A):
         return other.a+self.a

  def __sub__(self,other):
      if isinstance(other,A):
         return other.a-self.a

  def __lt__(self,other):
      if isinstance(other,A):
         return self.a<other.a

class B(A):
   def __init__(self,a,b):
      super().__init__(a,b)

   def isequal(self,other):
       if isinstance(other,A):
          if other.a==self.a and other.b==self.b:
             return True
          else:
             return False



if __name__=="__main__":
   a1=A(3,4)
   a2=A(10,13)
   print(a1-a2)
   print(a1>a2)


   