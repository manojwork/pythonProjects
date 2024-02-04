import requests
from bs4 import BeautifulSoup as bs 
URL="https://news.ycombinator.com/"

response=requests.get(url=URL)
html_code=response.text
soup=bs(html_code,"html.parser")
news=soup.find_all(name="span",class_="titleline")
news_names=[new.a.string for new in news]
news_names.pop(8)
news_links=[new.a.get("href") for new in news]
news_links.pop(8)
points_tag=soup.find_all(name="span",class_="score")
points=[int(point.string.split()[0]) for point in points_tag]
index_ofmax=points.index(max(points))
print(f" the top news is {news_names[index_ofmax]} \n link : {news_links[index_ofmax]} \n points : {max(points)}")

print(len(news_links))
print(len(points))