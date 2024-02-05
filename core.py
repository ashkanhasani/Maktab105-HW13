import psycopg2
mydict={"NAME":"ashkan","AGE":21}
con = psycopg2.connect(database="postgres", user="postgres", password="Ashkan@236236", host="127.0.0.1", port="5432")
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS test(
    NAME VARCHAR,
    AGE INT

);''')

cur.execute(f'''CREATE TABLE test2(
    {list(mydict.keys())[0]} VARCHAR,
    {list(mydict.keys())[1]} INT)''')
con.commit()
con.close()