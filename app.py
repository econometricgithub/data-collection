#importing necessary library
import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from flask import Flask, render_template,flash, request
from wtforms import Form, StringField, validators, SubmitField, SelectField
from bioinfokit.analys import get_data, stat
#Importing SQLAlcheny
from flask_sqlalchemy import SQLAlchemy
#from custom_validators import height_validator, weight_validator
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['MYSQL_HOST']='b5f3d54f1ae019'
app.config['MYSQL_USER']='us-cdbr-east-05.cleardb.net'
app.config['MYSQL_PASSWORD']='2577be25'
app.config['MYSQL_DB']='Survey Database'

mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('main_survey.html')

@app.route('/survey', methods = ['GET', 'POST'])
def survey():
    a=0
    b=[]
    c=0
    d=[]
    e=0
    f=0
    g=0
    h=0
    i=0
    j=0
    k=0
    l=0
    m=0
    n=0
    o=[]
    p=0
    q=0
    r=0
    s=0
    t=0
    u=""
    v=0
    w=0
    aa=0
    bb=0
    cc=0
    dd=0
    ee=0
    ff=0
    if request.method=='POST':
        a=request.form.get('timespending')
        b=request.form.getlist('reson_using')
        b=','.join(b)
        c = request.form.get('friend')
        d = request.form.getlist('group_membersihp')
        d = ','.join(d)
        e=request.form.get('information_use')
        f=request.form.get('SIU_1')
        g=request.form.get('SIU_2')
        h = request.form.get('SIU_3')
        i=request.form.get('entertainment_use1')
        j=request.form.get('entertainment_use2')
        k = request.form.get('political_efficacy')
        l = request.form.get('OEP_1')
        m = request.form.get('OEP_2')
        n= request.form.get('OEP_3')
        o = request.form.get('OEP_4')
        o = ','.join(o)
        p = request.form.get('OFEP_1')
        q = request.form.get('OFEP_2')
        r = request.form.get('OFEP_3')
        s = request.form.get('OFEP_4')
        t = request.form.get('gender')
        u = request.form.get('age')
        v = request.form.get('birthplace')
        w = request.form.get('education')
        aa = request.form.get('job')
        bb = request.form.get('income')
        cc = request.form.get('rural_urban1')
        dd= request.form.get('location')
        ee = request.form.get('urban2')
        ff = request.form.get('party')
        cur=mysql.connection.cursor()
        cur.execute(" INSERT INTO answers(time_spending,reasoning_using,number_friends,group_membership,informational_use,SIU_1,SIU_2,SIU_3,entertainment_use_1,entertainment_use_2,political_efficacy,OEP_1,OEP_2,OEP_3,OEP_4,OFEP_1,OFEP_2,OFEP_3,OFEP_4,gender,age,birth_place,education,job,income,rural_urban_1,location,rural_urban2,fav_party) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" , (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,aa,bb,cc,dd,ee,ff))
        mysql.connection.commit()
        cur.close()
        return render_template("successful.html", result1=a,result2=b,result3=c,result4=d,result5=e)
    return render_template('survey.html')
if __name__ == '__main__':
    app.run(debug=True)

