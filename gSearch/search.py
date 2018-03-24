from googlesearch import search
url_list = []
for url in search('Hong Kong', stop=10):
            url_list.append(url)
print(url_list)




