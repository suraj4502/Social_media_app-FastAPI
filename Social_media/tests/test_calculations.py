import pytest

from ..calculations import add, divide, BankAccount, InsufficientFunds


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
    
@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)

])
def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance == expected


def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)
    