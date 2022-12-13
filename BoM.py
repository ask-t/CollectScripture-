import re
import collect

print("1: 1Nephi, 2: 2Nephi, 3:Jacob, 4:Enos, 5:Jarom, 6: Omni, 7:words of Mormon, 8:Mosiah, 9:Alma, 10:Helaman, 11:3Nephi, 12:4Nephi, 13: Mormon. 14:Ether, 15:Moroni")
while True:
  try:
    name = input('choose the Name of book >>>')
    name = int(name)
    if 1 <= name <= 14:
      print('success')
      break
    else:
      continue
  except:
    continue

book = ''
match name:
  case 1:
    max = 22
    book = '1-ne'
  case 2:
    max = 33
    book = '2-ne'
  case 3:
    max = 7
    book = 'jacob'
  case 4:
    max = 1
    book = 'enos'
  case 5:
    max = 1
    book = 'jarom'
  case 6:
    max = 1
    book = 'omni'
  case 7:
    max = 1
    book = 'w-of-m'
  case 8:
    max = 29
    book = 'mosiah'
  case 9:
    max = 63
    book = 'alma'
  case 10:
    max = 16
    book = 'hel'
  case 11:
    max = 30
    book = '3-ne'
  case 12:
    max = 1
    book = '4-ne'
  case 13:
    max = 9
    book = 'morm'
  case 14:
    max = 15
    book ='ether'
  case 15:
    max = 10
    book ='moro'

while True:
  chapter = input(f'type chapter number you want (Last chapter is {max}) >>>')
  if re.match(r'\d',chapter)and 1 <=int(chapter)<=max:
    url_jpn = f'https://www.churchofjesuschrist.org/study/scriptures/bofm/{book}/{chapter}?lang=jpn'
    url_eng = f'https://www.churchofjesuschrist.org/study/scriptures/bofm/{book}/{chapter}?lang=eng'
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

text_master = f'Book of Mormon {chapter} : {collect.p(section)}\n{text_jpn}\n{text_eng}'


path_w = 'C:/Users/asktakahashi/Documents/Scripturepy/CollectScripture-/test.txt'
with open(path_w,mode ='w',encoding='utf-8')as f:
  f.write(text_master)

print('complete')

