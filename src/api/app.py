from flask import Flask, request, jsonify
from .sanitization import sanitize_input

app = Flask(__name__)

@app.route('/api/similarity', methods=['POST'])
def similarity():
    prompt1 = sanitize_input(request.json.get('prompt1', ''))
    prompt2 = sanitize_input(request.json.get('prompt2', ''))
    # Placeholder for similarity check logic
    return jsonify({"message": "Sanitized prompts received!", "prompt1": prompt1, "prompt2": prompt2})

if __name__ == '__main__':
    app.run(debug=True)