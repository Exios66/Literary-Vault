---
icon: square-terminal
---

# Open Ai Functions - Get Questions

### GET QUESTIONS

```json
// {
  "name": "get_questions",
  "description": "Retrieves questions from the repository's structured CSV files",
  "parameters": {
    "type": "object",
    "properties": {
      "category": {
        "type": "string",
        "description": "The category of questions to retrieve (astronomy, literature, or mathematics)",
        "enum": ["astronomy", "literature", "mathematics"]
      },
      "limit": {
        "type": "integer",
        "description": "Maximum number of questions to return",
        "default": 10,
        "minimum": 1,
        "maximum": 50
      },
      "random": {
        "type": "boolean",
        "description": "Whether to return random questions or sequential ones",
        "default": true
      }
    },
    "required": ["category"]
  },
  "returns": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "Unique identifier for the question"
        },
        "question": {
          "type": "string",
          "description": "The question text"
        },
        "options": {
          "type": "array",
          "description": "Multiple choice options if applicable",
          "items": {
            "type": "string"
          }
        },
        "correct_answer": {
          "type": "string",
          "description": "The correct answer to the question"
        }
      },
      "required": ["id", "question", "correct_answer"]
    }
  }
}
```
