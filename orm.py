# R - realtion
import sqlite3
con = sqlite3.connect('chinook.db')

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


con.row_factory = dict_factory
cur = con.cursor()

sql_query = '''
SELECT * FROM customers;
'''
cur.execute(sql_query)

customers = cur.fetchall()

con.close()

# O - Object
class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


# M - mapping
customer_objects = []
for c in customers:
    customer_objects.append(
        Customer(c['FirstName'], c['LastName'])
    )



# Usage
for cust in customer_objects:
    print(cust.get_full_name())

#  ORM
# O - object
# R - relation (table)
# M - mapping


'''
1. Установить flake8 и исправить все ошибки
2. Настроить travis ci.
3. показать все записи модели ContactUs

filter
exclude
order_by
values_list

get
create
count
first
last
exists

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#field-lookups
'''

'''
ETL
1. (Extract) get info (sources - json, csv, html, (authorization))
2. (Transform) normalize (2020/12/30) (2020-12-30, 30-12-2020, 30/12/2020, 30-12-2020T12:12:46)
3. (Load) Load data (sve to database, external API)
'''
