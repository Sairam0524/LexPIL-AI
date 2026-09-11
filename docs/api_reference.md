# API Reference

## Base URL
```
http://localhost:8000/api
```

## Authentication
All protected endpoints require a JWT token in the `Authorization` header:
```
Authorization: Bearer <token>
```

## Endpoints

### Case Analysis

#### POST /analyze
Analyze a legal case using the multi-agent system.

**Request:**
```json
{
  "party1": "Company A",
  "party2": "Company B",
  "party1_jurisdiction": "India",
  "party2_jurisdiction": "Singapore",
  "dispute_subject": "Contract",
  "facts": "Detailed case facts...",
  "additional_context": {}
}
```

**Response:**
```json
{
  "status": "success",
  "analysis": {
    "characterization": { ... },
    "jurisdiction": { ... },
    "choice_of_law": { ... },
    "treaties": { ... },
    "recognition": { ... },
    "enforcement": { ... },
    "research": { ... },
    "citations": { ... },
    "strategy": { ... }
  }
}
```

### Chat

#### POST /chat
Send a message for legal research.

**Request:**
```json
{
  "user_id": 1,
  "message": "What is the governing law for this contract?",
  "conversation_id": null
}
```

**Response:**
```json
{
  "status": "success",
  "conversation_id": 123,
  "response": "Based on the parties...",
  "cited_authorities": ["2023 SCC Online 1234", ...]
}
```

### Corpus Management

#### GET /corpus
Get corpus statistics.

**Response:**
```json
{
  "status": "success",
  "statistics": {
    "total_authorities": 15000,
    "total_cases": 25000,
    "total_treaties": 300,
    "last_updated": "2025-09-11T12:00:00Z"
  }
}
```

#### POST /upload
Upload a document for analysis.

**Form Data:**
- `file`: PDF or text file

**Response:**
```json
{
  "status": "success",
  "message": "Document uploaded successfully"
}
```

### Authorities

#### GET /authorities
Search legal authorities.

**Query Parameters:**
- `jurisdiction` (string): Filter by jurisdiction
- `authority_type` (string): case|statute|treaty|regulation|doctrine
- `keyword` (string): Search keyword
- `limit` (integer): Max results (default: 20, max: 100)

**Response:**
```json
{
  "status": "success",
  "authorities": [
    {
      "id": 1,
      "title": "Case Name",
      "citation": "2023 SCC 123",
      "jurisdiction": "India",
      "year": 2023
    }
  ],
  "total": 150
}
```

#### GET /authorities/{authority_id}
Get authority details.

**Response:**
```json
{
  "status": "success",
  "authority": {
    "id": 1,
    "title": "Full Case Title",
    "content": "Full judgment text...",
    "summary": "Brief summary...",
    "citations": ["2023 SCC 124", ...]
  }
}
```

### News

#### GET /news
Get recent legal news.

**Query Parameters:**
- `jurisdiction` (string): Filter by jurisdiction
- `days` (integer): Days to look back (default: 7, max: 90)
- `limit` (integer): Max results (default: 20, max: 100)

**Response:**
```json
{
  "status": "success",
  "news": [
    {
      "id": 1,
      "title": "New Court Decision",
      "source": "Court Announcements",
      "date": "2025-09-11",
      "summary": "...",
      "pil_impact": "High"
    }
  ],
  "total": 42
}
```

#### GET /news/categories
Get available news categories.

**Response:**
```json
{
  "status": "success",
  "categories": [
    "Court Announcements",
    "Government Gazettes",
    "Treaty Updates",
    "Judicial Updates"
  ]
}
```

### Admin

#### GET /admin/stats
Get admin statistics (Admin only).

**Response:**
```json
{
  "status": "success",
  "statistics": {
    "total_users": 150,
    "total_conversations": 5000,
    "corpus_size": "50GB",
    "last_update": "2025-09-11T12:00:00Z"
  }
}
```

#### POST /admin/reindex
Reindex corpus (Admin only).

**Request:**
```json
{
  "source": "bailii"
}
```

**Response:**
```json
{
  "status": "success",
  "message": "Reindexing started"
}
```

#### POST /admin/rebuild-graph
Rebuild Neo4j graph (Admin only).

**Response:**
```json
{
  "status": "success",
  "message": "Graph rebuild started"
}
```

### Health

#### GET /health
Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "service": "LexPIL AI",
  "version": "1.0.0"
}
```

## Error Responses

All error responses follow this format:
```json
{
  "status": "error",
  "detail": "Error description",
  "error_type": "ValueError|DatabaseError|etc"
}
```

HTTP Status Codes:
- 200: Success
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error
