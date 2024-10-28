---
icon: database
---

# Question Datasets

This directory contains structured question datasets in CSV format, designed for use with the Questions API.

## Available Datasets

### 1. Astronomy Questions

* [Refined_Astronomy_Questions.csv](Refined_Astronomy_Questions.csv)
  * Celestial objects
  * Space exploration
  * Astronomical phenomena
  * Scientific concepts

### 2. Literature Questions

* [Refined_Literature_Questions.csv](Refined_Literature_Questions.csv)
  * Literary works
  * Authors and genres
  * Literary analysis
  * Historical context

### 3. Mathematics Questions

* [Refined_Mathematics_Questions.csv](Refined_Mathematics_Questions.csv)
  * Mathematical concepts
  * Problem-solving
  * Numerical reasoning
  * Applied mathematics

### 4. General Knowledge Questions

* [Refined_General Knowledge_Questions.csv](Refined_General Knowledge_Questions.csv)
  * Diverse topics
  * Interdisciplinary content
  * General concepts
  * Cultural knowledge

### 5. Geography Questions

* [Refined_Geography_Questions.csv](Refined_Geography_Questions.csv)
  * World geography
  * Physical features
  * Cultural geography
  * Map skills

## Data Format

### CSV Structure

```csv
id,question,correct_answer,options
AST_001,"What is the closest star to Earth?","Sun","['Sun', 'Proxima Centauri', 'Alpha Centauri', 'Sirius']"
```

### Required Fields

* id: Unique identifier
* question: Question text
* correct_answer: Correct answer
* options: Multiple choice options (JSON array)

## API Integration

### Endpoints

```bash
# Get questions by category
GET /api/v1/questions/{category}

# Get random questions
GET /api/v1/questions/{category}/random
```

### Features

* Category filtering
* Random selection
* Limit control
* Response formatting

## Usage Guidelines

### Data Management

* Regular updates
* Quality control
* Format validation
* Content review

### Implementation

* API integration
* Error handling
* Response parsing
* Cache management

## Contributing

When adding questions:

1. Follow CSV format
2. Validate content
3. Update documentation
4. Test API integration
5. Review accuracy

## Maintenance

* Content updates
* Format validation
* API compatibility
* Documentation updates

---

Last Updated: 2024-01-27
