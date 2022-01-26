from calculator import Calculator,CalculatorError
import pytest

@pytest.fixture
def my_input():
   return [Calculator(3,4),Calculator(5,6),Calculator(8,9)]

def test_addition(my_input):
    objectlist=my_input
    val1=objectlist[0].addition()
    val2=objectlist[1].addition()
    val3=objectlist[2].addition()
    assert val1==7 and val2==11 and val3==17

def test_substraction(my_input):
    objectlist=my_input
    val1=objectlist[0].subs()
    val2=objectlist[1].subs()
    val3=objectlist[2].subs()
    assert val1==-1 and val2==-1 and val3==-1

def test_divison(my_input):
    objectlist=my_input
    val1=objectlist[0].divison()
    val2=objectlist[0].divison()
    val3=objectlist[0].divison()
    assert val1==0 and val2==0 and val3==0


@pytest.mark.hello
def test_add_exception():
    calc=Calculator(1,"a")
    with pytest.raises(CalculatorError) as context:
       result=calc.addition()
    assert str(context.value)=="Add Error"

@pytest.mark.hello
def test_subs_exception():
    calc1=Calculator(2,"b")
    with pytest.raises(CalculatorError) as context:
        result=calc1.subs()
    assert str(context.value)=="Subs Error"

@pytest.mark.hello
def test_div_exception():
    calc2=Calculator(3,"c")
    with pytest.raises(CalculatorError) as context:
         result=calc2.divison()
    assert str(context.value)=="Division Error"

def test_add_all():
    calc=Calculator(1,2)
    sum=calc.add_all(1,2,3,4,5)
    assert sum==15

def test_add_all_exception():
    calc=Calculator(3,4)
    with pytest.raises(CalculatorError) as context:
         result=calc.add_all(1,2,3,4,"hello","bello")
    assert str(context.value)=="Add all error"