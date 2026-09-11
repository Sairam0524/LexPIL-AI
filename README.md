# LexPIL AI - Private International Law AI Counsel

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![React 18](https://img.shields.io/badge/react-18-blue.svg)](https://react.dev/)

## Overview

LexPIL AI is a production-ready artificial intelligence platform specialized in **Private International Law (PIL)** counsel. It provides multi-agent reasoning for:

- **Dispute Characterization** - Classify legal disputes and identify relevant PIL principles
- **Jurisdiction Analysis** - Determine territorial, personal, and subject-matter jurisdiction
- **Governing Law** - Apply choice of law principles across multiple jurisdictions
- **Recognition & Enforcement** - Analyze foreign judgment recognition and enforcement
- **Litigation Strategy** - Generate evidence-based legal strategies
- **Authority Retrieval** - Access publicly available legal sources with automatic updates

## Key Features

✅ **Multi-Agent Legal Reasoning System**
- CharacterizationAgent
- JurisdictionAgent
- ChoiceOfLawAgent
- RecognitionAgent
- EnforcementAgent
- ResearchAgent
- TreatyAgent
- CitationAgent
- StrategyAgent
- NewsAgent

✅ **Automated Corpus Ingestion Pipeline**
- Daily automated updates from authorized sources
- Download → Parse → Clean → Extract → Chunk → Embed → Store
- No manual curation required

✅ **Knowledge Graph**
- Neo4j-backed relationship mapping
- Case precedent tracking
- Principle connections
- Treaty impact analysis

✅ **Real-Time Legal News**
- Court announcements monitoring
- Government gazette tracking
- Treaty update notifications

✅ **Professional UI**
- ChatGPT-like interface
- Conversation history
- Source citations
- Memo generation
- Knowledge graph visualization

## Tech Stack

**Frontend:**
- React 18 with TypeScript
- TailwindCSS for styling
- Vite build tool

**Backend:**
- FastAPI with Python 3.12
- PostgreSQL for relational data
- Neo4j for knowledge graph
- ChromaDB for vector embeddings

**AI/ML:**
- OpenAI-compatible API
- LangChain for agent orchestration

**Deployment:**
- Docker & Docker Compose
- Production-ready configuration

## Authorized Legal Sources

### India
- Supreme Court of India
- High Court websites
- India Code
- Law Commission Reports
- Gazette Notifications

### United Kingdom
- BAILII
- Legislation.gov.uk
- UK Supreme Court

### Singapore
- Singapore Statutes Online
- Singapore Judiciary

### United States
- CourtListener
- Legal Information Institute (LII)

### Australia
- AustLII

### International
- HCCH (Hague Conference)
- UNCITRAL
- UN Treaty Collection
- New York Convention materials
- CISG Database

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.12+
- Node.js 18+
- PostgreSQL 14+
- Neo4j 5.x

### Installation

```bash
# Clone repository
git clone https://github.com/Sairam0524/LexPIL-AI.git
cd LexPIL-AI

# Install backend dependencies
cd backend
pip install -r requirements.txt

# Install frontend dependencies
cd ../frontend
npm install

# Start development servers
cd ..
docker-compose up -d
```

### Access Points
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Admin Panel: http://localhost:3000/admin
- Neo4j Browser: http://localhost:7474

## API Endpoints

| Method | Endpoint | Purpose |
|--------|----------|----------|
| POST | `/api/analyze` | Analyze legal case |
| POST | `/api/chat` | Conversational legal research |
| POST | `/api/upload` | Upload document for analysis |
| GET | `/api/corpus` | Corpus statistics |
| GET | `/api/authorities` | Query legal authorities |
| GET | `/api/news` | Fetch legal news |
| GET | `/health` | Health check |

## Database Models

- **Authority** - Case law and statutory references
- **Case** - Legal judgments and decisions
- **Principle** - Legal principles and doctrine
- **JurisdictionRule** - Jurisdiction determination rules
- **Treaty** - International treaties and conventions
- **CountryProfile** - Country-specific legal profiles
- **CommentarySummary** - Analytical summaries
- **Citation** - Citation tracking and relationships
- **User** - User accounts and preferences
- **Conversation** - Chat history and context

## Knowledge Graph Structure

```
Case → establishes → Principle
Principle → relates_to → Jurisdiction
Principle → relates_to → ChoiceOfLaw
Case → cites → Case
Country → applies → Rule
Treaty → affects → Country
```

## Project Structure

```
LexPIL-AI/
├── frontend/                 # React TypeScript application
├── backend/                  # FastAPI application
├── database/                 # Database schemas and migrations
├── corpus/                   # Legal source configurations
├── ai/                       # Multi-agent system
├── ingestion/                # Corpus ingestion pipeline
├── deployment/               # Docker and deployment configs
└── docs/                     # Complete documentation
```

## Configuration

All configuration is managed via environment variables. See `.env.example` for template.

## Authentication

JWT-based authentication with three roles:
- **Admin** - Full system access
- **Researcher** - Corpus access and analysis
- **User** - Basic chat and research

## Testing

```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd ../frontend
npm test

# Integration tests
cd ..
pytest integration/
```

## Continuous Updates

The system automatically:
1. Checks configured legal sources daily
2. Downloads new judgments and statutes
3. Creates embeddings
4. Updates vector database
5. Updates Neo4j graph
6. Recomputes authority relationships

## Production Deployment

See [deployment.md](./docs/deployment.md) for comprehensive deployment guide.

## Documentation

- [Architecture Overview](./docs/architecture.md)
- [API Reference](./docs/api_reference.md)
- [Corpus Design](./docs/corpus_design.md)
- [Deployment Guide](./docs/deployment.md)
- [Contributing Guidelines](./CONTRIBUTING.md)

## Legal Compliance

This platform uses **only publicly accessible and official legal sources**. It does not:
- Scrape copyrighted databases (Westlaw, LexisNexis, etc.)
- Violate intellectual property rights
- Provide legal advice (educational purpose only)

## License

MIT License - See LICENSE file for details

## Support

For issues and questions:
- GitHub Issues: https://github.com/Sairam0524/LexPIL-AI/issues
- Documentation: https://github.com/Sairam0524/LexPIL-AI/wiki

## Disclaimer

LexPIL AI provides legal information and analysis for educational purposes. It is not a substitute for professional legal advice. Always consult qualified legal professionals for actual legal matters.

---

**Developed with ❤️ for the global legal community**
