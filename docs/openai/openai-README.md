# OpenAI Schema API Documentation

To interact with the given schema using `curl`, let’s assume you’re working with a JSON schema that represents questions with an ID, question text, correct answer, and multiple options. Here’s a breakdown of potential `curl` commands to:

1. **Get all questions**
2. **Add a new question**
3. **Get a question by ID**
4. **Update a question**
5. **Delete a question**

I'll first outline example endpoints based on a RESTful approach, assuming FastAPI handles the backend with endpoints for managing questions.

## Schema Example

Assume the JSON schema structure for each question is:

```json
{
  "id": "1",
  "question": "What is the capital of France?",
  "correct_answer": "Paris",
  "options": [
    "Berlin",
    "Paris",
    "Rome",
    "Madrid"
  ]
}
```

### FastAPI Endpoint Structure (Assumptions)

Here’s an assumed structure for your FastAPI endpoints based on standard CRUD operations:

- `GET /questions` - List all questions
- `POST /questions` - Add a new question
- `GET /questions/{id}` - Get a question by ID
- `PUT /questions/{id}` - Update a question by ID
- `DELETE /questions/{id}` - Delete a question by ID

### `curl` Commands

#### 1. List All Questions

```bash
curl -X GET "http://0.0.0.0:8000/questions" -H "accept: application/json"
```

#### 2. Add a New Question

To add a new question, provide a JSON body with `id`, `question`, `correct_answer`, and `options`.

```bash
curl -X POST "http://0.0.0.0:8000/questions" \
     -H "Content-Type: application/json" \
     -d '{
           "id": "1",
           "question": "What is the capital of France?",
           "correct_answer": "Paris",
           "options": ["Berlin", "Paris", "Rome", "Madrid"]
         }'
```

#### 3. Get a Specific Question by ID

```bash
curl -X GET "http://0.0.0.0:8000/questions/1" -H "accept: application/json"
```

#### 4. Update a Question

To update a question by ID, include the updated JSON data in the request body.

```bash
curl -X PUT "http://0.0.0.0:8000/questions/1" \
     -H "Content-Type: application/json" \
     -d '{
           "id": "1",
           "question": "What is the capital of Germany?",
           "correct_answer": "Berlin",
           "options": ["Berlin", "Paris", "Rome", "Madrid"]
         }'
```

#### 5. Delete a Question

```bash
curl -X DELETE "http://0.0.0.0:8000/questions/1" -H "accept: application/json"
```

### Summary of `curl` Commands

| Action                  | `curl` Command                                                                                                  |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| **List All Questions**  | `curl -X GET "http://0.0.0.0:8000/questions" -H "accept: application/json"`                                      |
| **Add New Question**    | `curl -X POST "http://0.0.0.0:8000/questions" -H "Content-Type: application/json" -d '{...}'`                   |
| **Get Question by ID**  | `curl -X GET "http://0.0.0.0:8000/questions/{id}" -H "accept: application/json"`                               |
| **Update Question**     | `curl -X PUT "http://0.0.0.0:8000/questions/{id}" -H "Content-Type: application/json" -d '{...}'`              |
| **Delete Question**     | `curl -X DELETE "http://0.0.0.0:8000/questions/{id}" -H "accept: application/json"`                            |
