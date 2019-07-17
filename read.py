# 引入 sqlite 套件
import sqlite3


#定義資料庫位置
conn = sqlite3.connect('database.db') # ~代表路徑
db_connection = conn.cursor()
#t查詢數據
rows = db_connection.execute("SELECT serialno,patientno FROM Records;")
for row in rows:
    print(str(row[0]) , str(row[1]))
db_connection.close()