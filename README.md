# LLM Prompt Similarity Service

# API Documentation

### Endpoint: `/api/similarity` (POST)

**Description**: This endpoint calculates the similarity between two text prompts using a specified similarity metric. If the similarity score exceeds a given threshold, an additional response from the LLM (Language Model) may be provided.

- **URL**: `/api/similarity`
- **Method**: `POST`
- **Content-Type**: `application/json`

**Request Body**:

```json
{
  "prompt1": "<string>",
  "prompt2": "<string>",
  "metric": "<string>"  // Optional: "cosine" (default) or "jaccard"
}
```
- **prompt1**: The first text prompt to compare (required).
- **prompt2**: The second text prompt to compare (required).
- **metric-Type**: Similarity metric to use. Can be cosine (default) or jaccard (optional).

**Response**:
- **Status Code**: `200 OK`
- **Content-Type**: `application/json`

**Response Body**:
```json
{
  "message": "Similarity calculated successfully!",
  "similarity_score": <float>,
  "metric_used": "<string>",
  "llm_response": "<string>" // Optional: present only if similarity score exceeds threshold
}
```
- **similarity_score**: The calculated similarity score between the prompts.
- **metric_used**: The similarity metric used (e.g., cosine or jaccard).
- **llm_response**: A response genContent-Typeerated by the LLM if the similarity score exceeds a specified threshold.

**Error Responses**:
- **400 Bad Request**: One or more inputs were rejected due to validation.
```json
{
   "error": "One or more inputs were rejected. Please provide appropriate content."
}
```
   - **500 Internal Server Error**: An unexpected error occurred while processing the request.
```json
{
  "error": "An unexpected error occurred. Please try again later."
}
```
### Examples
**Request**:
```json
{
  "prompt1": "How are you?",
  "prompt2": "How are you doing?",
  "metric": "cosine"  // Optional: "cosine" (default) or "jaccard"
}
```
**Response**:
```json
{
   "message": "Similarity calculated successfully!",
   "similarity_score": 0.8660254037844388,
   "metric_used": "cosine",
   "llm_response": "This is a simulated response to the prompt."
}
```

## Directory Structure
- src: contains the main source code for the Flask service
- tests: contains unit tests for the API
- docs: any documentation for the project

## Setup

**Prerequisites**:
- Python 3.10+
- Docker (for containerized setup)

**Steps to set up the development environment**:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd ai_similarity_service
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
### Running the Service Locally:
1. Start the Flask service:
   ```python
   python -m src.api.app
   ```
2. Access the Service:
   - The API will be available at `http://127.0.0.1:5000/api/similarity`

### Running Tests:
1. Run the tests:
   ```
   python -m unittest discover tests
   ```
2. Load Testing with Locust:
   ```
   locust -f locustfile.py
   ```
   Access the Locust UI at `http://localhost:8089` to perform load testing.

## Docker Deployment

### Building the Docker Image
To build the Docker image, run:
```
docker build -t ai_similarity_service .
```

### Running the Docker Container
To run the Docker container, execute:
```
docker run -p 5000:5000 ai_similarity_service
```

The service will be accessible at `http://127.0.0.1:5000/api/similarity`.