import json
from app import app
# user pytest

app.print_hello()

def test_get():
    assert 1==1 

def test_create():
    assert 3>2
    
def test_update():
    assert 'string' == 'string'
