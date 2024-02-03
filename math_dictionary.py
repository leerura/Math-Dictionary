import requests, bs4, csv

storage = []
for number in range (0,339):
    URL = 'https://www.kms.or.kr/mathdict/list.html?start='+str(30*number)+'&sort=ename&key=&keyword=&alpa=#none'
    response = requests.get(URL,headers={"User-Agent":"Mozilla/5.0"})
    soup = bs4.BeautifulSoup(response.text,"html.parser")
    result = soup.find_all('td')
    
    for i in result:
        storage.append(i.text)

English = []
Korean = []

for j in range (0,10150):
    English.append(storage[2*j])
    Korean.append(storage[2*j+1])

f = open('contents.csv' , 'w', newline = '')
wr = csv.writer(f)
wr.writerow(English)
wr.writerow(Korean)
f.close()