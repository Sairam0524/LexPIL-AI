from sqlalchemy import Column, String, Text, DateTime, Integer, Date
from sqlalchemy.orm import declarative_base
from datetime import datetime, date

Base = declarative_base()

class Treaty(Base):
    __tablename__ = "treaties"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(500), nullable=False, unique=True, index=True)
    treaty_type = Column(String(100), nullable=False)
    year_adopted = Column(Integer, nullable=False)
    date_adopted = Column(Date, nullable=True)
    date_entered_force = Column(Date, nullable=True)
    jurisdiction = Column(String(100), nullable=True)
    parties = Column(Text, nullable=True)
    summary = Column(Text, nullable=False)
    full_text = Column(Text, nullable=True)
    key_provisions = Column(Text, nullable=True)
    pil_relevance = Column(Text, nullable=True)
    uncitral_link = Column(String(500), nullable=True)
    un_link = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
