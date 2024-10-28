# Questions API Documentation

This API provides endpoints for retrieving and randomizing questions from various categories.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API:
```bash
python questions_api.py
```

The server will start on http://localhost:8000

## API Endpoints

### 1. Get Questions
```
GET /api/v1/questions/{category}
```

Retrieves questions from a specific category.

Parameters:
- `category` (path): Category of questions (astronomy, literature, or mathematics)
- `limit` (query, optional): Maximum number of questions to return (1-50, default: 10)
- `random` (query, optional): Whether to return random questions (default: true)

Example:
```bash
curl http://localhost:8000/api/v1/questions/astronomy?limit=5&random=true
```

Response:
```json
[
  {
    "id": "ASTRO_001",
    "question": "What is the closest star to Earth besides the Sun?",
    "correct_answer": "Proxima Centauri",
    "options": [
      "Proxima Centauri",
      "Alpha Centauri A",
      "Barnard's Star",
      "Sirius"
    ]
  }
]
```

### 2. Randomize Questions
```
GET /api/v1/questions/{category}/random
```

Gets randomly selected and ordered questions from a specific category.

Parameters:
- `category` (path): Category of questions (astronomy, literature, or mathematics)
- `count` (query, optional): Number of questions to randomly select (1-20, default: 5)
- `seed` (query, optional): Random seed for reproducible randomization

Example:
```bash
curl http://localhost:8000/api/v1/questions/mathematics/random?count=10&seed=42
```

Response:
```json
[
  {
    "id": "MATH_015",
    "question": "What is the square root of 144?",
    "correct_answer": "12",
    "options": [
      "10",
      "12",
      "14",
      "16"
    ]
  }
]
```

### 3. Health Check
```
GET /api/v1/health
```

Verifies API is running properly and shows paths to question files.

Example:
```bash
curl http://localhost:8000/api/v1/health
```

Response:
```json
{
  "status": "healthy",
  "question_files": {
    "astronomy": "/path/to/Refined_Astronomy_Questions.csv",
    "literature": "/path/to/Refined_Literature_Questions.csv",
    "mathematics": "/path/to/Refined_Mathematics_Questions.csv"
  }
}
```

## Error Handling

The API returns appropriate HTTP status codes:

- 200: Success
- 400: Bad Request (invalid parameters)
- 404: Category or resource not found
- 500: Internal Server Error

Error response format:
```json
{
  "detail": "Error message"
}
```

## Development

### API Documentation
Access the interactive API documentation at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Data Source
Questions are loaded from CSV files in the `external-resources/questions` directory:
- Refined_Astronomy_Questions.csv
- Refined_Literature_Questions.csv
- Refined_Mathematics_Questions.csv

### Features
- Input validation using Pydantic models
- Automatic API documentation with OpenAPI
- Caching of question data for improved performance
- Support for reproducible randomization with seed parameter
- Health check endpoint for monitoring
- Proper error handling with detailed messages
- Automatic path resolution for question files

### CSV File Format
Required columns:
- id: Unique identifier for the question
- question: The question text
- correct_answer: The correct answer
- options: Optional column for multiple choice options (stored as string representation of list)

## Implementation Notes

The backend implementation follows these key principles:

1. **Data Validation**: Uses Pydantic models to ensure data integrity
2. **Error Handling**: Provides detailed error messages for troubleshooting
3. **Caching**: Implements in-memory caching of CSV data for better performance
4. **Path Resolution**: Automatically resolves paths relative to the project root
5. **Type Safety**: Implements proper type hints and enum validation
6. **Documentation**: Provides comprehensive API documentation via OpenAPI

The implementation fully supports both JSON schemas:
- `get-questions.json`: Implemented in the GET /api/v1/questions/{category} endpoint
- `randomize.json`: Implemented in the GET /api/v1/questions/{category}/random endpoint
