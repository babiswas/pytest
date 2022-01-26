import pytest
from sample import A,B

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



@pytest.mark.subclass
def test_subclass():
    obj1=B(3,4)
    assert isinstance(obj1,A)

@pytest.mark.subclass
def test_subclass1():
    obj1=A(5,6)
    assert isinstance(obj1,B)==False

@pytest.mark.subclass
def test_subclass2():
    obj1=B(11,12)
    assert isinstance(obj1,B)==True

@pytest.mark.subclass
def test_subclass3():
   obj2=B(14,15)
   assert issubclass(B,A)==True

@pytest.mark.subclass
def test_subclass3():
   obj2=B(14,15)
   assert issubclass(A,B)==False







