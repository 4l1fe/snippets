from bs4 import BeautifulSoup
import bisect
try:
    from urllib.request import urlopen
except:
    from urllib import urlopen


site = 'http://crate.io/?has_releases=on&q={search}'
search = 'http'

page = BeautifulSoup(urlopen(site.format(search=search)))
# page = BeautifulSoup(requests.get(site.format('/?has_releases=on&q={search}').format(search=search)).content)

table = []

while True:

    for result in page.find_all('div', attrs={'class':'result'}): # строка с именем пакета  и количеством загрузок
        count = result.find('span', attrs={'class':'count'}).string # загрузки
        count = int(count.replace(',', ''))
        package_name = result.find(attrs={'class':'package-name'}).string # имя пакета
        couple = [count, package_name]
        bisect.insort_right(table, couple) # добавляю в список через сортировку

    li = page.find('li', attrs={'class':'next'}) # строка с ссылку на след страницу
    print(li['class'])
    if 'disabled' in li['class']: break # если найден disabled, то это последняя страница - выход
    page = BeautifulSoup(urlopen(site.format(li.a['href']))) # перехожу на след страницу
    # page = BeautifulSoup(requests.get(site.format(li.a['href'])).content)

table.reverse() # хочу видеть на первых позициях пакет с большим кол загрузок
for num, i in enumerate(table): print(num, i)
