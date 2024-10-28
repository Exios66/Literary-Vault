---
icon: square-terminal
cover: >-
  https://images.unsplash.com/photo-1505664194779-8beaceb93744?crop=entropy&cs=srgb&fm=jpg&ixid=M3wxOTcwMjR8MHwxfHNlYXJjaHw2fHxsaWJyYXJ5fGVufDB8fHx8MTczMDAyMTMyNXww&ixlib=rb-4.0.3&q=85
coverY: 0
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Literary Vault Documentation

[![Exios66 - Literary-Vault](https://img.shields.io/static/v1?label=Exios66&message=Literary-Vault&color=blueviolet&logo=github)](https://github.com/Exios66/Literary-Vault "Go to GitHub repo")
[![stars - Literary-Vault](https://img.shields.io/github/stars/Exios66/Literary-Vault?style=social)](https://github.com/Exios66/Literary-Vault)
[![Docs - GitBook Dox](https://img.shields.io/badge/Docs-GitBook_Dox-brightgreen)](https://morningstar-developments.gitbook.io/morningstar-docs)

***

## License

Released under [MIT](/LICENSE) by [@Exios66](https://github.com/Exios66).

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE/)
[![Commits](https://img.shields.io/github/commit-activity/m/Exios66/Literary-Vault.svg)](https://github.com/Exios66/Literary-Vault/commits/main)
[![Issues](https://img.shields.io/github/issues/Exios66/Literary-Vault.svg)](https://github.com/Exios66/Literary-Vault/issues)
[![Contributors](https://img.shields.io/github/contributors/Exios66/Literary-Vault.svg)](https://github.com/Exios66/Literary-Vault/graphs/contributors)
[![Last Commit](https://img.shields.io/github/last-commit/Exios66/Literary-Vault.svg)](https://github.com/Exios66/Literary-Vault/commits/main)

## 🗂️ Repository Structure

```bash
literary-vault/
├── analysis/              # Detailed analysis of research papers
│   ├── AI-Research/      # AI-related research analysis
│   ├── EEG/             # EEG research analysis
│   └── Manipulation-Deception/ # Studies on manipulation/deception
├── docs/                 # Repository documentation
│   ├── Analysis/        # Detailed research analysis
│   ├── api/            # API documentation and implementation
│   ├── Integration/    # Integration guides
│   ├── openai-functions/ # OpenAI function schemas
│   └── pdfs/           # PDF documentation
├── external-resources/   # Additional resources
│   ├── Math-PDFs/      # Mathematics resources
│   └── questions/      # Question datasets
├── scripts/             # Utility scripts
├── CHANGELOG.md         # Project change history
├── CONTRIBUTING.md      # Contribution guidelines
├── LICENSE             # MIT License
└── README.md           # Repository documentation
```

## 📚 Components

### 1. Analysis Directory

Comprehensive research analysis organized by topic:

* AI Research (neural networks, ELIZA program, neuropsychoanalysis)
* EEG Studies (cognitive load, VR integration, Oxford handbook)
* Manipulation/Deception (persuasion models, cognitive mechanisms)

### 2. API Services

#### Questions API

REST API for accessing curated question datasets:

* Astronomy questions
* Literature questions
* Mathematics questions
* General Knowledge questions

Features:

* Category-based retrieval
* Random selection
* Customizable limits
* OpenAPI documentation

Endpoints:

```bash
GET /api/v1/questions/{category}
GET /api/v1/questions/{category}/random
GET /api/v1/health
```

#### Changelog API

Programmatic changelog management:

* Add entries
* Create releases
* Query history
* Schema validation

### 3. External Resources

* Mathematics PDFs
* Question datasets (CSV format)
* Reference materials
* Supplementary documentation

### 4. Integration Tools

* OpenAI function schemas
* API integration guides
* Changelog automation
* Documentation templates

### 5. Scripts

Utility scripts for repository management:

* Changelog management (cl)
* API servers
* Documentation generators
* Integration tools

## 🔧 Usage

### 1. API Services

Start the API servers:

```bash
# Questions API
python docs/api/questions_api.py

# Changelog API
python docs/api/changelog_api.py
```

Access documentation:

* Questions API: http://localhost:8000/docs
* Changelog API: http://localhost:8001/docs

### 2. Changelog Management

```bash
# Add entry
python scripts/update_changelog.py add "Added" "New feature"

# Create release
python scripts/update_changelog.py release "1.0.0"
```

### 3. Question Datasets

Access structured questions via API or direct CSV files:

* Refined_Astronomy_Questions.csv
* Refined_Literature_Questions.csv
* Refined_Mathematics_Questions.csv
* Refined_General Knowledge_Questions.csv

## 📋 Guidelines

* Follow API documentation
* Use provided schemas
* Update changelog
* Maintain documentation
* Follow naming conventions
* Include proper citations

## 🔒 Security

* MIT License compliance
* API authentication
* Data validation
* Error handling
* Secure endpoints

## 📚 Documentation

* API Documentation (/docs/api/)
* Integration Guides (/docs/Integration/)
* OpenAI Schemas (/docs/openai-functions/)
* Analysis Templates (/docs/Analysis/)

## 🛠️ Development

* Python 3.x required
* FastAPI for APIs
* JSON schema validation
* Markdown documentation
* Git integration

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

Released under [MIT License](LICENSE).

---

Last Updated: 2024-01-27
