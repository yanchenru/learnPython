import pymysql 
conn = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql') 
cur = conn.cursor() 
cur.execute("USE scraping")
