import pytest

from ..Social_media.calculations import add, divide, BankAccount


@pytest.fixture
def zero_bank_account():
    print("creating empty bank account")
    return BankAccount()


@pytest.fixture
def bank_account():
    return BankAccount(50)


@pytest.mark.parametrize("n1, n2, expected", [
    (2,2, 4),
    (5,7,12),
    (9,8,17)
])
def test_add(n1, n2, expected):
    print('testing add function')
    result= add(n1,n2)
    assert result == expected
    
def test_divide():
    print("testing divide function")
    assert divide(4,2) ==2
    

def test_initial_amount():
    sky_account = BankAccount(50)
    assert sky_account.balance == 50
    
def test_withdraw():
    account = BankAccount(50)
    account.withdraw(20)
    assert account.balance == 30
    
def test_deposit():
    account = BankAccount(50)
    account.deposit(20)
    assert account.balance == 70
    
def test_interest():
    account = BankAccount(50)
    account.collect_interest()
    assert int(account.balance) == 55
    