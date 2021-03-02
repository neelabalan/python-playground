import json

# user pytest
class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        pass 

    def test_create(self):
        pass
        
    def test_update(self):
        pass 
