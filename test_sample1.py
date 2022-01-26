import pytest
from sample import A

@pytest.mark.skip
def test_obj():
   obj=A(2,3)
   str1=str(obj)
   assert str1=="2 and 3"

def test_sum():
    obj1=A(3,4)
    obj2=A(5,6)
    assert obj1.a+obj2.a==8

def test_objsum():
   obj1=A(8,2)
   obj2=A(6,1)
   assert obj1+obj2==14

def test_subs():
    obj3=A(10,4)
    obj4=A(5,2)
    assert obj3-obj4==-5

def test_gtlt():
   obj1=A(10,2)
   obj2=A(5,1)
   val=obj2<obj1
   assert val==True




