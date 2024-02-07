import psycopg2


class Update:
    """
    update_mode= insert , for insert a new row
    update_mode= set: for update specific part of table
    """
    con = psycopg2.connect(database="postgres", user="postgres", password="Ashkan@236236", host="127.0.0.1",
                           port="5432")
    cur = con.cursor()

    def __init__(self, table_name, update_mode, key_tuple, value_tuple):
        self.table_name = table_name
        assert update_mode in ["insert", "set"], "your mode is not valid"
        self.update_mode = update_mode
        assert isinstance(key_tuple, tuple), "your keys should be in tuple"
        self.key_tuple = key_tuple
        assert isinstance(value_tuple, tuple), "your values should be in tuple"
        self.value_tuple = value_tuple

    @classmethod
    def update(cls, instance: object | list):
        assert isinstance(instance, object | list), "you should pass list or object to this clas"
        if isinstance(instance, cls):
            assert isinstance(instance, cls), "your instance should be an object from Update class"
            if instance.update_mode == "insert":
                Update.cur.execute(f'''
                    INSERT INTO {instance.table_name}
                    VALUES {instance.value_tuple};''')
                print("insert done.")
            else:
                assert len(instance.key_tuple) == 2, "you should have 2 col_label"
                Update.cur.execute(f'''
                        UPDATE {instance.table_name}
                        SET {instance.key_tuple[0]} = '{instance.value_tuple[0]}'
                        WHERE {instance.key_tuple[1]} = {instance.value_tuple[1]};
                        ''')
                print("set done.")
        else:
            for obj in instance:
                cls.update(obj)
        Update.con.commit()


if __name__ == "__main__":
    a = Update('ashkan', "insert", ('name', 'age'), ('bahar1', 10))
    b = Update('ashkan', "insert", ('name', 'age'), ('bahar2', 20))
    c = Update('ashkan', "insert", ('name', 'age'), ('bahar3', 21))
    Update.update([a, b, c])
    Update.con.close()
