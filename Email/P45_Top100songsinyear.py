import requests
from bs4 import BeautifulSoup as bs
year =input(" enter the year : ") 
link=f"https://www.billboard.com/charts/hot-100/{year}-08-12"
response=requests.get(url=link)
soup=bs(response.text,"html.parser")
song_details=soup.select("ul li ul li h3")
songs=[song.string.strip() for song in song_details]
print(songs)