import re
import collect

print("1: Matthew, 2: Mark, 3: Luke, 4: John, 5: Acts, 6: Romans, 7: 1Corinthians, 8: Chorinthians, 9: Galatians, 10: Ephesians, 11: Philippians, 12: Colossians, 13: 1Thessalonians, 14:2Thessalonians, 15: 1Timothy ")
print('16: 2Thimothy, 17: Titus, 18: Philemon, 19: Hebrews, 20: James, 21: 1 Peter, 22: 2Peter, 23: 1John, 24: 2John, 25: 3John, 26: Jude, 27: Revelation')

while True:
    try:
        name = input('choose the Name of Book>>>')
        name = int(name)
        if 1 <= name <= 27:
            print('Success')
            break
        else:
            continue
    except:
        continue

match name:
    case 1:
        max = 28
        book = 'matt'
    case 2:
        max = 16
        book = 'mark'
    case 3:
        max = 24
        book = 'luke'
    case 4:
        max = 21
        book = 'john'
    case 5:
        max = 28
        book = 'acts'
    case 6:
        max = 16
        book = 'rom'
    case 7:
        max = 16
        book = '1-cor'
    case 8:
        max = 13
        book = '2-cor'
    case 9:
        max = 6
        book = 'gal'
    case 10:
        max = 6
        book = 'eph'
    case 11:
        max = 4
        book = 'philip'
    case 12:
        max = 4
        book = 'col'
    case 13:
        max = 5
        book = '1-thes'
    case 14:
        max = 3
        book = '2-thes'
    case 15:
        max = 6
        book = '1-tim'
    case 16:
        max = 4
        book = '2-tim'
    case 17:
        max = 3
        book = 'titus'
    case 18:
        max= 1
        book = 'philem'
    case 19:
        max = 13
        book ='heb'
    case 20:
        max = 5
        book = 'james'
    case 21:
        max = 5
        book = '1-pet'
    case 22:
        max = 3
        book = '2-pet'
    case 23:
        max = 5
        book = '1-jn'
    case 24:
        max = 1
        book = '2-jn'
    case 25:
        max = 1
        book = '3-jn'
    case 26:
        max = 1
        book = 'jude'
    case 27:
        max = 22
        book = 'rev'

while True:
    chapter = input(f'type chapter number you want (Last chapter is {max})>>>')
    if re.match(r'\d',chapter) and 1<= int(chapter) <= max:
        url_jpn = f'https://www.churchofjesuschrist.org/study/scriptures/nt/{book}/{chapter}?lang=jpn'
        url_eng = f'https://www.churchofjesuschrist.org/study/scriptures/nt/{book}/{chapter}?lang=eng'
        break
    else: print('error! type chapter number again')
print(url_eng)
print(url_jpn)
print('fill out verse number. When you have done, write "over" at the end.')
section = list(iter(input,'over'))

list_id = []
for i in section:
    list_id.append('p'+i)

text_jpn = collect.Scripture_japanese(url_jpn,list_id)
text_eng = collect.scripture(url_eng,list_id)

text_master = f'New Testament {book} {chapter} : {collect.p(section)}\n{text_jpn}\n{text_eng}'

path_w = 'C:/Users/asktakahashi/Documents/Scripturepy/CollectScripture-/test.txt'
with open(path_w,mode ='w',encoding='utf-8')as f:
  f.write(text_master)

print('complete')