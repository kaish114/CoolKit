import requests
from sys import argv
from bs4 import BeautifulSoup
import pandas as pd
 
name='srbcheema1'
if(len(argv)==2):
 name=argv[1]
 
req=requests.get('http://codeforces.com/contests/with/'+name)
soup=BeautifulSoup(req.text,'html.parser')
 
 
a=soup.find_all(id='body')
b=a[0].find_all('div',recursive=False)
#inside body
c=b[3].find_all('div',recursive=False)
d=c[1].find_all('div',recursive=False)
e=d[2].find_all('div',recursive=False)
f=e[5].find_all('table',recursive=False)
g=f[0].find_all('thead',recursive=False)
#went inside table
h=g[0].find_all('tr',recursive=False)
#went inside thead
l=h[0].get_text('')
print(l[1],end=('                         '))
print(l[3:10],end=('                         '))
print(l[11:15],end=('    '))
print(l[16:22])
i=f[0].find_all('tbody',recursive=False)
j=i[0].find_all('tr',recursive=False)
#print(j[0].get_text())
a=[]
b=[]
c=[]
d=[]
for row in i.find('tr'):
    cells = row.findAll('td')
    states=row.findAll('a') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        a.append(cells[0].find(text=True))
        b.append(states[0].find(text=True))
        c.append(cells[1].find(text=True))
        d.append(cells[2].find(text=True)) 
df=pd.DataFrame(a,columns=['#'])
df['Contest']=b
df['Rank']=c
df['Solved']=d
df