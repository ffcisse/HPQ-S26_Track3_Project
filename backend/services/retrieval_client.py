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
