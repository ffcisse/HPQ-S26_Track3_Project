from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    user_query: str
    session_id: Optional[str] = None
