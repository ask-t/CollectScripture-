from flask import Flask
from flask import render_template,request,redirect
import DC
# import NewTestament as New
# import OldTestament as Old
# import BoM
import ScriptureList
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
                index = num
                max = author_list[num][1]
                link = author_list[num][2]
                break
            num += 1
        return render_template('ot_select.html',author = author, max = max, link =link )

@app.route("/nt",methods = ['GET','POST'])
def nt():
    with app.app_context():
        author_list = ScriptureList.new_dict
        return render_template('nt.html',author_list = author_list)

@app.route("/nt/<author>",methods = ['GET','POST'])
def nt_author(author):
    with app.app_context():
        author_list = ScriptureList.new_list
        num = 0
        for i in author_list:
            if i[0] == author:
                index = num
                max = author_list[num][1]
                link = author_list[num][2]
                break
            num += 1
        return render_template('nt_select.html',author = author, max = max, link =link )

@app.route("/bofm",methods = ['GET','POST'])
def bofm():
    with app.app_context():
        author_list = ScriptureList.BoM_dict
        return render_template('BoM.html',author_list = author_list)

@app.route("/bofm/<author>",methods = ['GET','POST'])
def BoM_author(author):
    with app.app_context():
        author_list = ScriptureList.BoM_list
        num = 0
        for i in author_list:
            if i[0] == author:
                index = num
                max = author_list[num][1]
                link = author_list[num][2]
                break
            num += 1
        return render_template('BoM_select.html',author = author, max = max, link =link )

@app.route("/dc",methods = ['GET','POST'])
def dc():
    with app.app_context():
        if request.method == 'POST':
            chapter = request.form.get('chapter')
            verseF = request.form.get('from')
            verseT = request.form.get('to')
            master = DC.main(chapter,verseF,verseT)
            text = master[0]
            text1 = master[1]
            text2 = master[2]
            return render_template('dc.html',text = text, text1 = text1, text2 = text2)
        else:
            return render_template('dc.html')






@app.route ("/sample",methods=['GET','POST'])
def sample():
    with app.app_context():
        return render_template('sample.html')

@app.route ("/test",methods=['GET','POST'])
def test():
    with app.app_context():
        book = request.form.get('book')
        return render_template('test.html', book = book)

# def index():
#     with app.app_context():
#         if request.method == 'POST':
#             book = request.form.get('book')
#             chapter = request.form.get('chapter')
#             verseF = request.form.get('from')
#             verseT = request.form.get('to')
#             if chapter != '' and verseF != '' and verseT != '':
#                 master = DC.main(chapter,verseF,verseT)
#                 if book == 'Old':
#                     master = Old.main(chapter,verseF,verseT)
#                 elif book == 'New':
#                     master = New.main(chapter,verseF,verseT)
#                 elif book == 'B&M':
#                     master = BoM.main(chapter,verseF,verseT)
#                 elif book == 'D&C':
#                     master = DC.main(chapter,verseF,verseT)
#                 # elif book == 'Pearl':
#                 #     master = Pearl.main(chapter,verseF,verseT)
#                 else:
#                     return  render_template('index.html')
#                 text = master[0]
#                 text1 = master[1]
#                 text2 = master[2]
#             else:
#                 text =''
#                 text1 =''
#                 text2 = ''
#             return  render_template('index.html',text =text,text1=text1,text2=text2,list_O=list_O,list_N = list_N,list_B = list_B)
#         else:
#             return  render_template('index.html',list_O = list_O,list_N = list_N,list_B = list_B)


#  author = request.form.get('author')
#             if author != '':
#                 chapter_max = str(author_list[author])
#                 return render_template('index3.html',chapter_max = chapter_max )


