from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://lexpil:password@localhost:5432/lexpil"
    neo4j_url: str = "neo4j://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"
    
    # ChromaDB
    chroma_host: str = "localhost"
    chroma_port: int = 8000
    
    # API
    openai_api_key: str
    openai_model: str = "gpt-4-turbo-preview"
    openai_base_url: str = "https://api.openai.com/v1"
    
    # JWT
    jwt_secret: str
    jwt_algorithm: str = "HS256"
    jwt_expiration_hours: int = 24
    
    # Application
    app_env: str = "development"
    app_debug: bool = False
    app_port: int = 8000
    frontend_url: str = "http://localhost:3000"
    backend_url: str = "http://localhost:8000"
    
    # Corpus
    corpus_update_hour: int = 0
    corpus_update_minute: int = 0
    corpus_batch_size: int = 100
    corpus_embedding_batch_size: int = 50
    
    # News
    news_update_interval_hours: int = 6
    news_retention_days: int = 30
    
    # Logging
    log_level: str = "INFO"
    log_format: str = "json"
    
    # Redis
    redis_url: str = "redis://localhost:6379/0"
    
    # Embedding
    embedding_model: str = "text-embedding-3-small"
    embedding_dimension: int = 1536
    chunk_size: int = 1000
    chunk_overlap: int = 200
    
    # Security
    cors_origins: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    allowed_hosts: List[str] = ["localhost", "127.0.0.1"]
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
