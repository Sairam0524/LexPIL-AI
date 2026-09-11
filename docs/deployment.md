# Deployment Guide

## Prerequisites

- Docker & Docker Compose 2.0+
- Python 3.12 (for local development)
- Node.js 18+ (for frontend development)
- OpenAI API key
- PostgreSQL 14+ (if not using Docker)
- Neo4j 5.x (if not using Docker)

## Local Development with Docker

### Quick Start

```bash
# Clone repository
git clone https://github.com/Sairam0524/LexPIL-AI.git
cd LexPIL-AI

# Copy environment file
cp .env.example .env

# Set your OpenAI API key
echo "OPENAI_API_KEY=your_key_here" >> .env
echo "JWT_SECRET=your_secret_here" >> .env

# Start all services
docker-compose up -d
```

## Production Deployment

For production, use:
- Kubernetes for orchestration
- AWS ECS, Google Cloud Run, or Azure Container Instances
- CloudFlare for CDN and DDoS protection
- Managed databases (AWS RDS, Google Cloud SQL)

## Environment Configuration

Required environment variables in .env file - see .env.example for complete list.

## Monitoring

```bash
# Health check
curl http://localhost:8000/health

# View logs
docker-compose logs -f backend
```

## Support

For deployment issues, refer to the documentation folder or create an issue on GitHub.
