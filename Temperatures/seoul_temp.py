import psycopg2

host = 'arjuna.db.elephantsql.com'
user = 'sdzmzmbl'
password = 'YC1tuq4XEQ3slSwhEttfkPT-l8furrsW'
database = 'sdzmzmbl'

connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# 나머지 코드는 titanic.csv 의 데이터를 passenger 테이블로 전달할 수 있도록 자유롭게 작성해주시기 바랍니다.

cur = connection.cursor()
# DB passenger 존재하면 삭제
cur.execute("DROP TABLE IF EXISTS seoul_temp")
# 테이블 만들기
cur.execute("""CREATE TABLE seoul_temp(
                            id INT NOT NULL PRIMARY KEY,
                            date VARCHAR,
                            avg_temp FLOAT,
                            min_temp FLOAT,
                            max_temp FLOAT);""")

import csv

with open('seoul_month_temp.csv', 'r') as f:
    csv_reader = csv.DictReader(f)
    for idx, i in enumerate(csv_reader):
        # print(f"""VALUES({idx}, {i['date']}, {i['avg_temp']}, {i['min_temp']}, {i['max_temp']})""")
        cur.execute(f"""INSERT INTO seoul_temp(id, date, avg_temp, min_temp, max_temp)
                        VALUES({idx}, {i['date']}, {i['avg_temp']}, {i['min_temp']}, {i['max_temp']});
                        """)

connection.commit()
cur.close()
connection.close()