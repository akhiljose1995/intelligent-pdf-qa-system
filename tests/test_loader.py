from core.loader import PDFLoader

def test_pdf_loader():
    loader = PDFLoader()
    docs = loader.load("data/raw/sample.pdf")

    assert len(docs) > 0
    assert docs[0].text
    assert "page" in docs[0].metadata
