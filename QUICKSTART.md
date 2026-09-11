# LexPIL AI - Quick Start Guide

## Quick Start (5 minutes)

```bash
# Clone repository
git clone https://github.com/Sairam0524/LexPIL-AI.git
cd LexPIL-AI

# Create .env file
echo "OPENAI_API_KEY=your_openai_key" > .env
echo "JWT_SECRET=your_jwt_secret" >> .env

# Start all services
docker-compose up -d

# Wait for services to be healthy (30 seconds)
sleep 30

# Access the application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## Project Structure

```
LexPIL-AI/
├── frontend/         # React + TypeScript UI
├── backend/          # FastAPI + Python
├── database/         # Database schemas
├── ai/               # Multi-agent system
├── ingestion/        # Corpus pipeline
├── deployment/       # Docker configs
├── docs/             # Complete documentation
└── tests/            # Test suites
```

## Key Features

✅ Multi-agent legal analysis system
✅ Automated corpus ingestion with daily updates
✅ ChatGPT-like interface for legal research
✅ Real-time source citations
✅ Knowledge graph (Neo4j)
✅ Vector search (ChromaDB)
✅ Admin panel for management

## 10 Specialized Agents

1. **CharacterizationAgent** - Classify disputes
2. **JurisdictionAgent** - Determine jurisdiction
3. **ChoiceOfLawAgent** - Identify governing law
4. **RecognitionAgent** - Analyze recognition issues
5. **EnforcementAgent** - Plan enforcement
6. **ResearchAgent** - Retrieve authorities
7. **TreatyAgent** - Analyze treaties
8. **CitationAgent** - Format citations
9. **StrategyAgent** - Generate litigation strategy
10. **NewsAgent** - Monitor legal news

## Quick API Example

```bash
curl -X POST http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "party1": "Company A",
    "party2": "Company B",
    "party1_jurisdiction": "India",
    "party2_jurisdiction": "Singapore",
    "dispute_subject": "Contract",
    "facts": "Breach of service agreement"
  }'
```

## Common Commands

```bash
# View logs
docker-compose logs -f backend

# Run tests
pytest backend/tests/

# Health check
curl http://localhost:8000/health

# Access database
docker-compose exec postgres psql -U lexpil -d lexpil

# Stop services
docker-compose down
```

## Troubleshooting

**Services won't start:**
```bash
docker-compose down -v
docker-compose up -d
```

**API not responding:**
```bash
curl http://localhost:8000/health
docker-compose logs backend
```

## Next Steps

1. Access frontend at http://localhost:3000
2. Try analyzing a legal case
3. Explore corpus statistics
4. Review admin panel
5. Read full documentation in /docs

## Documentation

- 📖 [Architecture](docs/architecture.md)
- 📚 [API Reference](docs/api_reference.md)
- 🔄 [Deployment Guide](docs/deployment.md)
- 📋 [Corpus Design](docs/corpus_design.md)
- 🤝 [Contributing](CONTRIBUTING.md)

## Support

- 🐛 Issues: GitHub Issues
- 💬 Discussions: GitHub Discussions
- 📧 Maintainers: [GitHub Profile]

## License

MIT - See LICENSE file

---

**Ready to start?** → `docker-compose up -d`
