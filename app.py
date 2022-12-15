from flask import Flask
from flask import render_template,request,redirect
import DC
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    with app.app_context():
        if request.method == 'POST':
            chapter = request.form.get('chapter')
            verseF = request.form.get('from')
            verseT = request.form.get('to')
            text = DC.main(chapter,verseF,verseT)
            return  render_template('index.html',text =text)
        else:
             return  render_template('index.html')



