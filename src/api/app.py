from flask import Flask, request, jsonify, abort
from .sanitization import sanitize_input, sanitize_output
from .similarity import jaccard_similarity, cosine_similarity
from .llm import query_llm

app = Flask(__name__)

SIMILARITY_THRESHOLD = 0.7

@app.route('/api/similarity', methods=['POST'])
def similarity():
        if not request.is_json:
            raise ValueError("Request content must be JSON")
        
        data = request.get_json()
        if not data:
            abort(400, description="No input data provided")

        prompt1 = data.get('prompt1')
        prompt2 = data.get('prompt2')
        metric = request.json.get('metric', 'cosine')  # Default to cosine similarity

        if not prompt1 or not prompt2:
            abort(400, description="Both 'prompt1' and 'prompt2' are required")

        if metric not in ['cosine', 'jaccard']:
            abort(400, description="Invalid metric specified. Choose 'cosine' or 'jaccard'.")

        try:
            # Sanitize input
            prompt1_sanitized = sanitize_input(prompt1)
            prompt2_sanitized = sanitize_input(prompt2)

            # Calculate similarity
            if metric == 'jaccard':
                similarity_score = jaccard_similarity(prompt1_sanitized, prompt2_sanitized)
            else:
                similarity_score = cosine_similarity(prompt1_sanitized, prompt2_sanitized)

            # Define threshold for similarity to send to LLM
            llm_response = None

            if similarity_score > SIMILARITY_THRESHOLD:
                # Send one of the prompts to the LLM and sanitize the output
                raw_response = query_llm(prompt1)
                llm_response = sanitize_output(raw_response) if raw_response else None

            # Return response
            return jsonify({
                "message": "Similarity calculated successfully!",
                "similarity_score": similarity_score,
                "metric_used": metric,
                "llm_response": llm_response
            })

        except ValueError as e:
            abort(400, description=str(e))
        except Exception as e:
            app.logger.error(f"An unexpected error occurred: {str(e)}")
            abort(500)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


# Error Handlers
@app.errorhandler(400)
def bad_request(error):
    response = jsonify({'error': 'Bad Request', 'message': error.description})
    response.status_code = 400
    return response

@app.errorhandler(404)
def not_found(error):
    response = jsonify({'error': 'Not Found', 'message': 'Resource not found'})
    response.status_code = 404
    return response

@app.errorhandler(500)
def internal_error(error):
    # Log the error internally
    app.logger.error(f"Internal Server Error: {str(error)}")
    response = jsonify({'error': 'Internal Server Error', 'message': 'An unexpected error occurred'})
    response.status_code = 500
    return response