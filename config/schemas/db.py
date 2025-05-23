from pydantic import BaseModel

class DatabaseConfig(BaseModel):
    host: str
    port: int
    username: str
    password: str
    database: str