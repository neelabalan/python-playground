import json
import os
import pytest

from app import user 


@pytest.fixture
def client():
    user.app.config['TESTING'] = True
    with user.app.test_client() as client:
        # with user.app.app_context():
        #     flaskr.init_db()
        yield client

def test_empty_db(client):
    rv = client.get('/users')
    assert b'' in rv.data

def test_post(client):
    rv = client.post(
        '/users/1', 
        data=dict(
            name='john',
            email='john@doe.com'
        ), 
        follow_redirects=True
    )
    assert rv.status_code == 200

# def test_get():
#     assert 1==1 

# def test_create():
#     assert 3>2
    
# def test_update():
#     assert 'string' == 'string'
