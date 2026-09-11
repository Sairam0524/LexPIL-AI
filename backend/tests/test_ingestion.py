import pytest
from app.ingestion.content_parser import ContentParser
from app.ingestion.citation_extractor import CitationExtractor
from app.ingestion.document_chunker import DocumentChunker

def test_content_parser():
    html = "<html><body><h1>Test</h1><p>Content here</p></body></html>"
    result = ContentParser.parse_html(html)
    assert "content" in result

def test_citation_extraction():
    text = "In 2023 SCC Online 1234, the court held that..."
    citations = CitationExtractor.extract_citations(text)
    assert isinstance(citations, list)

def test_document_chunker():
    chunker = DocumentChunker()
    content = "This is a test. " * 100
    chunks = chunker.chunk_document(content)
    assert len(chunks) > 0
