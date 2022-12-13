import re
import collect

def main():
# In[5]:
  while True:
    chapter = input('type chapter number you want:')
    if re.match(r'\d',chapter)and int(chapter)<139:
      url_jpn = 'https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/'+chapter+'?lang=jpn'
      url_eng = 'https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/'+chapter+'?lang=eng'
      break
    else: print('error! type again chapter number')


  # In[6]:
  print(url_jpn,url_eng)
  # ## どの節が必要かを入力、そして出力できるようにする。

  # In[7]:
  print('fill out section number.When you have done, write "over" at the end.')
  section = list(iter(input, 'over'))
  # In[10]:
  list_id = []
  for i in section:
      list_id.append('p'+i)
  # In[11]:
  text_jpn = collect.Scripture_japanese(url_jpn,list_id)
  # In[12]:
  text_eng = collect.scripture(url_eng,list_id)
  # In[13]:
  text_master = '教義と聖約'+ chapter + ':'+ collect.p(section) +'\n'+text_jpn +'\n'+ text_eng
  # In[14]:
  path_w = '/Users/ask/Documents/Programing/flask/scripture/test.txt'
  # In[15]:
  with open(path_w, mode='w') as f:
      f.write(text_master)
  print('完了')
  # In[ ]:

main()