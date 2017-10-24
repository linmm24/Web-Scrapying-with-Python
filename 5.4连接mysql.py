import pymysql
#创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', passwd='root', db='book', charset='utf8')
#创建游标
cur = conn.cursor()
#执行sql
cur.execute("SELECT * FROM bookinfo WHERE id=1")
#获取剩余结果的前n行数据
print(cur.fetchmany(3))
#获取剩余结果的第一行数据
#print(cur.fetchone())
#所有行数据   fetchall()
#返回受影响的行数
effect_row = cur.execute("select * from bookinfo")
print(effect_row )
# 提交，不然无法保存新建或者修改的数据
conn.commit()
cur.close()
conn.close()