from sqlalchemy import Column, String, Text, DateTime, Integer, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Case(Base):
    __tablename__ = "cases"
    
    id = Column(Integer, primary_key=True, index=True)
    case_name = Column(String(500), nullable=False, index=True)
    year = Column(Integer, nullable=False, index=True)
    court = Column(String(200), nullable=False, index=True)
    country = Column(String(100), nullable=False, index=True)
    citation = Column(String(200), unique=True, index=True)
    parties = Column(String(500), nullable=True)
    headnote = Column(Text, nullable=True)
    judgment = Column(Text, nullable=False)
    ratio = Column(Text, nullable=True)
    obiter = Column(Text, nullable=True)
    pil_relevance = Column(Text, nullable=True)
    jurisdiction_issue = Column(String(255), nullable=True)
    choice_of_law_issue = Column(String(255), nullable=True)
    recognition_enforcement = Column(String(255), nullable=True)
    source_url = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
