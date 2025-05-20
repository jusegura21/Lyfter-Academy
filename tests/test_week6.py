import pytest
from Semana6.Ejercicio3 import sumatoria_de_lista
from Semana6.Ejercicio4 import text_inverter
from Semana6.Ejercicio5 import upper_and_lower_cases
from Semana6.Ejercicio6 import sorteador
from Semana6.Ejercicio6 import create_list
from Semana6.Ejercicio7 import numero_primo
 

#Sumatoria de lista
def test_sumatoria_de_lista_w_short_list():
    short_list=[1,2,3,4]
    result=sumatoria_de_lista(short_list)
    assert result==10

def test_sumatoria_de_lista_w_long_list():
    counter=0
    input_list=[]
    #Act
    while counter<=100:
        input_list.append(counter)
        counter+=1
    result=sumatoria_de_lista(input_list)
    #assert
    assert result==sum(input_list)

def test_sumatoria_de_lista_w_floats():
    #Arrange
    input1=[0.5,0.7,0.8]#works kith other data types like integers, list of dictionaries, floats, etc.
    #Act
    result=sumatoria_de_lista(input1)
    #Assert
    assert result==2.0

#text_inverter
def test_text_inverter_w_lowcase():
    input='sopa de pollo con arroz y vegetales'
    result=text_inverter(input)
    assert result=='selategev y zorra noc ollop ed apos'

def test_text_inverter_w_uppercase():
    input='HOLA MUNDO'
    result=text_inverter(input)
    assert result=='ODNUM ALOH'

def test_text_inverter_w_mix_upper_lower_case():
    input='Hola Mundo'
    result=text_inverter(input)
    assert result == 'odnuM aloH'

#upper_and_lower_cases
def test_upper_and_lower_cases_w_numbers():
    input='2224'
    result1=upper_and_lower_cases(input)
    assert result1[0] == 0

def test_upper_and_lower_cases_with_spaces():
    input='hello world'
    result=upper_and_lower_cases(input)[1]
    assert result == 10 #hello world contains 10 lower cases without counting the space
    
def test_upper_and_lower_cases_with_upper_and_lower():
    input='Hello World'
    result1=upper_and_lower_cases(input)[1]
    result2=upper_and_lower_cases(input)[0]
    assert (result1 == 8) and (result2==2) 

#create_list
def test_create_list_with_spaces():
    input='item1-item2 - item3 '
    result=create_list(input)
    assert result == ['item1','item2 ',' item3 ']

def test_create_list_with_empy_items():
    input='item1--item3'
    result=create_list(input)
    assert result == ['item1','','item3']

def test_create_list_with_wrong_input():
    input=123
    with pytest.raises(TypeError):
        create_list(input)

#sorteador
def test_sorteador_with_words_list():
    input= ['zapayo','ayote','manzana']
    result=sorteador(input)[0]
    assert result == ['ayote', 'manzana', 'zapayo']

def test_sorteador_with_empy_index():
    input= ['zapayo','','manzana']
    with pytest.raises(IndexError):
        sorteador(['', 'manzana', 'zapayo'])

def test_sorteador_with_numbers():
    input=['string',2,'other']
    with pytest.raises(TypeError):
        sorteador(input)

#Numero_primo
def test_numero_primo_with_prime_number():
    input=7
    result=numero_primo(7)
    assert result 
    
def test_numero_primo_with_none_prime_number():
    input=7
    result=numero_primo(10)
    assert not result 

def test_numero_primo_with_text():
    input='sdad'
    with pytest.raises(TypeError):
        numero_primo(input)

