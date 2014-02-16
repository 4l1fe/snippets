import psycopg2

con = psycopg2.connect(host='localhost', port='5432', dbname='unittests_DB', user='postgres', password='postgres')
cur = con.cursor()

cur.execute('select * from "ОписаниеБазыДанных"')
for rec in cur.fetchall():
    print(rec)
cur.close()
con.close()