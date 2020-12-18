from flask import Flask
import os
import BusinessObjects as bo
import DataObjects as do

app = Flask(__name__)
db_ip = os.getenv("dp_ip") #'10.0.2.15'
ConnectionData = {}
ConnectionData['user'] = 'postgres'
ConnectionData['pastword'] = 'postgres'
ConnectionData['host'] = str(db_ip)
ConnectionData['post'] = '5432'
ConnectionData['Database'] = 'northwind'

@app.route("/")
def hello():
    c1 = bo.Customer(1, 'dauXanh', 'peter', '556 Nui Thanh', 'Da nang', '50000', 'Viet Nam' )
    return c1.CustomerName

@app.route("/test_Insert")
def test_Insert():
    c2 = bo.Customer(ConnectionData)
    c1 = bo.Customer(1, 'dauXanh', 'peter', '556 Nui Thanh', 'Da nang', '50000', 'Viet Nam' )
    s1 = c2.insert(c1)
    return s1

    if __name__ == "__main__" :
        app.run(host= '0.0.0.0', port = 8080 )
