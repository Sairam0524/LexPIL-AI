import logging
from typing import List
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config import settings

logger = logging.getLogger(__name__)

class DocumentChunker:
    """Chunks legal documents for embedding"""
    
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap,
            separators=["\n\n", "\n", " ", ""]
        )
    
    def chunk_document(self, content: str) -> List[str]:
        """Chunk a document"""
        try:
            chunks = self.splitter.split_text(content)
            logger.info(f"Created {len(chunks)} chunks")
            return chunks
        except Exception as e:
            logger.error(f"Error chunking document: {e}")
            return []
    
    def chunk_documents(self, contents: List[str]) -> List[str]:
        """Chunk multiple documents"""
        all_chunks = []
        try:
            for content in contents:
                chunks = self.chunk_document(content)
                all_chunks.extend(chunks)
            logger.info(f"Created {len(all_chunks)} total chunks")
        except Exception as e:
            logger.error(f"Error chunking documents: {e}")
        
        return all_chunks
