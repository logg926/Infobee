from googlesearch import search
from chtext import htmlText

url_list = []
for url in search('Hong Kong', stop=1):
    url_list.append(url)

for item in url_list:
    htmlText(item)
    print('\n'*100)





