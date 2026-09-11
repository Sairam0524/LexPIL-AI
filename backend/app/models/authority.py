from sqlalchemy import Column, String, Text, DateTime, Integer, Enum
from sqlalchemy.orm import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class AuthorityType(str, enum.Enum):
    CASE = "case"
    STATUTE = "statute"
    TREATY = "treaty"
    REGULATION = "regulation"
    DOCTRINE = "doctrine"

class Authority(Base):
    __tablename__ = "authorities"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False, index=True)
    authority_type = Column(Enum(AuthorityType), nullable=False)
    jurisdiction = Column(String(100), nullable=False, index=True)
    country = Column(String(100), nullable=False, index=True)
    year = Column(Integer, nullable=True)
    citation = Column(String(200), unique=True, index=True)
    source_url = Column(String(500), nullable=True)
    content = Column(Text, nullable=False)
    summary = Column(Text, nullable=True)
    keywords = Column(String(1000), nullable=True)
    embedding_id = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_indexed = Column(DateTime, nullable=True)
