# LLM Prompt Similarity Service

## Directory Structure
- src: contains the main source code for the Flask service
- tests: contains unit tests for the API
- docs: any documentation for the project

## Setup
1. Create a virtual environment and activate it:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Flask service:
   ```
   python -m src.api.app
   ```

4. Run the tests:
   ```
   python -m unittest discover tests
   ```

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