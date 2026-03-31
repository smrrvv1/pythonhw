from datetime import datetime
from pydantic import BaseModel, ConfigDict

class UserSchema(BaseModel):
    id: int
    name: str
    age: int
    gender: str = "female"
    created_at: datetime | None = None
