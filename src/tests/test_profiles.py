import unittest
from src import create_app, db
from src.models.Profile import Profile
from src.models.User import User

class TestProfiles(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.app = create_app()
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()
        db.create_all()
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])

    @classmethod
    def tearDown(cls):
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()




    def test_profiles_index(self):
        response= self.client.get("/api/profile/all")

        data = response.get_json()

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)

    def test_profile_create(self):
        response = self.client.post("api/register",                   
        json = {                                                        
            "email": "test11@test.com",
            "password": "123456"
        })
        response = self.client.post("api/login",                      
        json = {              
            "email": "test11@test.com",
            "password": "123456"
        })                    
        data = response.get_json()                                      
        headers_data= {                                                 
            'Authorization': f"Bearer {data['token']}"
        }
        

        data = {                                                       
            "username" : "test_username", 
            "fname" : "test", 
            "lname" : "test",
            "account_active": "True",
            "contractor": "True",
            "employer": "False"
        }
        response = self.client.post("/api/profile/",                       
        json = data,                                                    
        headers = headers_data)                                         
        self.assertEqual(response.status_code, 200)                     
        data = response.get_json()                                      
        profile = Profile.query.get(data["user"]["id"])                                                   
        self.assertEqual(profile.username, "test_username") 

