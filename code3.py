import requests
import bs4
req = requests.get("http://codeforces.com/contest/920/problem/A")
soup = bs4.BeautifulSoup(req.text,"html.parser")

a= soup.find_all(id='body')
b=a[0].find_all('div',recursive=False)
c=b[3].find_all('div',recursive=False)
d=c[1].find_all('div',recursive=False)

problem= d[1:]
e=problem[0].find_all('div', recursive=False)
problem_statement=e[0].find_all('div', recursive=False)


header= problem_statement[0].find_all('div', recursive=False)

title1=header[0].find_all('div', recursive=False)[0]
time_limit=header[0].find_all('div', recursive=False)[1]
memory_limit=header[0].find_all('div', recursive=False)[2]
input_file=header[0].find_all('div', recursive=False)[3]
output_file=header[0].find_all('div', recursive=False)[4]

#print(title1)
#print(time_limit)
#print(memory_limit)
#print(input_file)
#print(output_file)


input=problem_statement[0].find_all('div', recursive=False)
print(input)

