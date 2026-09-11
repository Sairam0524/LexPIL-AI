# Architecture Overview

## System Architecture

LexPIL AI follows a modern microservices architecture with clear separation of concerns:

### Frontend Layer
- **React 18** with TypeScript for type safety
- **TailwindCSS** for styling
- **Vite** for build optimization
- ChatGPT-like interface for user interaction
- Real-time source citations and knowledge graph visualization

### Backend Layer
- **FastAPI** (Python 3.12) for high-performance API
- **JWT authentication** with role-based access control
- **WebSocket support** for real-time chat
- RESTful endpoints for case analysis and research

### Database Layer
- **PostgreSQL** for relational data (cases, authorities, users)
- **Neo4j** for knowledge graph (relationships between entities)
- **ChromaDB** for vector embeddings and semantic search
- **Redis** for caching and session management

### AI/ML Layer
- **Multi-Agent System** with specialized agents:
  - CharacterizationAgent - Dispute classification
  - JurisdictionAgent - Jurisdiction determination
  - ChoiceOfLawAgent - Governing law analysis
  - RecognitionAgent - Foreign judgment recognition
  - EnforcementAgent - Enforcement strategy
  - ResearchAgent - Authority retrieval
  - TreatyAgent - Treaty analysis
  - CitationAgent - Citation analysis
  - StrategyAgent - Litigation strategy
  - NewsAgent - Legal news analysis
- **AgentOrchestrator** coordinates all agents
- **OpenAI-compatible API** for LLM integration

### Corpus Layer
- **Source Downloader** - Fetches from authorized sources
- **Content Parser** - Extracts structured data
- **Citation Extractor** - Identifies legal citations
- **Document Chunker** - Prepares text for embedding
- **Embedding Generator** - Creates vector representations
- **Corpus Updater** - Orchestrates daily updates

## Data Flow

### Case Analysis Workflow
```
User Input
    ↓
CharacterizationAgent (Identify dispute type)
    ↓
JurisdictionAgent (Determine jurisdiction)
    ↓
ChoiceOfLawAgent (Identify governing law)
    ↓
TreatyAgent (Applicable treaties)
    ↓
RecognitionAgent (Recognition issues)
    ↓
EnforcementAgent (Enforcement options)
    ↓
ResearchAgent (Find supporting authorities)
    ↓
CitationAgent (Format citations)
    ↓
StrategyAgent (Generate litigation strategy)
    ↓
Comprehensive Analysis Report
```

### Corpus Update Workflow
```
Scheduler Trigger (Daily)
    ↓
Source Downloader (Get new documents)
    ↓
Content Parser (Extract content)
    ↓
Citation Extractor (Find citations)
    ↓
Document Chunker (Prepare for embedding)
    ↓
Embedding Generator (Create vectors)
    ↓
ChromaDB Storage (Vector DB)
    ↓
Neo4j Graph Update (Relationships)
    ↓
Available for Search & Retrieval
```

## Knowledge Graph Structure

### Entities
- **Case** - Judicial decisions
- **Authority** - Statutes, treaties, regulations
- **Principle** - Legal doctrines and rules
- **Country** - Jurisdictions
- **Treaty** - International agreements
- **Court** - Judicial institutions

### Relationships
```
Case --cites--> Case
Case --establishes--> Principle
Principle --relates_to--> Jurisdiction
Principle --relates_to--> ChoiceOfLaw
Country --applies--> Rule
Country --ratifies--> Treaty
Treaty --affects--> Country
Court --located_in--> Country
```

## Security Architecture

### Authentication
- JWT tokens with configurable expiration
- HS256 signing algorithm
- Refresh token support (TODO)

### Authorization
- Role-based access control (RBAC)
- Three roles: Admin, Researcher, User
- Endpoint-level permission checking

### Data Protection
- CORS configuration for frontend origins
- HTTPS support in production
- Environment variable management for secrets
- SQL injection prevention via SQLAlchemy ORM

## Scalability Considerations

### Horizontal Scaling
- Stateless API design enables load balancing
- Separate services (database, cache, vector store)
- Docker containerization for easy deployment

### Performance Optimization
- ChromaDB for efficient vector similarity search
- Redis caching layer
- Batch processing in corpus ingestion
- Connection pooling for databases

### Deployment Flexibility
- Docker Compose for local development
- Kubernetes-ready architecture
- Cloud-agnostic infrastructure code

## Integration Points

### OpenAI API
- Chat completions for agent reasoning
- Embedding generation for corpus
- Configurable model selection

### Legal Databases
- Web scraping with BeautifulSoup
- Feed parsing with feedparser
- RSS monitoring for updates
- Rate limiting to respect source policies

### External Services (Future)
- Email notifications
- SMS alerts
- Integration with legal practice management tools
