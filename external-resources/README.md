---
icon: screwdriver-wrench
---

# External Resources

This directory contains supplementary materials and datasets that support the research and analysis in the Literary Vault.

## Directory Structure

```bash
external-resources/
├── Math-PDFs/           # Mathematics resources and documents
│   └── 2021-released-items-math-g5.pdf
├── questions/           # Question datasets in CSV format
│   ├── Refined_Astronomy_Questions.csv
│   ├── Refined_Literature_Questions.csv
│   ├── Refined_Mathematics_Questions.csv
│   └── Refined_General Knowledge_Questions.csv
└── README.md           # This file
```

## Question Datasets

### Available Categories

1. **Astronomy Questions**
   * Celestial objects and phenomena
   * Space exploration
   * Astronomical concepts
   * [View Dataset](questions/Refined_Astronomy_Questions.csv)

2. **Literature Questions**
   * Literary works
   * Authors and genres
   * Literary analysis
   * [View Dataset](questions/Refined_Literature_Questions.csv)

3. **Mathematics Questions**
   * Mathematical concepts
   * Problem-solving
   * Numerical reasoning
   * [View Dataset](questions/Refined_Mathematics_Questions.csv)

4. **General Knowledge Questions**
   * Diverse topics
   * Interdisciplinary content
   * General concepts
   * [View Dataset](questions/Refined_General Knowledge_Questions.csv)

### API Integration

These datasets are accessible through the Questions API:

```bash
# Get questions by category
GET /api/v1/questions/{category}

# Get random questions
GET /api/v1/questions/{category}/random
```

See [API Documentation](../docs/api/README.md) for detailed usage.

## Mathematics Resources

### Available Documents

* **2021 Released Items (Grade 5)**
  * Mathematical problems
  * Solution strategies
  * Assessment materials
  * [View PDF](Math-PDFs/2021-released-items-math-g5.pdf)

### Usage Guidelines

1. **Question Datasets**
   * CSV format for easy parsing
   * Consistent structure across categories
   * Regular updates and maintenance
   * API-friendly format

2. **Math PDFs**
   * Educational reference
   * Problem-solving examples
   * Teaching resources
   * Assessment preparation

## Contributing

When adding new resources:

1. Follow naming conventions
2. Update relevant documentation
3. Maintain data structure
4. Test API compatibility
5. Include source references

## Data Format

### Question CSV Structure

```csv
id,question,correct_answer,options
AST_001,"What is the closest star to Earth?","Sun","['Sun', 'Proxima Centauri', 'Alpha Centauri', 'Sirius']"
```

### Required Fields

* id: Unique identifier
* question: Question text
* correct_answer: The answer
* options: Multiple choice options

## Maintenance

* Regular dataset updates
* Quality assurance checks
* Format validation
* API compatibility testing
* Documentation updates

## Related Documentation

* [API Documentation](../docs/api/README.md)
* [Integration Guide](../docs/Integration/changelog-integration.md)
* [OpenAI Functions](../docs/openai-functions/)

---

Last Updated: 2024-01-27
