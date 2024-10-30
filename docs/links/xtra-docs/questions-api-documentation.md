# Questions API Documentation

#### Get Questions

Retrieves questions from a specific category.

**Parameters**

| Name     | Type            | Required | Description                                                   |
| -------- | --------------- | -------- | ------------------------------------------------------------- |
| category | string (path)   | Yes      | Category of questions (astronomy, literature, or mathematics) |
| limit    | integer (query) | No       | Maximum number of questions to return (1-50, default: 10)     |
| random   | boolean (query) | No       | Whether to return random questions (default: true)            |

**Response Schema**

{ "type": "array", "items": { "type": "object", "properties": { "id": { "type": "string", "description": "Unique identifier for the question" }, "question": { "type": "string", "description": "The question text" }, "correct\_answer": { "type": "string", "description": "The correct answer" }, "options": { "type": "array", "items": { "type": "string" }, "description": "Multiple choice options if applicable" } }, "required": \["id", "question", "correct\_answer"] } }

**Example Response**

\[ { "id": "ASTRO\_001", "question": "What is the closest star to Earth besides the Sun?", "correct\_answer": "Proxima Centauri", "options": \[ "Proxima Centauri", "Alpha Centauri A", "Barnard's Star", "Sirius" ] } ]

#### Randomize Questions

Generates a random set of questions from a specific category.

**Parameters**

| Name     | Type           | Required | Description                                                   |
| -------- | -------------- | -------- | ------------------------------------------------------------- |
| category | string (body)  | Yes      | Category of questions (astronomy, literature, or mathematics) |
| count    | integer (body) | No       | Number of questions to return (1-20, default: 5)              |
| seed     | integer (body) | No       | Random seed for reproducible results                          |

**Request Body Schema**

{ "type": "object", "properties": { "category": { "type": "string", "enum": \["astronomy", "literature", "mathematics"] }, "count": { "type": "integer", "minimum": 1, "maximum": 20, "default": 5 }, "seed": { "type": "integer", "description": "Optional random seed" } }, "required": \["category"] }

**Example Response**

\[ { "id": "MATH\_003", "question": "What is the value of π (pi) to two decimal places?", "correct\_answer": "3.14", "options": \[ "3.14", "3.16", "3.12", "3.18" ] }, { "id": "MATH\_007", "question": "What is the square root of 144?", "correct\_answer": "12", "options": \[ "12", "14", "10", "16" ] } ]

### Models

#### Category (enum)

enum Category { astronomy literature mathematics }

#### QuestionBase

{ "type": "object", "properties": { "id": { "type": "string", "description": "Unique identifier for the question" }, "question": { "type": "string", "description": "The question text" }, "correct\_answer": { "type": "string", "description": "The correct answer" }, "options": { "type": "array", "items": { "type": "string" }, "description": "Multiple choice options if applicable" } }, "required": \["id", "question", "correct\_answer"] }
