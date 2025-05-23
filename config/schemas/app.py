from pydantic import BaseModel
from .auth import Credentials

class AppConfig(BaseModel):
    base_url: str
    browser: str
    credentials: Credentials
    headless: bool