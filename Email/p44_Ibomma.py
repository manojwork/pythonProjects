from bs4 import BeautifulSoup as bs
import requests
import imdb
import smtplib
ia=imdb.IMDb()
def get_rating(movie):
    movies=ia.search_movie(movie)
    if movies:
        mov=movies[0]
        ia.update(mov)
        if "rating" in mov.keys():
            return mov['rating']
            

def sendmail(temp):
    with smtplib.SMTP("smtp.gmail.com",port=587) as connect:
        connect.starttls()
        connect.login(user="manojbabu.mandhala@gmail.com",password="bvydresbbflrglwb")
        connect.sendmail(from_addr="manojbabu.mandhala@gmail.com",to_addrs="manojmass421@gmail.com",msg=f"subject:IBOMMA movie Rating\n\n{temp}")
    
response=requests.get(url="https://ww2.ibomma.boo/telugu-movies/")
data=response.text
soup=bs(data,"html.parser")
movies_details=soup.find_all("h2",class_="entry-title")
movies_name=[movie.a.string for movie in movies_details]
movies_dict={ movie.a.string:[get_rating(movie.a.string),movie.a.get("href")] for movie in movies_details}
temp=""
for key,values in movies_dict.items():
        temp+=f"{key} : {values[0]} \nLink:{values[1]}\n\n"
sendmail(temp)
