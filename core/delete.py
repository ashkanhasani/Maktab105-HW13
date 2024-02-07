import psycopg2


class Delete:
    """
    delete_mode=full : to delete all data
    delete_mode=part : to delete row that have col_label = value condition
    """
    con = psycopg2.connect(database="postgres", user="postgres", password="Ashkan@236236", host="127.0.0.1",
                           port="5432")
    cur = con.cursor()

    def __init__(self, table_name, delete_mode, col_label=None, value=None):
        self.table_name = table_name
        assert delete_mode in ["full", "part"], "your delete mode is not valid"
        self.delete_mode = delete_mode
        self.col_label = col_label
        self.value = value

    @classmethod
    def delete(cls, instance: object | list):
        assert isinstance(instance, object | list), "you should pass an object or list to delete method"
        if isinstance(instance, cls):
            assert isinstance(instance, cls), "you should pass an object from delete class to this method"
            if instance.delete_mode == "full":
                Delete.cur.execute(f'''DELETE FROM {instance.table_name};''')
                print("delete done.")
            else:
                Delete.cur.execute(f'''
                DELETE FROM {instance.table_name} 
                WHERE {instance.col_label}={instance.value};''')
                print("delete done.")
        else:
            for obj in instance:
                cls.delete(obj)
        Delete.con.commit()


if __name__ == "__main__":
    Delete.delete([Delete("ashkan", "part", "age", 10),
                   Delete("ashkan", "part", "age", 20),
                   Delete("ashkan", "part", "age", 21)])
    Delete.con.close()
