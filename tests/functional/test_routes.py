from iebank_api import app
import pytest

def test_get_accounts(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is requested (GET)
    THEN check the response is valid
    """
    response = testing_client.get('/accounts')
    assert response.status_code == 200

def test_dummy_wrong_path():
    """
    GIVEN a Flask application
    WHEN the '/wrong_path' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_create_account(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/accounts' page is posted to (POST)
    THEN check the response is valid
    """
    response = testing_client.post('/accounts', json={'name': 'John Doe', 'currency': '€', 'country': 'Spain'})
    assert response.status_code == 200

def test_get_single_account(testing_client):
    """
    GIVEN a Flask application
    WHEN a specific account ID is requested (GET)
    THEN check that the response contains the correct account information
    """
    # Create a test account first
    response_create = testing_client.post('/accounts', json={'name': 'Alice Smith', 'currency': '€', 'country': 'Germany'})
    assert response_create.status_code == 200
    account_id = response_create.json['id']

    # Now, request the specific account by ID
    response_get = testing_client.get(f'/accounts/{account_id}')
    assert response_get.status_code == 200

    # Check if the response contains the correct account information
    assert response_get.json['name'] == 'Alice Smith'
    assert response_get.json['currency'] == '€'
    assert response_get.json['country'] == 'Germany'

def test_update_account(testing_client):
    """
    GIVEN a Flask application
    WHEN a specific account ID is updated (PUT)
    THEN check that the account details have been updated correctly in the response
    """
    # Create a test account first
    response_create = testing_client.post('/accounts', json={'name': 'Bob Johnson', 'currency': '€', 'country': 'France'})
    assert response_create.status_code == 200
    account_id = response_create.json['id']

    # Update the account details
    response_update = testing_client.put(f'/accounts/{account_id}', json={'name': 'Bob Johnson Jr.'})
    assert response_update.status_code == 200

    # Request the updated account by ID
    response_get = testing_client.get(f'/accounts/{account_id}')
    assert response_get.status_code == 200

    # Check if the account details have been updated correctly
    assert response_get.json['name'] == 'Bob Johnson Jr.'

def test_delete_account(testing_client):
    """
    GIVEN a Flask application
    WHEN a specific account ID is deleted (DELETE)
    THEN check that the response indicates the account has been deleted
    """
    # Create a test account first
    response_create = testing_client.post('/accounts', json={'name': 'Eve Brown', 'currency': '€', 'country': 'Italy'})
    assert response_create.status_code == 200
    account_id = response_create.json['id']

    # Delete the account
    response_delete = testing_client.delete(f'/accounts/{account_id}')
    assert response_delete.status_code == 200

    # Try to retrieve the deleted account by ID
    response_get = testing_client.get(f'/accounts/0')
    assert response_get.status_code == 404  # Account should not exist anymore






