import psycopg2 as psycopg2


class DataBase:
    def __init__(self, host="localhost", database="twitter", user="postgres", password="123456"):
        self.conn = psycopg2.connect(host=host, database=database, user=user, password=password)

    def insert(self, name):
        cur = self.conn.cursor()
        try:
            cur.execute("INSERT INTO test VALUES (%s)", (name,))
        except:
            pass
        self.conn.commit()
        cur.close()

    def pull_all(self):
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM test;")
        data = cur.fetchall()
        cur.close()
        return data