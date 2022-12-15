
import collect

def main(chapter,f,t):
  chapter = str(chapter)
  url_jpn = f'https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/{chapter}?lang=jpn'
  url_eng = f'https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/{chapter}?lang=eng'
  # ## どの節が必要かを入力、そして出力できるようにする。

  section = [str(i) for i in range(int(f),int(t)+1)]
  list_id = ['p'+ i for i in section]
  text_jpn = collect.Scripture_japanese(url_jpn,list_id)
  text_eng = collect.scripture(url_eng,list_id)
  text_jpn2 =''
  text_eng2 =''
  for i in text_jpn:
    if i in '[]':
      continue
    else:
      text_jpn2 = text_jpn2 + i
  for i in text_eng:
    if i in '[]':
      continue
    else:
      text_eng2 = text_eng2 + i
  print(text_jpn2)
  print(text_eng2)

  if len(list_id) == 1:
    text_master = f'Doctrine and Covenants Chapter {chapter} :{f}'
  else:
     text_master = f'Doctrine and Covenants Chapter {chapter} :{collect.p(section)}'

  print('complete')
  return (text_master,text_jpn2,text_eng2)
