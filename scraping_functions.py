from bs4 import BeautifulSoup
import requests
import re

def scrape_content(url, type):
    new_data = ""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    if(type == "bbc"):
        title = soup.find("h1", class_="bbc-14gqcmb e1p3vdyi0").text if soup.find("h1", class_="bbc-14gqcmb e1p3vdyi0") else "No title"
        content =" ".join([p.get_text() for p in soup.find_all('p', class_="bbc-hhl7in e17g058b0")])
        content = re.split("Haz clic aquí para leer más historias",content)[0].strip()
        new_data+=f"{title} \n{content}" 
        
        
    else: 
        title = soup.find("h1", class_="c-detail__title").text if soup.find("h1", class_="c-detail__title") else "No title"

        paragraphs = soup.find_all("div", class_="paragraph")
        content = "" 
        for paragraph in paragraphs:    
            for child in paragraph.children:
                if child.name == "b":
                    content +=f"{child.get_text(strip=True)} "
                elif child.name is None:
                    content+=child.strip()+" "

        new_data+=f"{title} \n{content}" 
       
    return new_data
