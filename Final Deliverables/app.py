from cloudant.client import Cloudant

#creating the Cloudant Database 
client = Cloudant.iam("1c6f917d-87ac-491b-90a0-6e3ae5b5daca-bluemix","tYJcUyVJYs3WrxF_1absTN4RXrbdQ_RDWBRUy9BX-28c",connect=True)
database = client.create_database("bath4_database")

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

if (__name__ == '__main__'):
    app.run(debug=True) 