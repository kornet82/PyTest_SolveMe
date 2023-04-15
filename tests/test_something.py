import requests
from configuration import SERVICE_URL

from src.base_classes.response import Response
from jsonschema import validate
# from src.schemas.post import POST_SCHEMA
from src.pydantic_schemas.post import ResponsePydantic


def test_getting_posts():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(ResponsePydantic)


# {'data': [{'company_id': 1, 'company_name': 'Tesla', 'company_address': 'Nicholastown, IL 80126', 'company_status': 'ACTIVE'},
# {'company_id': 2, 'company_name': 'Google', 'company_address': '1093 Cooke Harbor Apt. 908', 'company_status': 'ACTIVE'},
# {'company_id': 3, 'company_name': 'Toyota', 'company_address': 'Davidberg, MN 88952', 'company_status': 'ACTIVE'}],
# 'meta': {'limit': 3, 'offset': 0, 'total': 7}}



