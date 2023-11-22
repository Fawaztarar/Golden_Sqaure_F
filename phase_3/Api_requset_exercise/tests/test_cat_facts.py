from unittest.mock import Mock 
from lib.cat_facts import CatFacts
def test_mock_cat_facts ():
    requester_mock = Mock()
    response_mock = Mock ()
    requester_mock.get. return_value = response_mock
    response_mock. json. return_value = {"fact": "Cats have four legs"}

    assert response_mock.json() == {"fact": "Cats have four legs"}