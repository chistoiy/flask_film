import pymysql
conn = pymysql.connect('127.0.0.1','root','chis1chang',database='movie')
cursor = conn.cursor()
sql = "select * from role "
ret = cursor.execute(sql)
ret = cursor.fetchall()
print(ret)