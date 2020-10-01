from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

password = os.environ['MYSQL_ROOT_PASSWORD']
connection = mysql.connector.connect(
    host='mysql-cluster-ip-service',
    port=3306,
    user='root',
    password=password    
)

cur = connection.cursor()
cur.execute("SHOW DATABASES")
dbs = []
for d in cur:    
    dbs.append(d[0])
connection.close()

# URL will will be prefixed with "/parser/" before all routes
@app.route('/')
def hello_world():     
    l = ','.join(dbs)
    return "Here are the databases: {0}".format(l)
    


if __name__ == '__main__':    
    app.run(debug=True, host='0.0.0.0')    