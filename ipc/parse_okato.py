from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor as TPE
from bs4 import BeautifulSoup as BS
from pprint import pprint as pp
from threading import Thread
from multiprocessing import Process, Queue, cpu_count
from queue import Empty
from traceback import print_exc
import psycopg2


def get_content(urls_q, content_q):
    while True:
        try:
            url = urls_q.get(timeout=2)
            if url:
                content = urlopen(url).read()
                print('got content')
                content_q.put(content)
        except:
            print('thread closed')
            break


def parse(urls_q, content_q):
    conn = psycopg2.connect('dbname=tree host=127.0.0.1 user=postgres password=postgres')
    cur = conn.cursor()
    cur.execute("""create table if not exists okato (
                          id serial primary key,
                          code varchar(11) null unique,
                          name varchar(200) not null,
                          centre varchar(100) not null);""")
    cur.execute("""create extension ltree;""")
    cur.execute("""delete from okato;""")
    conn.commit()

    rows = []
    # file = open('okato.txt', 'w')
    while True:
        try:
            content = content_q.get(timeout=7)
            print('parse content')
            trs = BS(content).find('table', class_='pos-list').find_all('tr')

            for tr in trs[1:]:
                # print(tr.td.a['href'])
                url = 'http://classifikator.ru' + getattr(tr.td.a, 'href', '')
                row = [td.string or getattr(td.a, 'string', '') for td in tr.find_all('td')]
                rows.append(row)
            args = ','.join([cur.mogrify("(%s,%s,%s)", r).decode() for r in rows])
            query = cur.mogrify("insert into okato (code, name, centre) values " + args)
            cur.execute(query)
            conn.commit()
            # pp(rows, file)  # запись в файл
        except:
            print_exc()
            print('worker closed')
            break
        finally:
            # file.close()
            cur.close()
            conn.close()


if __name__ == '__main__':
    urls_q, content_q = Queue(), Queue()
    urls_q.put('http://classifikator.ru/dic/okato/')

    worker = Process(target=parse, args=(urls_q, content_q))
    worker.start()

    for _ in range(cpu_count()*2):
        t = Thread(target=get_content, args=(urls_q, content_q))
        t.start()

    worker.join()