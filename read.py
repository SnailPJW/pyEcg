# 引入 sqlite 套件
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

#定義資料庫位置
conn = sqlite3.connect('database.db')
db_connection = conn.cursor()

List_Ecg_Signal = []          ## 空列表

#t查詢數據
rows = db_connection.execute("SELECT serialno,time,length,date,ecg,qrs,beat,feature,measurement,marker,scale,parameter FROM Records;")
for row in rows:
    # print ("serialno = ", row[0])
    # print ("time = ", row[1])
    # print ("length = ", row[2])
    # print ("date = ", row[3])
#     print ("ecg = ", np.frombuffer(row[4], dtype='<f4'),"\n")
    # print ("qrs = ", row[5])
    # print ("beat = ", row[6])
#     print ("feature = ", row[7].hex())
#     print ("measurement = ", row[8].hex())
#     print ("marker = ", row[9].hex())
    # print ("scale = ", row[10],"\n")
    # print ("parameter = ", binascii.hexlify(row[11]))
#     print("parameter = ",float.fromhex(row[11].hex()),"\n" )
    #   print("parameter = ", np.frombuffer(row[11], dtype=np.float32),"\n" )
    List_Ecg_Signal.append(np.frombuffer(row[4], dtype='<f4'))
        
db_connection.close()


