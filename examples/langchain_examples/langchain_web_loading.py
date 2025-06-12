import bs4
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    "https://lt.wikipedia.org/wiki/Anyk%C5%A1%C4%8Diai",
    bs_kwargs={
        "parse_only": bs4.SoupStrainer(id="mw-content-text")
    }
)

docs = loader.load()
print(docs[0].page_content)