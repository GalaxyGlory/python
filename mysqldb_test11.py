# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(host='192.168.45.12',user='root', password='oracle', database='sampdb', use_unicode=True)
cursor = conn.cursor()

cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()

# 关闭Cursor和Connection:
cursor.close()
conn.close()