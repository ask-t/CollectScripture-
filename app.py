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
            master = DC.main(chapter,verseF,verseT)
            text = master[0]
            text1 = master[1]
            text2 = master[2]
            return  render_template('index.html',text =text,text1=text1,text2=text2)
        else:
             return  render_template('index.html')



