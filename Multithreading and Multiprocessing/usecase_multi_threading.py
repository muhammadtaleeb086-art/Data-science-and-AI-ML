"""
Real-world Example : Multi-threading for I/O-bound tasks
Scenario : Web Scraping
Web scraping is a common task that involves fetching data from websites. This process is often I/O-bound, as it spends a lot of time waiting for responses from the server. Using multi-threading can significantly speed up the scraping process by allowing multiple requests to be made simultaneously.
"""

"""

https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/
"""

import threading
import requests
from bs4 import BeautifulSoup 
urls=[
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_content(url):
    reponse=requests.get(url)
    soup=BeautifulSoup(reponse.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')

threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched")
