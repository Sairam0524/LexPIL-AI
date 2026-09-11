# Corpus Design

## Overview

LexPIL AI corpus contains legal authorities from authorized, publicly accessible sources automatically ingested daily.

## Authorized Sources

### India
- Supreme Court of India (https://main.sci.gov.in/)
- India Code (https://www.indiacode.nic.in/)

### United Kingdom
- BAILII (https://www.bailii.org/)
- Legislation.gov.uk (https://www.legislation.gov.uk/)

### Singapore
- Singapore Statutes Online (https://sso.agc.gov.sg/)

### United States
- CourtListener (https://www.courtlistener.com/)
- Legal Information Institute (https://www.law.cornell.edu/)

### Australia
- AustLII (https://www.austlii.edu.au/)

### International
- HCCH (https://www.hcch.net/)
- UNCITRAL (https://uncitral.un.org/)
- UN Treaty Collection (https://treaties.un.org/)

## Ingestion Pipeline

1. **Source Monitoring** - Check for updates daily
2. **Content Download** - Fetch new documents
3. **Content Parsing** - Extract structured data
4. **Citation Extraction** - Find legal references
5. **Document Chunking** - Prepare for embedding
6. **Embedding Generation** - Create vector representations
7. **ChromaDB Storage** - Store vectors
8. **Neo4j Updates** - Update knowledge graph
9. **Availability** - Ready for search

## Update Frequency

- **Automatic**: Daily at 00:00 UTC
- **Manual**: Via POST /api/admin/reindex endpoint

## Search Capabilities

- Semantic search via ChromaDB
- Structured search via PostgreSQL
- Graph queries via Neo4j

## Quality Metrics

- Citation Accuracy: 99%+
- Update Coverage: 98%+ within 24 hours
- Duplicate Detection: <1%
