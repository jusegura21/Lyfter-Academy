import pytest
from Week15.Excercise1 import homemade_bubble_sort

#Arrange
#Act
#Assert
def test_homemade_bubble_sort_w_short_list():
    #Arrange
    input_list=[5,3,4,2,1]
    #Act
    result=homemade_bubble_sort(input_list)
    #Assert
    assert result == sorted(input_list)

def test_homemade_bubble_sort_w_long_list():
    #Arrange
    import random
    counter=0
    input_list=[]
    #Act
    while counter<=100:
        input_list.append(random.randint(0,100))
        counter+=1
    result=homemade_bubble_sort(input_list)
    #assert
    assert result==sorted(input_list)

def test_homemade_bubble_sort_w_empy_list():
    #Arrange
    input_list=[]
    #Act
    result=homemade_bubble_sort(input_list)
    #Assert
    assert not result

def test_homemade_bubble_sort_w_wrong_inputs():
    #Arrange
    input1='random' 
    #Act&Assert   #works kith other data types like integers, list of dictionaries, floats, etc. 
    with pytest.raises(TypeError):
        homemade_bubble_sort(input1)
