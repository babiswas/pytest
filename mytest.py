def my_key_val(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():
       print(key,value)

def my_key(*args):
   print(args)
   for key in args:
      print(key)

if __name__=="__main__":
   my_key_val(**{"hello":12,"bello":24})
   my_key(*["hello","bello"])