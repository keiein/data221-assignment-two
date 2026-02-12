#assignment_question_eight.py

#incomplete...

import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Data_science"

response = requests.get(url)
parsed_html_document = BeautifulSoup(response.text, "html5lib") #same as question seven

clean_headings = [] #stores the clean headings
excluded_headings = ['References', 'External Links', 'See also', 'Notes'] #excluded headings to check

div = parsed_html_document.find("div", id="mw-content-text") #find div

if div:
    headings=div.find_all("h2")

    for h2 in headings:
        text = h2.get_text()
        text = text.replace("[edit]", "").strip()

        if text and text not in excluded_headings:
            headings.append(text)

    file = open('headings.txt', 'w', encoding="utf-8")
    for heading in clean_headings:
        file.write(heading + "\n")

else:
    print("div not found")
