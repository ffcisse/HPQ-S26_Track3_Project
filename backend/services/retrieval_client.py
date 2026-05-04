def call_retrieval(query: str, top_k: int = 5):
    # This function is supposed to call the retrieval system (Thomas’s part)
    # It should take a query and return the top_k most relevant document chunks

    # Right now, this is just a mock function so the backend can run end-to-end
    # It always returns the same fake chunk regardless of the query
    return {
        "retrieved_chunks": [
            {
                "chunk_id": "mock_chunk_001",
                "chunk_text": "Retrieval-augmented generation uses external documents to help a language model produce more grounded and factual answers.",
                "source_title": "Mock Research Paper",
                "page_number": 1,
                "similarity_score": 0.82
            }
        ]
    }
def check_retrieval_quality(user_query: str, retrieved_chunks: list):
    if not retrieved_chunks:
        return {
            "needs_retry": True,
            "quality_score": 0,
            "issues": ["No retrieved chunks"],
            "reason": "No retrieved chunks were returned."
        }

    combined_context = " ".join(
        str(chunk.get("chunk_text", chunk.get("text", chunk))) if isinstance(chunk, dict) else str(chunk)
        for chunk in retrieved_chunks
    )

    query_terms = set(user_query.lower().split())
    context_terms = set(combined_context.lower().split())
    overlap = query_terms.intersection(context_terms)

    if len(overlap) < 2:
        return {
            "needs_retry": True,
            "quality_score": 0.5,
            "issues": ["Low relevance"],
            "reason": "Retrieved chunks appear weakly related to the user query."
        }

    return {
        "needs_retry": False,
        "quality_score": 0.8,
        "issues": [],
        "reason": "Retrieved chunks appear relevant enough to answer the query."
    }