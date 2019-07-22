# 引入 sqlite 套件
import sqlite3
import struct
# import binascii


#定義資料庫位置
conn = sqlite3.connect('database.db') # ~代表路徑
db_connection = conn.cursor()
#t查詢數據
rows = db_connection.execute("SELECT serialno,time,length,date,ecg,qrs,beat,feature,measurement,marker,scale,parameter FROM Records;")
for row in rows:
    # print ("serialno = ", row[0])
    # print ("time = ", row[1])
    # print ("length = ", row[2])
    # print ("date = ", row[3])
    # print ("ecg = ", row[4])
    # print ("qrs = ", row[5])
    # print ("beat = ", row[6])
#     print ("feature = ", row[7].hex())
#     print ("measurement = ", row[8].hex())
#     print ("marker = ", row[9].hex())
    # print ("scale = ", row[10],"\n")
    # print ("parameter = ", binascii.hexlify(row[11]))
    print("parameter = ",struct.unpack('!f', row[11].hex().decode('hex'))[0],"\n" )
db_connection.close()
