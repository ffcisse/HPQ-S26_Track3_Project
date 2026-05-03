def generate_answer(user_query: str, retrieved_chunks: list):
    # Combine all the retrieved chunk text into one string
    # This acts as the "context" we’ll base the answer on
    context = " ".join(chunk["chunk_text"] for chunk in retrieved_chunks)
    
    return {
        # For now, just returning the context as the answer
        # Later this will be replaced with an LLM-generated response
        "answer": f"Based on the retrieved context: {context}",
        # Pull out source info from each chunk so we can trace where the answer came from
        "sources": [
            {
                "source_title": chunk["source_title"],
                "page_number": chunk["page_number"],
                "chunk_id": chunk["chunk_id"]
            }
            for chunk in retrieved_chunks
        ],
        # Simple explanation of how the answer was formed
        # (this will get more detailed once we add real reasoning)
        "reasoning": "The answer was generated using the retrieved chunks."
    }