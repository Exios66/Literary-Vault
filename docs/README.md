---
icon: square-terminal
description: Main Landing Page to the GitBook Docs Vault Hub.
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

# The Literary Vault Docs

### Literary Vault Documentation Guide

[![Exios66 - Literary-Vault](https://img.shields.io/static/v1?label=Exios66\&message=Literary-Vault\&color=blueviolet\&logo=github)](https://github.com/Exios66/Literary-Vault) [![stars - Literary-Vault](https://img.shields.io/github/stars/Exios66/Literary-Vault?style=social)](https://github.com/Exios66/Literary-Vault) [![Docs - GitBook Dox](https://img.shields.io/badge/Docs-GitBook\_Dox-brightgreen)](https://morningstar-developments.gitbook.io/morningstar-docs)

***

### License

Released under [MIT](../LICENSE/) by [@Exios66](https://github.com/Exios66).

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE/) [![Commits](https://img.shields.io/github/commit-activity/m/Exios66/Literary-Vault.svg)](https://github.com/Exios66/Literary-Vault/commits/main) [![Issues](https://img.shields.io/github/issues/Exios66/Literary-Vault.svg)](https://github.com/Exios66/Literary-Vault/issues) [![Contributors](https://img.shields.io/github/contributors/Exios66/Literary-Vault.svg)](https://github.com/Exios66/Literary-Vault/graphs/contributors) [![Last Commit](https://img.shields.io/github/last-commit/Exios66/Literary-Vault.svg)](https://github.com/Exios66/Literary-Vault/commits/main)

### 🗂️ Repository Structure

````
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
````

<pre class="language-markdown" data-overflow="wrap" data-full-width="true"><code class="lang-markdown">#<a data-footnote-ref href="#user-content-fn-1"> </a>Literary Vault

An active catalog and toolkit supporting neuroscience research with organized documentation, backend services, and infrastructure for comprehensive analysis and API services.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
  - [Research Analysis](#research-analysis)
  - [API Services](#api-services)
  - [External Resources](#external-resources)
  - [Integration Tools](#integration-tools)
  - [Utility Scripts](#utility-scripts)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)

## Overview

Literary Vault is structured to support data-driven neuroscience research. It provides categorized research analysis, curated datasets, external resources, and REST APIs for accessing and managing these resources. With detailed integration tools and utility scripts, it is designed for scalable and secure deployment in research and development environments.

## Features

### Research Analysis
The repository organizes neuroscience-related research into well-defined categories:
- **AI Research**: Covers neural networks, the ELIZA program, and neuropsychoanalysis.
- **EEG Studies**: Includes cognitive load studies, VR integration, and research referenced in the *Oxford Handbook*.
- **Manipulation/Deception Studies**: Focuses on models of persuasion and cognitive mechanisms behind deception.

### API Services

#### Questions API
A REST API that allows categorized access to a curated dataset of questions on topics including astronomy, literature, mathematics, and general knowledge.
- **Endpoints**:
  - `GET /api/v1/questions/{category}` - Retrieve questions by category.
  - `GET /api/v1/questions/{category}/random` - Fetch random questions from a specified category.
  - `GET /api/v1/health` - Health check endpoint for service status.

#### Changelog API
Programmatic management of the project's changelog, supporting:
- Adding new entries
- Creating releases
- Querying the change history with schema validation for consistent format.

### External Resources
The repository contains additional documentation and datasets to support research:
- **Mathematics PDFs**: Mathematical references and learning material.
- **Question Datasets**: Curated question sets in CSV format across various disciplines.

### Integration Tools
Tools to simplify integrations:
- **OpenAI Function Schemas**: Templates for OpenAI function integration.
- **API Integration Guides**: Step-by-step guides to integrate with external APIs.
- **Changelog Automation**: Scripts to automate changelog updates and versioning.

### Utility Scripts
Scripts provided for streamlined repository management, including:
- **Changelog Management**: Automates updating and versioning for changelog entries.
- **API Launchers**: Scripts to start API servers.
- **Documentation Generators**: Helps maintain and organize documentation.

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Exios66/Literary-Vault.git
   cd Literary-Vault

2. Install dependencies:

```python
pip install -r requirements.txt
```


<strong># Usage
</strong>
Start API Servers

Run API servers for different modules:

# Start Questions API
python docs/api/questions_api.py

# Start Changelog API
python docs/api/changelog_api.py

Changelog Management

Use the provided scripts to add entries or create releases:

# Add an entry to the changelog
python scripts/update_changelog.py add "Added" "Description of new feature"

# Create a release entry
python scripts/update_changelog.py release "1.0.0"

Access Question Datasets

The repository includes various question sets in CSV format, accessible either via the API or directly:

	•Refined_Astronomy_Questions.csv
	•Refined_Literature_Questions.csv
	•Refined_Mathematics_Questions.csv
	•Refined_General_Knowledge_Questions.csv

Development

	• Python: Ensure Python 3.x is installed.
	• Framework: FastAPI powers the API services.
	• JSON Validation: JSON schema validation is used across APIs.
	• Documentation: Markdown format for documentation.
	• Version Control: Use Git for tracking changes.

Contribution Guidelines

We welcome contributions to enhance the Literary Vault. Please follow these guidelines:

	1. Fork the repository and create a new branch for your feature or bug fix.
	2. Follow existing naming conventions and structure.
	3. Document any new additions or changes.
	4. Submit a pull request with a clear description of the updates.

For more details, see CONTRIBUTING.md.

<strong>## License
</strong>
This project is licensed under the MIT License. See the LICENSE file for details.

<strong>### Last updated on October 28, 2024
</strong>
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

<strong>### Features:
</strong>
* Category-based retrieval
* Random selection
* Customizable limits
* OpenAPI documentation

### Endpoints:

```bash
GET /api/v1/questions/{category}
GET /api/v1/questions/{category}/random
GET /api/v1/health
```
</code></pre>



**Changelog API**

Programmatic changelog management:

* Add entries
* Create releases
* Query history
* Schema validation

#### 3. External Resources

* Mathematics PDFs
* Question datasets (CSV format)
* Reference materials
* Supplementary documentation

#### 4. Integration Tools

* OpenAI function schemas
* API integration guides
* Changelog automation
* Documentation templates

#### 5. Scripts

Utility scripts for repository management:

* Changelog management (cl)
* API servers
* Documentation generators
* Integration tools

### 🔧 Usage

#### 1. API Services

Start the API servers:

```bash
# Questions API
python docs/api/questions_api.py

# Changelog API
python docs/api/changelog_api.py
```

Access documentation:

* Questions API: [http://localhost:8000/docs](http://localhost:8000/docs)
* Changelog API: [http://localhost:8001/docs](http://localhost:8001/docs)
* Changelog Server API: [https://exios66.github.io/Literary-Vault/](https://exios66.github.io/Literary-Vault/)

#### 2. Changelog Management

```bash
# Add entry
python scripts/update_changelog.py add "Added" "New feature"

# Create release
python scripts/update_changelog.py release "1.0.0"
```

#### 3. Question Datasets

Access structured questions via API or direct CSV files:

* Refined\_Astronomy\_Questions.csv
* Refined\_Literature\_Questions.csv
* Refined\_Mathematics\_Questions.csv
* Refined\_General Knowledge\_Questions.csv

### 📋 Guidelines

* Follow API documentation
* Use provided schemas
* Update changelog
* Maintain documentation
* Follow naming conventions
* Include proper citations

### 🔒 Security

* MIT License compliance
* API authentication
* Data validation
* Error handling
* Secure endpoints

### 📚 Documentation

* API Documentation (/docs/api/)
* Integration Guides (/docs/Integration/)
* OpenAI Schemas (/docs/openai-functions/)
* Analysis Templates (/docs/Analysis/)

### 🛠️ Development

* Python 3.x required
* FastAPI for APIs
* JSON schema validation
* Markdown documentation
* Git integration

### 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### 📄 License

Released under [MIT License](LICENSE/).

***

#### Last Updated: 2024-10-28

[^1]: 
