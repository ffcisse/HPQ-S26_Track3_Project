from services.retrieval_client import call_retrieval
from services.reflection_client import check_retrieval_quality
from agent.query_refiner import refine_query
from agent.answer_generator import generate_answer
from services.retrieval_client import call_retrieval


def run_agent_pipeline(user_query: str, session_id=None):
    # Keep track of all retrieval attempts (for debugging / frontend display)
    retrieval_steps = []
    # Step 1: Initial retrieval
    # Send the user query to the retrieval system
    initial = call_retrieval(user_query, top_k=5)
    
    # Log what we retrieved for this query
    retrieval_steps.append({
        "query": user_query,
        "results": initial["retrieved_chunks"]
    })
    # Step 2: Ask evaluation module if retrieval was good enough
    # We will call Madhu’s logic
    print("Using evaluator from:", check_retrieval_quality.__module__)
    quality_feedback = check_retrieval_quality(
        user_query=user_query,
        retrieved_chunks=initial["retrieved_chunks"]
    )
    print("QUALITY FEEDBACK:", quality_feedback)
    print("FUNCTION FILE:", check_retrieval_quality.__code__.co_filename)
    #Step 3: Adaptive retrieval (only if needed)
    if quality_feedback["needs_retry"]:
        
        # If retrieval was weak, rewrite the query to improve it
        refined_query = refine_query(
            user_query=user_query,
            retrieved_chunks=initial["retrieved_chunks"],
            feedback=quality_feedback
        )
        # Call retrieval again with the improved query
        refined = call_retrieval(refined_query, top_k=5)
        # Log this second retrieval step
        retrieval_steps.append({
            "query": refined_query,
            "results": refined["retrieved_chunks"]
        })

        final_chunks = refined["retrieved_chunks"]
        used_adaptive_retrieval = True
    else:
        # If initial retrieval was good, just use it
        final_chunks = initial["retrieved_chunks"]
        used_adaptive_retrieval = False
    # Step 4: Generate final answer
    # Pass the query + retrieved chunks to the answer generator
    answer_package = generate_answer(user_query, final_chunks)
    # Step 5: Format final response
    return {
        "answer": answer_package["answer"],
        "sources": answer_package["sources"],
        "reasoning": answer_package["reasoning"],
        "reflection": None, # placeholder (will come from memory/eval later)
        "limitations": None,  # placeholder
        "evaluation": quality_feedback,
        "used_adaptive_retrieval": used_adaptive_retrieval,
        "retrieval_steps": retrieval_steps # helpful for debugging + frontend display
    }