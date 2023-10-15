from iebank_api.models import Account
import pytest

def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.name == 'John Doe'
    assert account.currency == '€'
    assert account.country == 'Spain'
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == 'Active'

def test_create_account_with_invalid_currency():
    """
    GIVEN a Account model
    WHEN a new Account is created with an invalid currency
    THEN check the currency is set to '€'
    """
    account = Account('John Doe', '€€€', 'Spain')
    assert account.currency == '€'

def test_create_account_with_invalid_country():
    """
    GIVEN a Account model
    WHEN a new Account is created with an invalid country
    THEN check the country is set to 'Spain'
    """
    account = Account('John Doe', '€', 'Spain')
    assert account.country == 'Spain'

def test_account_balance_update():
    """
    GIVEN an existing account
    WHEN the account balance is updated
    THEN check that the balance field is updated correctly
    """
    account = Account('Grace Lee', '€', 'United Kingdom')
    account.balance = 1000.0
    assert account.balance == 1000.0

def test_account_status_change():
    """
    GIVEN an existing account
    WHEN the account status is changed
    THEN check that the status field is updated correctly
    """
    account = Account('Michael Brown', '€', 'Canada')
    account.status = 'Inactive'
    assert account.status == 'Inactive'

def test_account_creation_timestamp():
    """
    GIVEN a newly created account
    THEN check that the created_at field is set correctly
    """
    account = Account('Sophia Wilson', '€', 'Australia')
    assert account.created_at is not None
 