from bs4 import BeautifulSoup
import requests

url = 'https://za.indeed.com/jobs?q=junior+developer+no+experience&l=&vjk=3151a61c2d85fb0e'
page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml').text
print(soup)
