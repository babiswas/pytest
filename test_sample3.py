import pytest
from sample import A

@pytest.mark.parametrize("obj1,obj2,sum",[((1,2),(3,4),4),((5,2),(6,4),11),((5,7),(6,4),11)])
def test_sum(obj1,obj2,sum):
    a1=A(obj1[0],obj1[1])
    b1=A(obj2[0],obj2[1])
    assert a1+b1==sum


@pytest.mark.parametrize("obj1,obj2,diff",[((1,2),(3,4),2),((5,2),(6,4),1),((8,7),(6,4),-2)])
def test_subs(obj1,obj2,diff):
    a1=A(obj1[0],obj1[1])
    b1=A(obj2[0],obj2[1])
    assert a1-b1==diff

@pytest.mark.parametrize("obj1,obj2,verdict",[((1,2),(3,4),True),((5,2),(6,4),True),((8,7),(6,4),False)])
def test_subs(obj1,obj2,verdict):
    a1=A(obj1[0],obj1[1])
    b1=A(obj2[0],obj2[1])
    test=a1<b1
    assert test==verdict

@pytest.mark.skip
@pytest.mark.parametrize("obj1,str1",[((1,2),"1 and 2"),((5,2),"5 and 2"),((8,7),"8 and 7")])
def test_subs(obj1,str1):
    a1=A(obj1[0],obj1[1])
    assert str(a1)==str1
    
    