#assignment_question_seven.py

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

response = requests.get(url)
parsed_html_document = BeautifulSoup(response.text, "html5lib") #from slides

if parsed_html_document.title:
    print(f"Title: {parsed_html_document.title.string}")
    div = parsed_html_document.find("div", id="mw-content-text") #finding div
    if div:
        paragraphs = div.find_all("p")

        for paragraph in paragraphs: #getting paragraph with more than 50 characters
            text = paragraph.get_text().strip() #without whitespace
            if len(text) >= 50:
                print(text)
                break


