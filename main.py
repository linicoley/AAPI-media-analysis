from striprtf.striprtf import rtf_to_text
import os 

##sources:
#https://stackoverflow.com/questions/60897366/how-to-read-rtf-file-and-convert-into-python3-strings-and-can-be-stored-in-pyth

months = {"January" : 1, "February" : 2, "March" : 3, "April" : 4, "May" : 5, "June" : 6, "July" : 7, "August" : 8, "September" : 9, "October" : 10, "November" : 11, "December" : 12}

def print_full_file(file):
  with open(file) as infile:
      for line in infile:
        text = rtf_to_text(line)
        #print(text)

#print_full_file("test.RTF")
#print_full_file("test folder/fox.RTF")

sources = {"MSNBC", "Fox News Network", "The Daily Beast", "The Washington Times"}

def get_source(file):
  source = ""
  with open(file) as infile: 
    for line in infile:
      text = rtf_to_text(line)
      if any(source in text for source in sources):
        if text.startswith("MSNBC") :
          source = "MSNBC"
        elif text.startswith("Fox News Network") :
          source = "Fox News Network"
        elif text.startswith("The Daily Beast") :
          source = "The Daily Beast"
        elif text.startswith("The Washington Times") :
          source = "The Washington Times"
  return source

def get_title(file):
  title = ""
  with open(file) as infile:
    for line in infile:
      text = rtf_to_text(line)
      #this is kinda just hardcoding...
      if "heading" in text or "Normal" in text or "|" in text or "\n" in text or "Load-Date" in text or len(text) == 0:
        continue
      else:
        return title

#print(get_title("test.RTF"))

def get_date_string(file, source_name):
  #date_string = ""
  reached_source_name = False
  with open(file) as infile:
    for line in infile:
      text = rtf_to_text(line)
      if source_name in text:
        reached_source_name = True
        continue
      if reached_source_name and any(x in text for x in list(months)):
        return text

#print(get_date_string("test folder/fox.RTF", "Daily Beast"))
#print(get_date_string("test.RTF", "Washington Times"))

#def make_date(string):
  #date_split = string.split(" ")

def get_body(file):
  to_print = False
  test_string = ""
  with open(file) as infile:
      for line in infile:
        text = rtf_to_text(line)
        if "Body" in text:
          to_print = True
          continue
        elif "Load-Date" in text:
          to_print = False
          break
        if to_print:
          test_string += text.strip()
  return test_string

#test = get_body("test folder/spartacus.RTF")
#print(test)

def make_doc(file, source_name):
  doc = {}
  doc['date'] = get_date_string(file, source_name)
  doc['source'] = source_name
  #doc['title'] = get_title(file)
  doc['text'] = get_body(file)
  return doc

#import json

data = {}
data['docs'] = []
for filename in os.listdir("msnbcfox/") :
  if get_source("msnbcfox/"+filename) == "Fox News Network" :
    data['docs'].append(make_doc("msnbcfox/"+filename, "Fox News Network"))

# data['docs'].append(make_doc("test folder/spartacus.RTF", "Washington Times"))
# data['docs'].append(make_doc("test folder/fox.RTF", "Daily Beast"))
# data['docs'].append(make_doc("test folder/russian.RTF", "Daily Beast"))

# with open('data.txt', 'w') as outfile:
#   json.dump(data, outfile)

import numpy as np
import pandas as pd

#try to make a CSV with the data from RTFs
titles = []
source = []
dates = []
body = []

for doc in data['docs']:
  source.append(doc['source'])
  dates.append(doc['date'])
  body.append(doc['text'])

df = {'source' : source, 'date' : dates, 'text' : body}
df = pd.DataFrame(df)
df.to_csv("fox.csv")

