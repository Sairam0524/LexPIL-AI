import logging
from typing import List, Dict, Any
import openai
from app.config import settings
from app.database import chroma_client

logger = logging.getLogger(__name__)

class EmbeddingGenerator:
    """Generates embeddings for legal documents"""
    
    def __init__(self):
        self.client = openai.OpenAI(
            api_key=settings.openai_api_key,
            base_url=settings.openai_base_url
        )
        self.model = settings.embedding_model
    
    async def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding for text"""
        try:
            response = self.client.embeddings.create(
                input=text,
                model=self.model
            )
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"Error generating embedding: {e}")
            return []
    
    async def generate_batch_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for batch of texts"""
        embeddings = []
        try:
            response = self.client.embeddings.create(
                input=texts,
                model=self.model
            )
            embeddings = [item.embedding for item in response.data]
            logger.info(f"Generated embeddings for {len(texts)} texts")
        except Exception as e:
            logger.error(f"Error generating batch embeddings: {e}")
        
        return embeddings
    
    async def store_in_chroma(self, documents: List[Dict[str, Any]], embeddings: List[List[float]]) -> None:
        """Store documents and embeddings in ChromaDB"""
        try:
            collection = chroma_client.get_collection()
            
            ids = [doc.get('id', str(i)) for i, doc in enumerate(documents)]
            texts = [doc.get('content', '') for doc in documents]
            metadatas = [doc.get('metadata', {}) for doc in documents]
            
            collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=texts,
                metadatas=metadatas
            )
            
            logger.info(f"Stored {len(documents)} documents in ChromaDB")
        except Exception as e:
            logger.error(f"Error storing in ChromaDB: {e}")
