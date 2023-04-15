from typing import List
from pydantic import BaseModel, validator

class Company(BaseModel):
    company_id: int
    company_name: str
    company_address: str
    company_status: str

class Meta(BaseModel):
    limit: int
    offset: int
    total: int

class Response(BaseModel):
    data: List[Company]
    meta: Meta

    @validator('id')
    def check_that_company_id_is_less_than_two(cls, v):
        if v > 2:
            raise ValueError("Company_id is not less than two")
        else:
            return v