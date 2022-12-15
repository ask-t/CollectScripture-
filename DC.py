
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
  if len(list_id) == 1:
    text_master = f'Doctrine and Covenants Chapter {chapter} :{f}\n{text_jpn}\n{text_eng}'
  else:
     text_master = f'Doctrine and Covenants Chapter {chapter} :{collect.p(section)}\n{text_jpn}\n{text_eng}'
  return (text_master)

