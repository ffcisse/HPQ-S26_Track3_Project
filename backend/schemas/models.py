from pydantic import BaseModel
from typing import Optional
# This defines the structure of the request coming from the frontend
# FastAPI uses this to automatically parse and validate incoming JSON

class QueryRequest(BaseModel):
    # The main question from the user (required)
    user_query: str
    # Optional session ID (useful later for tracking conversations/memory)
    session_id: Optional[str] = None

