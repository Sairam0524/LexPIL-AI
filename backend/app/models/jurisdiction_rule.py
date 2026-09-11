from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class JurisdictionRule(Base):
    __tablename__ = "jurisdiction_rules"
    
    id = Column(Integer, primary_key=True, index=True)
    country = Column(String(100), nullable=False, index=True)
    rule_type = Column(String(100), nullable=False)
    rule_name = Column(String(300), nullable=False)
    description = Column(Text, nullable=False)
    statutory_basis = Column(String(300), nullable=True)
    case_authority = Column(String(300), nullable=True)
    conditions = Column(Text, nullable=True)
    exceptions = Column(Text, nullable=True)
    cross_references = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
