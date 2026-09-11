from sqlalchemy import Column, String, Text, DateTime, Integer
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class CountryProfile(Base):
    __tablename__ = "country_profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    country_name = Column(String(100), nullable=False, unique=True, index=True)
    country_code = Column(String(3), nullable=False, unique=True)
    jurisdiction_rules = Column(Text, nullable=True)
    choice_of_law_rules = Column(Text, nullable=True)
    recognition_policy = Column(Text, nullable=True)
    enforcement_procedures = Column(Text, nullable=True)
    treaties_ratified = Column(Text, nullable=True)
    key_statutes = Column(Text, nullable=True)
    court_system = Column(Text, nullable=True)
    legal_system = Column(String(100), nullable=True)
    pil_expertise = Column(Text, nullable=True)
    major_cases = Column(Text, nullable=True)
    enforcement_mechanisms = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
