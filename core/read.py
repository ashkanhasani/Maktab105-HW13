import psycopg2


class Read:
    con = psycopg2.connect(database="postgres", user="postgres", password="Ashkan@236236", host="127.0.0.1",
                           port="5432")
    cur = con.cursor()

    def __init__(self, table_name):
        self.table_name = table_name

    @classmethod
    def read(cls, instance: object | list):
        if isinstance(instance, cls):
            Read.cur.execute(f'''SELECT * FROM {instance.table_name};''')
            rows = Read.cur.fetchall()

            for row in rows:
                for i in range(len(row)):
                    print(row[i])
                print("-" * 10, "next row", "-" * 10)


if __name__ == "__main__":
    Read.read(Read("ashkan"))
    Read.con.close()
