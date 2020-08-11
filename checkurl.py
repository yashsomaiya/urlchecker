import urllib.request
import pandas as pd
from urllib.request import Request, urlopen
import winsound

p=2
df_csv= pd.read_csv('E:\\fakenews\\fakebot\\politifact_data.csv',error_bad_lines=False, quotechar='"', thousands=',', low_memory=False)
for index, row in df_csv.iterrows():
    req = Request(row['news_url'], headers={'User-Agent': 'Mozilla/5.0'})

    if(urllib.request.urlopen(req).getcode()==200):
        print("ok",p)
        p+=1
        print('\007')
    elif(urllib.request.urlopen(row['news_url']).getcode()!=200):
        print("not okay",row['news_url'])

winsound.Beep(500, 1000)

print('\007')


