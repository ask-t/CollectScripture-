from flask import Flask
from flask import render_template,request,redirect
import collect as dc
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    return  render_template('index.html')



