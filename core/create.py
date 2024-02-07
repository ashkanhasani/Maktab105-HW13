import enum
import psycopg2


class TypeMode(enum.Enum):
    string = "CHAR(255)"
    text = "TEXT(1000)"
    bool = "BOOLEAN"
    integer = "INT"
    decimal = "FLOAT"
    date = "DATE"


class Table:
    __registered = {}

    def __init__(self, table_name: str, col_label: list, modes: list):
        assert len(col_label) == len(modes), "the number of labels and modes should be equal"
        assert isinstance(col_label, list), "your labels should define in a list"
        self.col_label = col_label
        for mode in modes:
            assert TypeMode[mode], f"the {mode} is not valid"
        self.modes = modes
        self.table_name = table_name

    def register(self):
        for i in range(len(self.col_label)):
            Table.__registered.update({self.col_label[i]: TypeMode[self.modes[i]].value})

    @classmethod
    def create(cls, instance: object | list):
        cls.__registered = {}
        if isinstance(instance, cls):
            instance.register()
            con = psycopg2.connect(database="postgres", user="postgres", password="Ashkan@236236", host="127.0.0.1",
                                   port="5432")
            cur = con.cursor()
            cur.execute(f'''CREATE TABLE IF NOT EXISTS {instance.table_name}();''')
            con.commit()
            con.commit()
            for key, value in cls.__registered.items():
                cur.execute(
                    f'''
                    ALTER TABLE {instance.table_name}
                    ADD {key} {value};
                    '''
                )
            con.commit()
            con.close()
        elif isinstance(instance, list):
            for table in instance:
                cls.create(table)


if __name__ == "__main__":
    Table.create(Table("ashkan", ["name", "age"], ["string", "integer"]))
