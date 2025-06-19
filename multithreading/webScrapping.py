# as we know the multithreading is I/O (input output) bound tasks , we have a live example for the i/o bound task that is web scrapping , web scrapping is a technique making the network request to get the web data from the websites , and it can take time , so for the concurrent tasks and improve the speed we gona use the multithreading

# bs4 (beautiful soup 4) used for the web scrapping

import threading 
import requests
from bs4 import BeautifulSoup

urls = [
        'https://langchain-ai.github.io/langgraph/concepts/why-langgraph/'

]

def fetchContent(url):
     print('inside the fetcch content')
     res = requests.get(url)
     soup = BeautifulSoup(res.content , 'html.parser')
     print(f'fetched{len(soup.text)} from {url}')


threads = []

for url in urls:
     thread = threading.Thread(target=fetchContent,args=(url,))
     threads.append(thread)
     thread.start()
for thr in threads:
     thr.join()

print('excution is done')

