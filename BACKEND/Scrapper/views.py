
# from django.conf.urls import url
from django.http import response
from Web_Scrapper import urls


# Create your views here.


import requests
from bs4 import BeautifulSoup 
import lxml
from collections import Counter
import pandas as pd
import re
import nltk
# from IPython.display import display
import string
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from django.shortcuts import render
import io
import urllib, base64
import json
from nltk.corpus import wordnet as wn
from rest_framework.response import Response



def index (request):
  return render(request, 'index.html')

def scrapednews (link):
  source = requests.get(link).text
  soup = BeautifulSoup(source, 'lxml')
  a = soup.body.text
  a = a.lower()
  return a

def scrapout (links):
  nltk.download('wordnet')
  nltk.download('stopwords')
  nltk.download('words')
  nltk.download('vader_lexicon')
  wn = nltk.WordNetLemmatizer()
  ps = nltk.PorterStemmer()
    
  e = []
  for i in links:
      source = requests.get(i).text
      soup = BeautifulSoup(source, 'lxml')
      a = soup.body.text
      a = a.lower()
      b = a.split()
      e+=b
  c = []
  d = []
  for i in e:
      if i not in d:
          c.append([i,e.count(i)])
          d.append(i)

  stopwords = nltk.corpus.stopwords.words('english')
  lst=[]
  for i in d:
    a=i.lower()
    lst.append(a)
  text = " ".join([word for word in lst if word not in string.punctuation])
  tokens = re.split('\W+', text)
  text_a = [word for word in tokens if word not in stopwords]
  texta = [wn.lemmatize(word) for word in text_a]
  final=list(texta)

  remove = str.maketrans('', '', string.punctuation)
  out_list = [s.translate(remove) for s in final]
  final1 = [x for x in out_list if not any(x1.isdigit() for x1 in x)]
  final2 = [x for x in final1 if len(x)>2]

  words = set(nltk.corpus.words.words())
  sent = ' '.join(final2)
  b = " ".join(w for w in nltk.wordpunct_tokenize(sent) \
          if w.lower() in words or not w.isalpha())
  f = b.split()
  g = []
  h = []
  for i in f:
      if i not in h:
          g.append([i,f.count(i)])
          h.append(i)
  emote_list = []
  with open('Scrapper/emot.txt','r') as files:
    for line in files:
      final_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()
      word,emotions = final_line.split(':')
      if word in h:
        emote_list.append(emotions)

  w = Counter(emote_list)

  negl=[]
  posl=[]
  neul=[]
  for i in h:

    score = SentimentIntensityAnalyzer().polarity_scores(i)
    neg = score['neg']
    pos = score['pos']
    neu = score['neu']
    if neg>pos:
      negl.append(i)
    elif pos>neg:
      posl.append(i)
    else:
      neul.append(i)

  a_dictionary = {"Neutral": 0, "Positive": 0, "Negative": 0}
  a_dictionary["Neutral"] = len(neul)
  a_dictionary["Positive"] = len(posl)
  a_dictionary["Negative"] = len(negl)
  max_key = max(a_dictionary, key=a_dictionary.get)
  # print("\n\n")
  vibe_render = "Overall Vibe of Scraped Data is "+str(max_key)+" inclined towards "+ list(a_dictionary.keys())[list(a_dictionary.values()).index(sorted(a_dictionary.values())[-2])]
  # print(vibe_render)

 
  a = {'Negative_Words': negl ,'Positive_Words': posl , 'Neutral_Words': neul }
  percentile_list = pd.DataFrame.from_dict(a, orient='index')
  percentile_list.T.to_csv('Neg_Pos_Neu_DATA.csv',index = True)
  percentile_list = percentile_list.transpose()
  print("\n\n")
  # display(percentile_list)
  df = pd.read_csv('Neg_Pos_Neu_DATA.csv')

  json_records = df.reset_index().to_json(orient ='records')
  table_data = []
  table_data = json.loads(json_records)
  print(table_data)

  # TODO >_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_

  fig,ax1 = plt.subplots()
  ax1.bar(w.keys(),w.values())
  fig.autofmt_xdate()
  # plt.savefig('graph.png')
  pps = ax1.bar(w.keys(), w.values(), align='center')
  for p in pps:
    height = p.get_height()
    ax1.text(x=p.get_x() + p.get_width() / 2, y=height+.10,
        s="{}%".format(height),
        ha='center')

   # convt to string
  # buf = io.BytesIO()
  fig.savefig('plt.png')
  # fig.close()
  with open('plt.png', 'rb') as img_file:
        # img_data = img_file.read()
        img_base64 =  base64.b64encode(img_file.read()).decode('utf-8')
  # buf.seek(0)
  # string_img = base64.b64encode(buf.read()).decode('utf-8')
  # uri = 'plt.png'
  
  
  variables = {
    'vibe': vibe_render,
    'data': img_base64,
    'table': table_data
  }
  print(variables)
  return variables


def textscrapout (request):
  nltk.download('wordnet')
  nltk.download('stopwords')
  nltk.download('words')
  nltk.download('vader_lexicon')
  wn = nltk.WordNetLemmatizer()
  ps = nltk.PorterStemmer()

  text_io=request.POST.get('text')  

  d = list(text_io.split(" "))
  stopwords = nltk.corpus.stopwords.words('english')
  lst=[]
  for i in d:
    a=i.lower()
    lst.append(a)
  
  text = " ".join([word for word in lst if word not in string.punctuation])
  tokens = re.split('\W+', text)
  text_a = [word for word in tokens if word not in stopwords]
  texta = [wn.lemmatize(word) for word in text_a]
  final=list(texta)

  remove = str.maketrans('', '', string.punctuation)
  out_list = [s.translate(remove) for s in final]
  final1 = [x for x in out_list if not any(x1.isdigit() for x1 in x)]
  final2 = [x for x in final1 if len(x)>2]

  words = set(nltk.corpus.words.words())
  sent = ' '.join(final2)
  b = " ".join(w for w in nltk.wordpunct_tokenize(sent) \
          if w.lower() in words or not w.isalpha())
  f = b.split()
  g = []
  h = []
  for i in f:
      if i not in h:
          g.append([i,f.count(i)])
          h.append(i)
  print(list(set(h)))
  print(len(h))
  emote_list = []
  with open('Scrapper/emot.txt','r') as files:
    for line in files:
      final_line = line.replace("\n",'').replace(",",'').replace("'",'').strip()
      word,emotions = final_line.split(':')
      if word in h:
        emote_list.append(emotions)

  w = Counter(emote_list)
  

  negl=[]
  posl=[]
  neul=[]
  for i in h:

    score = SentimentIntensityAnalyzer().polarity_scores(i)
    neg = score['neg']
    pos = score['pos']
    neu = score['neu']
    if neg>pos:
      negl.append(i)
    elif pos>neg:
      posl.append(i)
    else:
      neul.append(i)

  a_dictionary = {"Neutral": 0, "Positive": 0, "Negative": 0}
  a_dictionary["Neutral"] = len(neul)
  a_dictionary["Positive"] = len(posl)
  a_dictionary["Negative"] = len(negl)
  max_key = max(a_dictionary, key=a_dictionary.get)
  vibe_render = "Overall Vibe of Scraped Data is "+str(max_key)+" inclined towards "+ list(a_dictionary.keys())[list(a_dictionary.values()).index(sorted(a_dictionary.values())[-2])]


  #TODO >_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>


  a = {'Negative_Words': negl ,'Positive_Words': posl , 'Neutral_Words': neul }
  percentile_list = pd.DataFrame.from_dict(a, orient='index')
  percentile_list.T.to_csv('Neg_Pos_Neu_DATA.csv',index = True)
  percentile_list = percentile_list.transpose()
  

  df = pd.read_csv('Neg_Pos_Neu_DATA.csv')

  json_records = df.reset_index().to_json(orient ='records')
  table_data = []
  table_data = json.loads(json_records)
  print(table_data)

  #TODO >_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>


  fig,ax1 = plt.subplots()
  ax1.bar(w.keys(),w.values())
  fig.autofmt_xdate()
  pps = ax1.bar(w.keys(), w.values(), align='center',color=['cyan'])
  for p in pps:
    height = p.get_height()
    ax1.text(x=p.get_x() + p.get_width() / 2, y=height+.10,
        s="{}%".format(height),
        ha='center')

  buf = io.BytesIO()
  fig.savefig(buf, format='png')
  buf.seek(0)
  string_img = base64.b64encode(buf.read()).decode("utf-8")
  uri = urllib.parse.quote(string_img)
  print("\n\nEmotional Analysis",uri)

  #TODO >_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>_>
  variables_ = {
    'vibe': vibe_render,
    'data': uri,
    'table': table_data
  } 

  return render(request, 'text_data_scrap.html', variables_)



from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getData(request):
  # print(scrapout([request.GET.get('url')]))
  return Response(scrapout([request.GET.get('url')]))


@api_view(['GET'])
def getChatcontent(request):
  return Response(scrapednews(request.GET.get('url')))












    



