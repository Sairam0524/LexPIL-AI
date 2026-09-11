from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Citation(Base):
    __tablename__ = "citations"
    
    id = Column(Integer, primary_key=True, index=True)
    citing_authority_id = Column(Integer, nullable=False, index=True)
    cited_authority_id = Column(Integer, nullable=False, index=True)
    citation_type = Column(String(50), nullable=False)
    context = Column(String(500), nullable=True)
    page_reference = Column(String(50), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
