from flask import Flask, request, jsonify
from .sanitization import sanitize_input, sanitize_output
from .similarity import jaccard_similarity, cosine_similarity
from .llm import query_llm

app = Flask(__name__)

@app.route('/api/similarity', methods=['POST'])
def similarity():
    # Sanitize input
    prompt1 = sanitize_input(request.json.get('prompt1', ''))
    prompt2 = sanitize_input(request.json.get('prompt2', ''))
    metric = request.json.get('metric', 'cosine')  # Default to cosine similarity

    # Calculate similarity
    if metric == 'jaccard':
        similarity_score = jaccard_similarity(prompt1, prompt2)
    else:
        similarity_score = cosine_similarity(prompt1, prompt2)

    # Define threshold for similarity to send to LLM
    similarity_threshold = 0.7
    llm_response = None

    if similarity_score > similarity_threshold:
        # Send one of the prompts to the LLM and sanitize the output
        raw_response = query_llm(prompt1)
        llm_response = sanitize_output(raw_response)

    # Return response
    return jsonify({
        "message": "Similarity calculated successfully!",
        "similarity_score": similarity_score,
        "metric_used": metric,
        "llm_response": llm_response
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)