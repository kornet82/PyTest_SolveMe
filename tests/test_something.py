import requests
from configuration import SERVICE_URL
from src.enums.global_enums import GlobalErrorMessages
from jsonschema import validate
from src.schemas.post import POST_SCHEMA

def test_getting_posts():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()
    print(received_posts)
    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert len(received_posts) == 2, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value


# {'data': [{'company_id': 1, 'company_name': 'Tesla', 'company_address': 'Nicholastown, IL 80126', 'company_status': 'ACTIVE'},
# {'company_id': 2, 'company_name': 'Google', 'company_address': '1093 Cooke Harbor Apt. 908', 'company_status': 'ACTIVE'},
# {'company_id': 3, 'company_name': 'Toyota', 'company_address': 'Davidberg, MN 88952', 'company_status': 'ACTIVE'}],
# 'meta': {'limit': 3, 'offset': 0, 'total': 7}}



