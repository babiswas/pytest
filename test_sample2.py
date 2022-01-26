import pytest
from sample import A,B

@pytest.fixture
def value_init():
   obj1=A(2,3)
   obj2=A(10,5)
   return obj1,obj2

@pytest.fixture
def value_init1():
    obj1=A(3,4)
    obj2=B(12,5)
    return obj1,obj2

@pytest.mark.great
def test_add(value_init):
    obj1,obj2=value_init
    assert obj1+obj2==12

@pytest.mark.great
def test_sub(value_init):
    obj1,obj2=value_init
    assert obj1-obj2==8

def test_lt_F(value_init):
    obj1,obj2=value_init
    test=obj2<obj1
    assert test==False

def test_lt_T(value_init):
    obj1,obj2=value_init
    test=obj1<obj2
    assert test==True

def test_add1(value_init1):
    obj1,obj2=value_init1
    assert obj1+obj2==15
    