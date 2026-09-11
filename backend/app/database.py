from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from neo4j import AsyncGraphDatabase, GraphDatabase
import chromadb
from app.config import settings
import logging

logger = logging.getLogger(__name__)

# PostgreSQL
engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
    echo=settings.app_debug
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def init_db():
    """Initialize database connections"""
    try:
        with engine.begin() as conn:
            from app.models import Authority, Case, Principle, JurisdictionRule, Treaty, CountryProfile, Citation, User, Conversation
            Authority.__table__.create(conn, checkfirst=True)
            Case.__table__.create(conn, checkfirst=True)
            Principle.__table__.create(conn, checkfirst=True)
            JurisdictionRule.__table__.create(conn, checkfirst=True)
            Treaty.__table__.create(conn, checkfirst=True)
            CountryProfile.__table__.create(conn, checkfirst=True)
            Citation.__table__.create(conn, checkfirst=True)
            User.__table__.create(conn, checkfirst=True)
            Conversation.__table__.create(conn, checkfirst=True)
        logger.info("PostgreSQL databases initialized")
    except Exception as e:
        logger.error(f"Error initializing PostgreSQL: {e}")

async def close_db():
    """Close database connections"""
    engine.dispose()

# Neo4j
class Neo4jDriver:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Neo4jDriver, cls).__new__(cls)
            cls._instance.driver = GraphDatabase.driver(
                settings.neo4j_url,
                auth=(settings.neo4j_user, settings.neo4j_password)
            )
        return cls._instance
    
    def get_session(self):
        return self.driver.session()
    
    def close(self):
        self.driver.close()

neo4j_driver = Neo4jDriver()

# ChromaDB
class ChromaDBClient:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChromaDBClient, cls).__new__(cls)
            cls._instance.client = chromadb.HttpClient(
                host=settings.chroma_host,
                port=settings.chroma_port
            )
            try:
                cls._instance.collection = cls._instance.client.get_or_create_collection(
                    name="legal_corpus",
                    metadata={"hnsw:space": "cosine"}
                )
                logger.info("ChromaDB collection initialized")
            except Exception as e:
                logger.error(f"Error initializing ChromaDB: {e}")
        return cls._instance
    
    def get_collection(self):
        return self.collection

chroma_client = ChromaDBClient()
