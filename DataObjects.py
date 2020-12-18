import psycopg2
class Customer:
    def __init__(self, ConnectionData):
        self.ConnectionData = ConnectionData
    def insert(self, customer):
        con = None
        try:
            con = psycopg2.connect(user = self.ConnectionData['user'],
                                   password = self.ConnectionData['password'],
                                   host = self.ConnectionData['host'],
                                   database = self.ConnectionData['database'] )
            cur = con.cursor()
            sql = "INSERT INFO TblCustomers(CustomeName, ContacName,Address, City, PostalCode, Country) VALUES (%s,%s,%s,%s,%s)"
            record_to_insert =(customer.CustomeName, customer.ContacName, customer.Address, customer.City, customer.PostalCode, customer.Country)
            cur.execute(ssql, record_to_insert)
            con.commit()
            con.close()
            return 'Insert TblCustomers successfully'
        except (Exception, psycopg2.DatabaseError) as error :
            return str(error)
        finally: 
            if con is not None:
                con.close()
if __name__ == "__main__"
    print('this is data object packege')
                                