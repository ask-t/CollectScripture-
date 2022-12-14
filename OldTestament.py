import re
import collect

print('1: Genesis, 2: Exodus, 3: Leviticus, 4: Numbers, 5: Deuteronomy, 6: Joshua, 7: Judges, 8: Ruth, 9: 1 Samuel, 10: 2 Samuel, 11: 1 King, 12: 2 King, 13: 1 Chronicles, 14: 2 Chronicles, 15: Ezra, 16: Nehemiah, 17: Esther, 18: Job, 19: Psalms, 20: Proverbs, 21: Ecclesiastes, 22: Song of Solomon, 23: Isaiah, 24: Jeremiah, 25: Lamentations, 26: Ezekiel, 27: Daniel, 28: Hosea, 29: Joel, 30: Amos, 31; Obadiah, 32: Jonah, 33: Micah, 34: Nahum, 35: Habakkuk, 36: Zephaniah, 37: Haggai, 38: Zechariah, 39:Malachi')
while True:
    try:
        name = input('choose the Name of Book>>> ')
        name = int(name)
        if 1 <= name <= 39:
            print('Success')
            break
        else:
            continue
    except:
        continue

match name:
    case 1:
        max = 50
        book = 'gen'
    case 2:
        max = 40
        book = 'ex'
    case 3:
        max = 27
        book = 'lev'
    case 4:
        max = 36
        book = 'num'
    case 5:
        max = 34
        book = 'deut'
    case 6:
        max = 24
        book = 'josh'
    case 7:
        max = 21
        book ='judg'
    case 8:
        max = 4
        book = 'ruth'
    case 9:
        max = 31
        book = '1-sam'
    case 10:
        max = 24
        book = '2-sam'
    case 11:
        max = 22
        book = '1-kgs'
    case 12:
        max = 25
        book = '2-kgs'
    case 13:
        max = 29
        book ='1-chr'
    case 14:
        max = 36
        book = '2-chr'
    case 15:
        max = 10
        book = 'ezra'
    case 16:
        max = 13
        book = 'neh'
    case 17:
        max = 10
        book = 'esth'
    case 18:
        max = 42
        book = 'job'
    case 19:
        max = 150
        book = 'ps'
    case 20:
        max = 31
        book = 'prov'
    case 21:
        max = 12
        book = 'eccl'
    case 22:
        max = 8
        book = 'song'
    case 23:
        max = 66
        book = 'isa'
    case 24:
        max = 52
        book = 'jer'
    case 25:
        max = 5
        book = 'lam'
    case 26:
        max = 48
        book = 'ezek'
    case 27:
        max = 12
        book ='dan'
    case 28:
        max = 14
        book ='hosea'
    case 29:
        max = 3
        book = 'joel'
    case 30:
        max = 9
        book = 'amos'
    case 31:
        max =1
        book = 'obad'
    case 32:
        max = 4
        book = 'jonah'
    case 33:
        max = 7
        book = 'micah'
    case 34:
        max = 3
        book = 'nahum'
    case 35:
        max = 3
        book = 'hab'
    case 36:
        max = 3
        book = 'zeph'
    case 37:
        max = 2
        book = 'hag'
    case 38:
        max = 14
        book = 'zech'
    case 39:
        max = 4
        book = 'mal'

while True:
  chapter = input(f'type chapter number you want (Last chapter is {max}) >>>')
  if re.match(r'\d',chapter)and 1 <=int(chapter)<=max:
    url_jpn = f'https://www.churchofjesuschrist.org/study/scriptures/ot/{book}/{chapter}?lang=jpn'
    url_eng = f'https://www.churchofjesuschrist.org/study/scriptures/ot/{book}/{chapter}?lang=eng'
    break
  else: print('error! type chapter number again')
print(url_eng)
print( url_jpn)
print('fill out verse number.When you have done, write "over" at the end.')
section = list(iter(input, 'over'))

list_id = []
for i in section:
    list_id.append('p'+i)

text_jpn = collect.Scripture_japanese(url_jpn,list_id )
text_eng = collect.scripture(url_eng,list_id )

text_master = f'Old Testament {book} {chapter} : {collect.p(section)}\n{text_jpn}\n{text_eng}'


path_w = 'C:/Users/asktakahashi/Documents/Scripturepy/CollectScripture-/test.txt'
with open(path_w,mode ='w',encoding='utf-8')as f:
  f.write(text_master)

print('complete')
