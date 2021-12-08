
from bs4 import BeautifulSoup
from urllib.request import urlopen

## 아래와 같은 코드 : with ~ as
# with urlopen('https://en.wikipedia.org/wiki/Main_Page') as response:
#     soup = BeautifulSoup(response, 'html.parser')
#     for anchor in soup.find_all('a'):
#         print(anchor.get('href', '/'))

response = urlopen('https://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(response, 'html.parser')
for anchor in soup.find_all('a'):
    print(anchor.get('href', '/'))