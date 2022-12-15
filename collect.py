#!/usr/bin/env python
# coding: utf-8

# In[1]:
from bs4 import BeautifulSoup
import requests
# In[2]:

def p(list1) :
    list2 = list1[0],list1[-1]
    return str(list2).replace('[','').replace(']','').replace("'","").replace(',','-')
# In[16]:
def scripture(url_eng,list_id):
  a =['<sup class="marker">a</sup>',
 '<sup class="marker">b</sup>',
 '<sup class="marker">c</sup>',
 '<sup class="marker">d</sup>',
 '<sup class="marker">e</sup>',
 '<sup class="marker">f</sup>',
 '<sup class="marker">g</sup>',
 '<sup class="marker">h</sup>']
  response =requests.get(url = url_eng).text
  parse_html = BeautifulSoup(response,'html.parser')
  url_lists = parse_html.find_all(id = list_id)
  html = str(url_lists)
  for i in a:
    html = html.replace(i, "")

  parse_html2 = BeautifulSoup(html,'html.parser')
  text = parse_html2.text
  text2 = text.replace(',',"")

  return(text2)


# In[4]:
def Scripture_japanese(url_jpn,list_id ):
  b =['<sup class="marker">①</sup>',
 '<sup class="marker">②</sup>',
 '<sup class="marker">③</sup>',
 '<sup class="marker">⑤</sup>',
 '<sup class="marker">④</sup>',
 '<sup class="marker">⑥</sup>',
 '<sup class="marker">⑦</sup>',
 '<sup class="marker">⑧</sup>',
 '<sup class="marker">⑨</sup>']
  response =requests.get(url_jpn)
  response.encoding = response.apparent_encoding
  html = response.text
  parse_html = BeautifulSoup(html,'html.parser')
  html_a = parse_html.find_all(id= list_id)
  html_a = str(html_a)
  sup = parse_html.find_all('rt')

  a = []
  for i in sup:
    a.append(str(i))

  for i in a:
    html_a = html_a.replace(i, "")

  for i in b:
    html_a = html_a.replace(i, "")

  parse_html2 = BeautifulSoup(html_a,'html.parser')
  text = parse_html2.text
  text2 = text.replace(',',"")
  text3 = text2.replace('\u200b',"")
  return(text3)






