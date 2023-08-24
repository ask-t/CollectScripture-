from flask import Flask
from flask import render_template,request,redirect
import DC,NewTestament,OldTestament,BoM,ScriptureList
import pgp

author_list = book = chapter = verseF = verseT = author = ''
app = Flask(__name__)
@app.route("/",methods=['GET','POST'])
def index():
    with app.app_context():
        return render_template('index.html')

@app.route("/ot",methods = ['GET','POST'])
def ot():
    with app.app_context():
        author_list = ScriptureList.old_list
        return render_template('ot.html',author_list = author_list)

@app.route("/ot/<author>",methods = ['GET','POST'])
def ot_author(author):
    with app.app_context():
        author_list = ScriptureList.old_list
        num = 0
        for i in author_list:
            if i[0] == author:
                max = author_list[num][1]
                link = author_list[num][2]
                break
            num += 1
        if request.method == 'POST':
            link = request.form.get('link')
            chapter = request.form.get('chapter')
            verseF = request.form.get('from')
            verseT = request.form.get('to')
            if verseF <=verseT:
                master = OldTestament.main(link,chapter,verseF,verseT)
            else:
                master = ['Please fix the chapter numbers','','']
            text = master[0]
            text1 = master[1]
            text2 = master[2]
            return render_template('ot_select.html',author = author, max = max, link =link ,text = text, text1 = text1, text2 = text2)
        else:
            return render_template('ot_select.html',author = author, max = max, link =link )

@app.route("/nt",methods = ['GET','POST'])
def nt():
    with app.app_context():
        author_list = ScriptureList.new_list
        return render_template('nt.html',author_list = author_list)

@app.route("/nt/<author>",methods = ['GET','POST'])
def nt_author(author):
    with app.app_context():
        author_list = ScriptureList.new_list
        num = 0
        for i in author_list:
            if i[0] == author:
                max = author_list[num][1]
                link = author_list[num][2]
                break
            num += 1
        if request.method == 'POST':
            link = request.form.get('link')
            chapter = request.form.get('chapter')
            verseF = request.form.get('from')
            verseT = request.form.get('to')
            if verseF <=verseT:
                master = NewTestament.main(link,chapter,verseF,verseT)
            else:
                master = ['Please fix the chapter numbers','','']
            text = master[0]
            text1 = master[1]
            text2 = master[2]
            return render_template('nt_select.html',author = author, max = max, link =link ,text = text, text1 = text1, text2 = text2)
        else:
            return render_template('nt_select.html',author = author, max = max, link =link )

@app.route("/bofm",methods = ['GET','POST'])
def bofm():
    with app.app_context():
        author_list = ScriptureList.BoM_list
        return render_template('BoM.html',author_list = author_list)

@app.route("/bofm/<author>",methods = ['GET','POST'])
def bofm_author(author):
    with app.app_context():
        author_list = ScriptureList.BoM_list
        num = 0
        for i in author_list:
            if i[0] == author:
                max = author_list[num][1]
                link = author_list[num][2]
                break
            num += 1
        if request.method == 'POST':
            link = request.form.get('link')
            chapter = request.form.get('chapter')
            verseF = request.form.get('from')
            verseT = request.form.get('to')
            if verseF <=verseT:
                master = BoM.main(link,chapter,verseF,verseT)
            else:
                master = ['Please fix the chapter numbers','','']
            text = master[0]
            text1 = master[1]
            text2 = master[2]
            return render_template('BoM_select.html',author = author, max = max, link =link ,text = text, text1 = text1, text2 = text2)
        else:
            return render_template('BoM_select.html',author = author, max = max, link =link )


@app.route("/dc",methods = ['GET','POST'])
def dc():
    with app.app_context():
        if request.method == 'POST':
            chapter = request.form.get('chapter')
            verseF = request.form.get('from')
            verseT = request.form.get('to')
            if verseF <=verseT:
                master = DC.main(chapter,verseF,verseT)
            else:
                master = ['Please fix the chapter numbers','','']
            text = master[0]
            text1 = master[1]
            text2 = master[2]
            return render_template('dc.html',text = text, text1 = text1, text2 = text2)
        else:
            return render_template('dc.html')

@app.route("/pgp",methods = ['GET','POST'])
def pearl():
    with app.app_context():
        author_list = ScriptureList.pgp_list
        return render_template('pgp.html',author_list = author_list)

@app.route("/pgp/<author>",methods = ['GET','POST'])
def pgp_author(author):
    with app.app_context():
        author_list = ScriptureList.pgp_list
        num = 0
        for i in author_list:
            if i[0] == author:
                max = author_list[num][1]
                link = author_list[num][2]
                break
            num += 1
        if request.method == 'POST':
            link = request.form.get('link')
            chapter = request.form.get('chapter')
            verseF = request.form.get('from')
            verseT = request.form.get('to')
            if verseF <=verseT:
                master = pgp.main(link,chapter,verseF,verseT)
            else:
                master = ['Please fix the chapter numbers','','']
            text = master[0]
            text1 = master[1]
            text2 = master[2]
            return render_template('BoM_select.html',author = author, max = max, link =link ,text = text, text1 = text1, text2 = text2)
        else:
            return render_template('BoM_select.html',author = author, max = max, link =link )

if __name__ == '__main__':
    app.run(debug=True)

