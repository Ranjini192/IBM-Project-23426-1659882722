from cloudant.client import Cloudant

#creating the Cloudant Database 
client = Cloudant.iam("1c6f917d-87ac-491b-90a0-6e3ae5b5daca-bluemix","tYJcUyVJYs3WrxF_1absTN4RXrbdQ_RDWBRUy9BX-28c",connect=True)
database = client.create_database("bath4_database")

from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/afterLogin',methods=['POST','GET'])
def afterlogin():
    user = request.form['_id']
    passw = request.form['psw']
    print(user,passw)

    query = {'_id':{'$eq':user}}

    docs = database.get_query_result(query)
    print(docs)
    print(len(docs.all()))

    if(len(docs.all())==0):
        return render_template('login.html',pred='The username is not found')
    else:
        if((user==docs[0][0]['_id'] and passw==docs[0][0]['psw'])):
            return redirect(url_for('prediction'))
        else:
            print('Invalid User')
    


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/afterRegister',methods=['POST'])
def afterregister():
    x = [x for x in request.form.values()]
    print(x)
    data = {
        '_id':x[1],
        'name':x[0],
        'psw' : x[2]
    }
    print(data)

    query = {'_id':{'$eq' : data['_id']}}
    docs = database.get_query_result(query)

    if(len(docs.all())==0):
        url = database.create_document(data)
        return render_template('register.html', result="Registration is Successfully Completed")
    else:
        return render_template("register.html", result="You are already a member!")


if (__name__ == '__main__'):
    app.run(debug=True) 