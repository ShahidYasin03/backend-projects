from pydantic import BaseModel, HttpUrl
from datetime import datetime


from datetime import datetime
from pydantic import BaseModel, HttpUrl


class URLCreate(BaseModel):
    long_url: HttpUrl


class URLResponse(BaseModel):
    short_code: str
    long_url: HttpUrl


class URLInfo(BaseModel):
    short_code: str
    long_url: HttpUrl
    click_count: int
    created_at: datetime