def check_retrieval_quality(user_query: str, retrieved_chunks: list):
    if not retrieved_chunks:
        return {
            "needs_retry": True,
            "quality_score": 0.0,
            "issues": ["No retrieved chunks"],
            "reason": "No retrieved chunks were returned."
        }

    combined_context = " ".join(
        str(chunk.get("chunk_text", chunk.get("text", chunk)))
        if isinstance(chunk, dict)
        else str(chunk)
        for chunk in retrieved_chunks
    )

    if len(combined_context.strip()) < 100:
        return {
            "needs_retry": True,
            "quality_score": 0.3,
            "issues": ["Retrieved context too short"],
            "reason": "Retrieved context is too short to answer the query confidently."
        }

    query_terms = set(user_query.lower().split())
    context_terms = set(combined_context.lower().split())
    overlap = query_terms.intersection(context_terms)

    if len(overlap) < 2:
        return {
            "needs_retry": True,
            "quality_score": 0.5,
            "issues": ["Low query-context relevance"],
            "reason": "Retrieved chunks appear weakly related to the user query."
        }

    return {
        "needs_retry": False,
        "quality_score": 0.8,
        "issues": [],
        "reason": "Retrieved chunks appear relevant enough to answer the query."
    }
