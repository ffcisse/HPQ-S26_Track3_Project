def evaluate_retrieval(query, retrieved_context):
    if not retrieved_context or len(str(retrieved_context).strip()) < 50:
        return {
            "needs_retry": True,
            "reason": "Retrieved context is empty or too short."
        }

    query_terms = set(query.lower().split())
    context_terms = set(str(retrieved_context).lower().split())

    overlap = query_terms.intersection(context_terms)

    if len(overlap) < 2:
        return {
            "needs_retry": True,
            "reason": "Low relevance between query and retrieved context."
        }

    return {
        "needs_retry": False,
        "reason": "Context is relevant."
    }