# LexPIL AI - Complete Codebase Reference

## Table of Contents
1. [Backend Architecture](#backend-architecture)
2. [Frontend Architecture](#frontend-architecture)
3. [Database Models](#database-models)
4. [Multi-Agent System](#multi-agent-system)
5. [Corpus Ingestion](#corpus-ingestion)
6. [API Reference](#api-reference)
7. [Deployment](#deployment)

---

## Backend Architecture

### Main Application (main.py)
- FastAPI application initialization
- CORS middleware configuration
- Route registration
- Lifecycle management (startup/shutdown)
- Global exception handling

### Application Configuration (app/config.py)
- Environment variable management
- Database URLs
- API keys and secrets
- Model parameters
- Application settings

### Database Layer (app/database.py)
- PostgreSQL connection pooling
- Neo4j driver initialization
- ChromaDB client setup
- Session management
- Database initialization

### Data Models (app/models/)
- Authority - Cases, statutes, treaties
- Case - Judicial decisions
- Principle - Legal doctrines
- JurisdictionRule - Jurisdiction rules
- Treaty - International agreements
- CountryProfile - Country-specific rules
- Citation - Citation relationships
- User - User accounts
- Conversation - Chat history

---

## Frontend Architecture

### Pages
1. **Chat.tsx** - Conversational legal research interface
2. **Analysis.tsx** - Case analysis form and results
3. **Corpus.tsx** - Corpus statistics dashboard
4. **News.tsx** - Legal news feed
5. **Admin.tsx** - Admin control panel

### Components
1. **Layout.tsx** - Main layout with navigation
2. **ChatMessage.tsx** - Message display component
3. **SourceCitations.tsx** - Citation display

### Hooks
1. **useChat.ts** - Chat API integration
2. **useAnalyze.ts** - Case analysis API integration

---

## Multi-Agent System

### Base Agent (app/agents/base_agent.py)
- Abstract base class for all agents
- LLM integration
- System prompt management
- Error handling

### Specialized Agents
1. **CharacterizationAgent** - Dispute type classification
2. **JurisdictionAgent** - Jurisdiction determination
3. **ChoiceOfLawAgent** - Governing law analysis
4. **RecognitionAgent** - Foreign judgment recognition
5. **EnforcementAgent** - Enforcement strategy
6. **ResearchAgent** - Authority retrieval
7. **TreatyAgent** - Treaty analysis
8. **CitationAgent** - Citation management
9. **StrategyAgent** - Litigation strategy
10. **NewsAgent** - News analysis

### Orchestrator (app/agents/orchestrator.py)
- Coordinates all agents
- Manages workflow
- Aggregates results
- Handles dependencies

---

## Corpus Ingestion Pipeline

### Source Downloader (app/ingestion/source_downloader.py)
- Downloads from authorized sources
- Handles HTTP requests
- Rate limiting
- Error recovery

### Content Parser (app/ingestion/content_parser.py)
- Parses HTML and text
- Extracts judgment information
- Validates content

### Citation Extractor (app/ingestion/citation_extractor.py)
- Identifies case citations
- Extracts statute references
- Finds treaty mentions
- Uses regex patterns

### Document Chunker (app/ingestion/document_chunker.py)
- Splits documents into chunks
- Maintains context with overlap
- Preserves structure

### Embedding Generator (app/ingestion/embedding_generator.py)
- Creates vector embeddings
- Batch processing
- ChromaDB integration

### Corpus Updater (app/ingestion/corpus_updater.py)
- Orchestrates entire pipeline
- Manages workflow
- Updates all systems

---

## API Endpoints

### Case Analysis
```
POST /api/analyze
Request: Case facts
Response: Complete analysis with all agents' output
```

### Chat
```
POST /api/chat
Request: User message
Response: Assistant response with citations
```

### Corpus
```
GET /api/corpus
Response: Corpus statistics

POST /api/upload
Request: File upload
Response: Upload confirmation
```

### Authorities
```
GET /api/authorities
Query params: jurisdiction, authority_type, keyword, limit
Response: List of matching authorities

GET /api/authorities/{id}
Response: Authority details
```

### News
```
GET /api/news
Query params: jurisdiction, days, limit
Response: Legal news items

GET /api/news/categories
Response: Available news categories
```

### Admin
```
GET /api/admin/stats
Response: System statistics

POST /api/admin/reindex
Request: Source specification
Response: Reindex status

POST /api/admin/rebuild-graph
Response: Graph rebuild status
```

### Health
```
GET /health
Response: System health status
```

---

## Deployment

### Docker Compose Services
1. **PostgreSQL** - Relational database (port 5432)
2. **Neo4j** - Graph database (ports 7687, 7474)
3. **ChromaDB** - Vector store (port 8000)
4. **Redis** - Cache layer (port 6379)
5. **Backend** - FastAPI server (port 8000)
6. **Frontend** - React app (port 3000)

### Environment Configuration
See `.env.example` for all required variables

### Running the Application

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Access services
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
# Neo4j: http://localhost:7474
```

---

## Key Technologies

- **Frontend**: React 18, TypeScript, TailwindCSS, Vite
- **Backend**: FastAPI, Python 3.12, Pydantic
- **Databases**: PostgreSQL, Neo4j, ChromaDB, Redis
- **AI/ML**: OpenAI API, LangChain, Vector embeddings
- **Infrastructure**: Docker, Docker Compose
- **Testing**: pytest, vitest

---

## Authorization & Security

- JWT token-based authentication
- Role-based access control (Admin, Researcher, User)
- CORS configuration
- Environment variable management
- SQL injection prevention via ORM

---

## Performance Optimization

- Connection pooling (PostgreSQL)
- Redis caching layer
- ChromaDB HNSW indexing
- Batch processing in ingestion
- Async/await for non-blocking operations
- Stateless API design

---

For complete implementation details, refer to the individual files in the repository.
