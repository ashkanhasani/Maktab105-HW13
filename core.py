import psycopg2
mydict={"NAME":"ashkan","AGE":21}
con = psycopg2.connect(database="postgres", user="postgres", password="Ashkan@236236", host="127.0.0.1", port="5432")
cur = con.cursor()
cur.execute(f'''
    SELECT
  COUNT (*)
FROM
  ashkan;''')
con.commit()
con.close()
print(a)
