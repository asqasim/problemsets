from bs4 import BeautifulSoup
import requests

url = "https://medium.com/@qasim.datadev"

response = requests.get(url)
content = response.text

soap = BeautifulSoup(content, "html.parser")

print(type(soap))

links = soap.find_all("a")


for link in links: print(link)
