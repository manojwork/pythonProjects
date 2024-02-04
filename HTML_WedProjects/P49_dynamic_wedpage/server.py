from flask import Flask,render_template
import requests
from post import post
app=Flask(__name__)

response=requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
d=response.json()
post_objects=[]
for pos in d:
    postobj=post(pos["id"],pos["title"],pos["subtitle"],pos["body"])
    post_objects.append(postobj)
@app.route('/')
def home():
    return render_template('index.html',data=d)

@app.route('/blog/<num>')
def blogf(num):
    dat=None
    for i in post_objects:
        if int(i.id) == int(num):
            dat=i
            
    return render_template('blog.html',da=dat)


if __name__=='__main__' :
    app.run(debug=True)