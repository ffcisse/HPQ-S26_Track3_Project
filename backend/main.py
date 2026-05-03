from fastapi import FastAPI
from schemas.models import QueryRequest

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Backend is running"}

@app.post("/ask")
def ask_agent(request: QueryRequest):
    return {
        "answer": f"Received query: {request.user_query}",
        "sources": [],
        "reasoning": "Stub response",
        "reflection": None
    }
