from langchain_community.document_loaders import PyPDFLoader
from transformers import pipeline
from bs4 import BeautifulSoup
import requests
summarizer = pipeline("summarization", model="Falconsai/text_summarization")

def url_summarizer(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    text_content = soup.get_text()
    output = summarizer(text_content,max_length = 1000, min_length = 30, do_sample = False)
    return (output[0]['summary_text'])
