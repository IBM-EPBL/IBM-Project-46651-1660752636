from flask import Flask,render_template,request,redirect,url_for,session
import re
import firebase_admin
from firebase_admin import credentials,db

app=Flask(__name__)

cred = credentials.Certificate("smart-farmer-fa22a-firebase-adminsdk-mxrsq-fed74091ed.json")
default_app = firebase_admin.initialize_app(cred, {'databaseURL':'https://smart-farmer-fa22a-default-rtdb.firebaseio.com/'})
ref = db.reference("Smart_Farmers/")
userid_list = ref.get()

@app.route('/')
def home():
    return render_template('LoginPage.html')


@app.route('/loginpage',methods=['GET','POST'])
def loginpage():
    global userid
    msg=''

    if request.method == 'POST':
        userid=request.form['userid']
        password=request.form['password']
        
        for key, value in userid_list.items():
            if key == userid:
                if value == password:
                    print("login success")
                    return redirect('http://127.0.0.1:1880/ui')
                else:
                    print(password)
            else:
                print(userid)
                print(key)
                msg ="Invalid UserName and Password"
        return render_template('LoginPage.html',msg=msg)