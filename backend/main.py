from fastapi import FastAPI
from schemas.models import QueryRequest
from agent.pipeline import run_agent_pipeline

app = FastAPI()

# Define a POST endpoint at "/ask"
# This is where the frontend will send user queries
@app.post("/ask")
def ask_agent(request: QueryRequest):
    # Take the incoming request, extract the query + session_id,
    # and pass it into the agent pipeline
    return run_agent_pipeline(
        user_query=request.user_query,
        session_id=request.session_id
    )

