import pytest
from OOP import Categories
from OOP import Transactions

def test_try_add_category_success():
    c=Categories('dummy.txt',[])
    result=c.try_add_category('food')
    assert result is True
    assert 'food' in c.categories 

def test_empty_string_is_not_added():
    c = Categories('dummy.txt', [])
    result = c.try_add_category('   ')  # solo espacios
    assert result is False
    assert c.categories == []

def test_duplicate_is_not_added():
    c = Categories('dummy.txt', ['Alimento'])
    result = c.try_add_category('Alimento')
    assert result is False
    assert c.categories == ['Alimento']

def test_write_category_list(tmp_path):
    # Arrange
    path = tmp_path / "categories.txt"
    lista = ['Food', 'Transport', 'Entertainment']
    c = Categories(str(path), lista)

    # Act
    result = c.write_category_list()

    # Assert
    assert result is True
    assert path.exists()

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Verifica que las líneas coincidan con lo que se escribió
    assert lines == ['Food\n', 'Transport\n', 'Entertainment\n']

def test_read_categories(tmp_path):
    path= tmp_path / 'categories.txt'
    lista=['Food', 'Transport', 'Entertainment']
    c=Categories(str(path),lista)
    c.write_category_list()
    c.categories=[]
    result = c.read_list_from_file()
    assert result == ['Food', 'Transport', 'Entertainment']
    assert c.categories == ['Food','Transport','Entertainment']

def test_valid_transaction_data():
    t=Transactions('Income')
    desc,amount=t.set_transaction_data(' Business ','500')

    assert desc == 'Business'
    assert amount==500.0

def test_empy_description_in_set_transaction_data():
    #arrange
    t=Transactions('Income')
    with pytest.raises(ValueError,match='Description cannot be empty'):
        t.set_transaction_data('  ','100')

def test_invalid_amount_format_in_set_transaction_data():
    #arrange
    t=Transactions('Expense')
    with pytest.raises(ValueError,match='Invalid amount format'):
        t.set_transaction_data('Car','abc')

@pytest.mark.parametrize('amount',['0','-100'])       
def test_amount_zero_or_negative_in_set_transaction_data(amount):
    t=Transactions('Expense')
    with pytest.raises(ValueError,match='Amount must be greater than 0'):
        t.set_transaction_data('Taxi',amount)
