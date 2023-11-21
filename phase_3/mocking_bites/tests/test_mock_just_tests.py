from unittest.mock import Mock

class FakeClassWithVerifiedMethods():
    def __init__(self):
        self.greet_has_been_called = False

    def greet(self, name):
        self.greet_has_been_called = True
        assert name == "Kay"
        return "Hello, Kay!"

    def test_object_with_verified_methods():
        fake_object = FakeClassWithVerifiedMethods()
        assert fake_object.greet("Kay") == "Hello, Kay!"
        assert fake_object.greet_has_been_called == True
    
    def test_mock_with_verified_methods ():
        fake_object = Mock()
        fake_object.greet.return_value = "Hello, Kay!"
        assert fake_object.greet ("Kay") == "Hello, Kay!" 
        fake_object.greet.assert_called () 
        fake_object.greet.assert_called_with ("Kay")