from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/similarity', methods=['POST'])
def similarity():
    # Placeholder for input handling
    return jsonify({"message": "Endpoint is live!"})

if __name__ == '__main__':
    app.run(debug=True)
