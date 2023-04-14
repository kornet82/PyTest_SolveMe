POST_SCHEMA = {
    "type": "object",
    "properties": {
        "data": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "company_id": {"type": "integer"},
                    "company_name": {"type": "string"},
                    "company_address": {"type": "string"},
                    "company_status": {"type": "string"}
                },
                "required": ["company_id", "company_name", "company_address", "company_status"]
            }
        },
        "meta": {
            "type": "object",
            "properties": {
                "limit": {"type": "integer"},
                "offset": {"type": "integer"},
                "total": {"type": "integer"}
            },
            "required": ["limit", "offset", "total"]
        }
    },
    "required": ["data", "meta"]
}



# {'data': [{'company_id': 1, 'company_name': 'Tesla', 'company_address': 'Nicholastown, IL 80126', 'company_status': 'ACTIVE'},
# {'company_id': 2, 'company_name': 'Google', 'company_address': '1093 Cooke Harbor Apt. 908', 'company_status': 'ACTIVE'},
# {'company_id': 3, 'company_name': 'Toyota', 'company_address': 'Davidberg, MN 88952', 'company_status': 'ACTIVE'}],
# 'meta': {'limit': 3, 'offset': 0, 'total': 7}}