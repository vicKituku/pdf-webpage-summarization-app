from langchain_community.document_loaders import PyPDFLoader
from transformers import pipeline
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

# load and summarize pdf
def pdf_summarizer(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    content = "\n".join([page.page_content for page in pages])
    output = summarizer(content, max_length=1000, min_length=30, do_sample = False)
    return(output[0]['summary_text'])
