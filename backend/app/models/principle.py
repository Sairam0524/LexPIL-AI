from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Principle(Base):
    __tablename__ = "principles"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(300), nullable=False, unique=True, index=True)
    category = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=False)
    pil_domain = Column(String(100), nullable=False)
    supporting_authorities = Column(Text, nullable=True)
    exceptions = Column(Text, nullable=True)
    modern_applications = Column(Text, nullable=True)
    jurisdiction_relevance = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
