from typing import List
from pydantic import BaseModel, validator, Field

class Company(BaseModel):
    company_id: int = Field(le=2) # Если пишем так, то def check_that_company_id_is_less_than_two
                                  # можно закомментить,
                                  # это встроенный метод валидации в Field
    company_name: str
    company_address: str
    company_status: str

class Meta(BaseModel):
    limit: int
    offset: int
    total: int

class ResponsePydantic(BaseModel):
    data: List[Company]
    meta: Meta

    # @validator('company_id')
    # def check_that_company_id_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError("Company_id is not less than two")
    #     else:
    #         return v